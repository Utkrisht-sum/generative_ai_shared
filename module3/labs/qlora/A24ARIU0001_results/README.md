# QLoRA DialogSum results — A24ARIU0001

I trained and evaluated the model on one Kaggle T4:
https://www.kaggle.com/code/utkrishtsuman/a24ariu0001-qlora-dialogsum/1.
All 28 nonempty code cells completed without recorded errors. The notebook keeps
the saved outputs, with written answers explaining the results.

| Measure | Base | QLoRA |
| --- | ---: | ---: |
| ROUGE-1 | 32.05 | 45.52 |
| ROUGE-2 | 8.39 | 18.57 |
| ROUGE-L | 23.00 | 37.11 |
| Mean words | 33.32 | 21.30 |

The comparison uses the same 60 validation dialogues. QLoRA has strictly higher
ROUGE-L on 54 of them. Training used the prescribed 1,940 retained examples,
122 optimizer steps, effective batch 16 and one epoch. It took 14.43 minutes and
peaked at 6.37 GB of allocated GPU memory. The adapter file is about 73.9 MB and
is retained in the Kaggle output rather than Git.

`verify_metrics.py` recomputes ROUGE from `summary_predictions.csv` with
rouge_score 0.1.2 and checks it against the recorded JSON. A separate paired
percentile bootstrap (10,000 resamples, seed 42) gives a 95% interval of
10.62–17.97 ROUGE-L points for the mean gain. This interval describes sampling
the fixed predictions, not variation from retraining the model.

The examples still contain factual errors. In non-blind example 5, both models
reverse which person works at the supermarket and which does yard work. The tuned
summary also omits the recovery of Rusty in example 3. These are qualitative
observations from the saved dialogues and predictions, not human-rating scores.

The six rows in `blind_ratings.csv` still need a human's faithfulness and coverage
scores, with a note for each example. Until those ratings are collected, the human
comparison is incomplete. The provided rating tool uses the saved predictions,
so this step does not require training again.
