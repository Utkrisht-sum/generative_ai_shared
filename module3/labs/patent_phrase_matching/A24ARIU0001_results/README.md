# Patent project evidence — A24ARIU0001

I completed the offline experiments, final training run and one Kaggle late
submission on 9 November 2026. The four-page report remains a **draft** until I
add the required Submissions-tab screenshot. The course-platform upload is also
pending.

| Evidence | Saved Kaggle version |
| --- | --- |
| Offline weights and 53 dependency wheels | https://www.kaggle.com/code/utkrishtsuman/a24ariu0001-patent-offline-weights?scriptVersionId=367823110 |
| Baseline, MiniLM and two context comparisons | https://www.kaggle.com/code/utkrishtsuman/a24ariu0001-patent-experiments?scriptVersionId=367832537 |
| Final notebook used for submission | https://www.kaggle.com/code/utkrishtsuman/a24ariu0001-patent-final?scriptVersionId=367835971 |

These executed versions are public. Later quick saves changed visibility and
added written analysis; they did not start new jobs or competition entries.
`notebook_visibility.json` records those saves. Use final **version 1** for the
scored notebook link. The three executed notebooks beside this folder retain
their actual code cells, execution counts and outputs. Narrative cells and execution-status metadata were
updated after collection. Checkpoints and datasets stay out of this repository.

## Results

| Run | Validation Pearson | Training minutes | Peak allocated GB |
| --- | ---: | ---: | ---: |
| Section baseline | 0.820194 | 3.4274 | 2.7296 |
| Pretrained MiniLM, no task training | 0.581449 | 0 | — |
| No context | 0.816717 | 3.3270 | 2.6568 |
| Raw CPC code | 0.819209 | 3.3138 | 2.7083 |

All runs use the same 7,559 validation rows and held-out anchors. The two context
deltas are smaller than 0.005, so they do not establish a context winner. MiniLM
changes checkpoint, architecture and training regime together; the 0.238746
Pearson gap cannot be attributed to fine-tuning alone. Timings measure
`Trainer.train()`, including epoch evaluations, excluding checkpoint loading.
MiniLM's 2.948-second inference interval also excludes checkpoint loading.

The final run reproduces validation Pearson **0.820194478**. Kaggle submission
**58176236**, from final version 1, completed with public **0.7922** and private
**0.8084**. Public-minus-validation is −0.0280; private-minus-validation is
−0.0118. Anchor/section mix, partition size and selection on validation can
contribute to the differences. No leaderboard score selected a model. There was
one competition submission; the experiment baseline CSV was never submitted.

## Data and analysis

Only the original official competition files were used: 36,473 training rows,
733 anchors, and 36 visible test rows without labels. The seed-42 grouped split
has 28,914/7,559 rows and 586/147 anchors with zero anchor overlap. Later released
test labels and external prediction APIs were not used.

Section G has the lowest validation correlation (0.7062, n=1,040), followed by
C (0.7692, n=1,177). Five of the ten largest errors belong to G. The smallest
section, D (n=199), is not the lowest, so sample size alone does not explain this.
I grouped the ten reviewed errors into relation-sensitive lexical matches
(5), technical or part/whole relations (3), and missed functional paraphrases
(2). Four fragmentary pairs may need more expert context to interpret their
labels. The review describes the observed errors without claiming their cause
or assuming that a large error means the label is wrong.

Score compression is not uniform: mean prediction is 0.1195 for true zero,
0.6612 for true 0.75, and **1.0247** for true one. The last group overshoots.
Validation predictions are raw; only competition predictions are clipped.

## Files and verification

- `experiments.csv`, `best_config.json`: actual measurements and selection.
- `val_*.csv`, `val_predictions.csv`: paired experiment predictions; the latter
  is the selected experiment model used for error analysis.
- `final_val_predictions.csv`, `submission.csv`: final saved run outputs. The
  local submission file contains the 36 visible test rows; Kaggle reran the
  notebook against hidden test rows for its actual scores.
- `section_scores.csv`, `score_means.csv`, `score_compression.png`: raw validation
  analysis. `top_errors_for_review.csv` and `error_review.json` contain all ten
  reviewed pairs and their evidence.
- `kaggle_submission_status.json`, `submission_attempt.json`,
  `leaderboard_submissions.csv`: the accepted request and completed official API
  result. These are genuine API evidence, **not** a Submissions-tab screenshot.
- `run_summary.json`, `final_checks.json`: execution scope and output checks.
- `A24ARIU0001_PATENT_REPORT_UTKRISHT_SUMAN.DRAFT.pdf`: measured Tasks 1–5,
  references and the explicit missing-screenshot notice, within four pages.

Run `python verify_results.py` with NumPy and pandas to independently recompute
the paired scores, section/score tables, largest-error IDs and ledger agreement.

To finish the screenshot deliverable, sign in to Kaggle and open
https://www.kaggle.com/competitions/us-patent-phrase-to-phrase-matching/submissions.
Capture submission 58176236 with both scores, place the genuine image here and
record its relative path in `leaderboard_submissions.csv`. Then run:

```bash
python run_preparation/A24ARIU0001/tools/patent_report.py \
  module3/labs/patent_phrase_matching/A24ARIU0001_results
```

The default command still rejects a missing screenshot. The explicit
`--draft-without-screenshot` option creates only a marked `.DRAFT.pdf`; it does
not declare the project complete. On 11 November, the shared cloud browser
exposed Chrome with no tabs; the requested signed-in Brave session was not
connected. The saved-results verifier passed, and all four existing draft PDF
pages were rendered and inspected. The course brief still specifies the course
platform without an assignment URL; repository and public searches did not
establish the actual upload destination. The screenshot, final PDF and course
upload remain pending.

## Reproduction note

The first experiment attempt stopped during offline setup before training. It
tried to copy CPU-image transitive pins and requested a restart for unrelated
loaded scientific modules. The corrected bootstrap resolves required packages
from attached wheels, preserves compatible dependencies and working CUDA torch,
and checks actual imported distribution files before replacement. Experiment
version 2 passed setup and completed all 15 code cells; final version 1 completed
all 11. Python was 3.13.16, torch 2.11.0+cu130 and Transformers 5.22.2. The
failed setup is not a model experiment or competition entry.
