"""Prepare the offline patent runtime without replacing compatible image packages."""
from pathlib import Path
import importlib
import json
import subprocess
import sys
from importlib import metadata

ROOTS = [
    "transformers==5.22.2", "accelerate==1.15.0", "datasets==5.1.0",
    "scikit-learn>=1.4", "sentencepiece==0.2.3", "protobuf",
    "pandas>=2.1", "matplotlib>=3.8",
]

if Path("/kaggle/input").exists():
    candidates = sorted(Path("/kaggle/input").rglob("patent_runtime_wheels/wheels_manifest.json"))
    assert candidates, "Attach PATENT_DOWNLOAD_WEIGHTS output, including patent_runtime_wheels."
    manifest_path = candidates[0]
    manifest = json.loads(manifest_path.read_text())
    assert manifest["python"].split(".")[:2] == [str(sys.version_info.major), str(sys.version_info.minor)], \
        "The weights/wheels and notebook need the same Python major/minor version."
    roots = manifest.get("root_requirements", ROOTS)
    torch_before = metadata.version("torch")
    constraints = Path("/kaggle/working/patent_keep_cuda_torch.txt")
    constraints.write_text("torch==" + torch_before + "\n")
    base = [sys.executable, "-m", "pip", "install", "--disable-pip-version-check",
            "--no-index", "--find-links", str(manifest_path.parent), "-c", str(constraints)]
    report_path = Path("/kaggle/working/patent_runtime_plan.json")
    subprocess.run([*base, "--dry-run", "--report", str(report_path), *roots], check=True)
    planned = json.loads(report_path.read_text()).get("install", [])
    print("Offline package changes:", [p["metadata"]["name"] for p in planned], flush=True)

    # A loaded, unchanged dependency does not require a restart. Check the actual
    # module files belonging to distributions that pip proposes to replace.
    loaded_changes = {}
    loaded_files = {}
    for name, module in list(sys.modules.items()):
        origin = getattr(module, "__dict__", {}).get("__file__") if module else None
        if origin:
            loaded_files[name] = Path(origin).resolve()
    for package in planned:
        name = package["metadata"]["name"]
        try:
            dist = metadata.distribution(name)
        except metadata.PackageNotFoundError:
            continue
        files = {Path(dist.locate_file(f)).resolve() for f in dist.files or []}
        loaded = sorted(name for name, path in loaded_files.items() if path in files)
        if loaded:
            loaded_changes[name] = loaded[:8]
    if loaded_changes:
        raise RuntimeError("A fresh kernel is required BEFORE replacing loaded packages: "
                           + json.dumps(loaded_changes, sort_keys=True))
    if planned:
        subprocess.run([*base, *roots], check=True)
        importlib.invalidate_caches()
    assert metadata.version("torch") == torch_before, "Kaggle CUDA torch must be preserved."
    print("Offline runtime ready; compatible packages and CUDA torch preserved.", flush=True)
else:
    print("Local patent run: install requirements.txt and set PATENT_* paths first.")
