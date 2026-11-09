"""Recompute the recorded ROUGE metrics and a paired sampling interval."""
import csv
import json
from pathlib import Path

import numpy as np
from rouge_score import rouge_scorer

root = Path(__file__).resolve().parent
with (root / "summary_predictions.csv").open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
reported = json.loads((root / "run_summary.json").read_text())
assert len(rows) == 60
keys = ["rouge1", "rouge2", "rougeL"]
scorer = rouge_scorer.RougeScorer(keys, use_stemmer=True)
scores = {name: {key: [] for key in keys} for name in ["base", "QLoRA"]}
for row in rows:
    for name in scores:
        measured = scorer.score(row["reference"], row[name])
        for key in keys:
            scores[name][key].append(measured[key].fmeasure * 100)
metrics = {name: {key: float(np.mean(values)) for key, values in model.items()}
           for name, model in scores.items()}
for name, report_key in [("base", "base_rouge"), ("QLoRA", "tuned_rouge")]:
    for key, value in metrics[name].items():
        assert abs(value - reported[report_key][key]) < 1e-10
delta = np.array(scores["QLoRA"]["rougeL"]) - np.array(scores["base"]["rougeL"])
assert int(np.sum(delta > 0)) == reported["strict_rougeL_wins"]
rng = np.random.default_rng(42)
sample_means = delta[rng.integers(0, len(rows), size=(10000, len(rows)))].mean(axis=1)
print(json.dumps({
    "metrics": metrics,
    "strict_rougeL_wins": int(np.sum(delta > 0)),
    "mean_words": {name: float(np.mean([len(row[name].split()) for row in rows]))
                   for name in ["reference", "base", "QLoRA"]},
    "mean_rougeL_gain_points": float(delta.mean()),
    "paired_percentile_interval_95": np.quantile(sample_means, [.025, .975]).tolist(),
    "bootstrap_replicates": 10000,
    "bootstrap_seed": 42,
    "scope": "Fixed predictions from one training seed, not training-seed variation"
}, indent=2))
