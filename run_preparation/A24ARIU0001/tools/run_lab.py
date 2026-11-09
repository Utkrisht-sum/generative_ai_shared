#!/usr/bin/env python3
"""Execute a notebook with live terminal output and save outputs after each cell."""
import argparse
import ast
import base64
import contextlib
import io
import json
import os
from pathlib import Path
import sys
import traceback
import time

os.environ.setdefault("OMP_NUM_THREADS", "4")
os.environ.setdefault("MKL_NUM_THREADS", "4")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

class Tee(io.TextIOBase):
    def __init__(self, target, buffer): self.target, self.buffer = target, buffer
    def write(self, text):
        self.target.write(text); self.target.flush(); self.buffer.write(text)
        return len(text)
    def flush(self): self.target.flush()
    def isatty(self): return False

class Override(ast.NodeTransformer):
    def __init__(self, values): self.values = values
    def visit_Assign(self, node):
        if len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            key = node.targets[0].id
            if key in self.values:
                node.value = ast.parse(repr(self.values[key]), mode="eval").body
        return node

def run(path, output, overrides, through_cell=None):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import IPython.display as ipdisplay
    notebook = json.loads(path.read_text())
    output.parent.mkdir(parents=True, exist_ok=True)
    scope = {"__name__": "__main__"}
    count = 0
    original_display = ipdisplay.display
    print("Notebook:", path, "\nSaving:", output, "\nOverrides:", overrides, flush=True)
    for index, cell in enumerate(notebook["cells"]):
        if through_cell is not None and index >= through_cell: break
        if cell["cell_type"] != "code": continue
        count += 1
        cell.update(outputs=[], execution_count=count)
        buffer = io.StringIO()
        def display(*objects, **kwargs):
            for obj in objects:
                if hasattr(obj, "_repr_html_"):
                    html = obj._repr_html_()
                    cell["outputs"].append({"output_type": "display_data", "metadata": {},
                        "data": {"text/plain": repr(obj), "text/html": html or repr(obj)}})
                else:
                    print(obj)
        def show(*args, **kwargs):
            for number in plt.get_fignums():
                data = io.BytesIO()
                plt.figure(number).savefig(data, format="png", bbox_inches="tight", dpi=120)
                cell["outputs"].append({"output_type": "display_data", "metadata": {},
                    "data": {"image/png": base64.b64encode(data.getvalue()).decode(), "text/plain": "<Figure>"}})
            plt.close("all")
        ipdisplay.display = display
        scope["display"] = display
        plt.show = show
        print(f"\n--- Cell {index + 1}/{len(notebook['cells'])} ---", flush=True)
        try:
            tree = Override(overrides).visit(ast.parse("".join(cell["source"])))
            ast.fix_missing_locations(tree)
            last = tree.body.pop() if tree.body and isinstance(tree.body[-1], ast.Expr) else None
            with contextlib.redirect_stdout(Tee(sys.stdout, buffer)), contextlib.redirect_stderr(Tee(sys.stderr, buffer)):
                exec(compile(tree, f"{path}:cell{index}", "exec"), scope)
                if last:
                    value = eval(compile(ast.Expression(last.value), str(path), "eval"), scope)
                    if value is not None: display(value)
                if plt.get_fignums(): show()
        except BaseException as exc:
            if buffer.getvalue(): cell["outputs"].insert(0, {"output_type": "stream", "name": "stdout", "text": buffer.getvalue()})
            cell["outputs"].append({"output_type": "error", "ename": type(exc).__name__,
                "evalue": str(exc), "traceback": traceback.format_exc().splitlines()})
            output.write_text(json.dumps(notebook, indent=1) + "\n")
            raise
        finally:
            ipdisplay.display = original_display
        if buffer.getvalue(): cell["outputs"].insert(0, {"output_type": "stream", "name": "stdout", "text": buffer.getvalue()})
        output.write_text(json.dumps(notebook, indent=1) + "\n")
    print("\nFinished " + (f"selected prefix (cells 1-{through_cell})" if through_cell else "all cells") + ". Executed notebook:", output, flush=True)
    return scope

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("notebook", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--through-cell", type=int, help="Run a prefix through this 1-based cell number; this is not a complete lab run")
    parser.add_argument("--serve", action="store_true", help="Open the logged Gradio app after execution and keep it running")
    parser.add_argument("--set", action="append", default=[], metavar="NAME=JSON")
    options = parser.parse_args()
    if options.through_cell is not None and options.through_cell < 1:
        parser.error("--through-cell must be positive")
    overrides = {}
    for entry in options.set:
        key, value = entry.split("=", 1); overrides[key] = json.loads(value)
    path = options.notebook.resolve()
    output = options.output.resolve() if options.output else path.with_name(path.stem + ".executed.ipynb")
    if output == path: parser.error("Choose a separate output notebook")
    scope = run(path, output, overrides, options.through_cell)
    if options.serve:
        if "demo_test" not in scope:
            parser.error("--serve is available for the Gradio notebook")
        scope["RUN_UI"] = True
        scope["launch"](scope["demo_test"])
        print("Partner app running; press Ctrl+C when finished.", flush=True)
        try:
            while True: time.sleep(1)
        except KeyboardInterrupt:
            for app in scope.get("_running", []): app.close()
