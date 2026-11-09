# Remaining labs — A24ARIU0001

This folder holds the runnable continuation files. It is preparation for the
remaining experiments, not a claim that they have run or been submitted.
The notebooks are adapted from the course material and the continuation package
provided by Utkrisht Suman. Dataset, model and paper references are retained in
the notebooks. Existing lab submissions are kept in their original directories.

## Current status

Checked on 10 November 2026 (India).

| Work | Verified state | Still needed |
| --- | --- | --- |
| Labs 1–5 | Submission notebooks exist in the fork | Check the course platform for acceptance; a fork file alone is not submission evidence |
| GPT-2 recipes | Fork PR #1 is merged; executed notebook and measured evidence are present | No rerun needed |
| Gradio chatbot | Fork PR #2 is a draft with recorded automated outputs | A real partner session, chat log, observations and ratings |
| QLoRA DialogSum | Implementation prepared; the optimizer-check bug is fixed | T4 training, generated summaries, ROUGE and six human ratings |
| Optional U-Net | Real-data implementation prepared | Ten epochs on Oxford-IIIT Pet, held-out Dice/IoU, plots and failure analysis |
| Patent project | Weight preparation completed; official competition inputs verified | Experiment/final runs, reviewed errors, actual Kaggle scores and the report |

The course repository's current master does not contain the fork's A24ARIU0001
submission files. GPT-2's fork merge does not establish course acceptance.

## Run order

Use one job at a time. Preserve the supplied seeds, training limits, batch sizes,
lengths and epoch budgets. The preparation branch does not change those settings.

| Notebook topic | Runtime | Internet | Inputs |
| --- | --- | --- | --- |
| QLORA_DIALOGSUM | Kaggle T4 | On | None |
| UNET_PET_SEGMENTATION | Kaggle GPU | On for download | Original Oxford pet images and trimaps if downloading fails |
| PATENT_DOWNLOAD_WEIGHTS | Kaggle CPU | On | None |
| PATENT_EXPERIMENTS | Kaggle T4 | Off | Official competition data and the whole saved weight/wheel output |
| PATENT_FINAL | Kaggle T4 | Off | Official competition data, weight/wheel output and experiment output containing best_config.json |

Save each notebook with its actual outputs, and download it separately from its
small result ZIP. Model weights, datasets and environments are not needed for
the first result review. The patent final notebook must run offline; its selected
context comes from grouped validation, not from leaderboard scores.

### QLoRA correction

Transformers converts `optim="paged_adamw_8bit"` into an enum. Its string
representation is `OptimizerNames.PAGED_ADAMW_8BIT`, so the original check for
lowercase `"paged"` fails with correct settings. The corrected cell compares
`args.optim.value` with `"paged_adamw_8bit"` and prints the precision and optimizer
settings. It still rejects incorrect precision, optimizer and batch settings.

### Genuine human observations

After QLoRA, run `python tools/rate_summaries.py <extracted-result-folder>` to
record the six blinded ratings. Gradio's partner session remains on the existing
draft PR: https://github.com/Utkrisht-sum/generative_ai_shared/pull/2.
Blank rating files are pending work; automated judgments do not replace them.

### Patent submission

Use only the official competition train/test files. Do not use the later fully
rated dataset, which contains hidden test labels. Record every real submission
and keep the scores and screenshots. The course brief requires the final PDF
(at most four pages), Kaggle version link and leaderboard screenshot on the
course platform. A GitHub branch does not replace those deliverables.

`tools/patent_report.py` builds the report from real results and reviewed errors.
It deliberately refuses missing leaderboard evidence. Do not fill result tables
with fixture values or estimated scores.

## Local checks and access

All seven notebooks in the original continuation package passed format validation
and their 116 code cells compiled. The QLoRA check was tested with the specified
Transformers version: the original failed, the corrected version accepted the
intended configuration, and six incorrect configurations were rejected. These
are implementation checks, not experiment measurements.

The preparation machine has zero CUDA devices. After the access settings were
published, both GitHub API and Kaggle authentication succeeded. Kaggle reported
about 28.3 of 30 GPU hours remaining. The corrected private QLoRA T4 run is now
executing, and the patent CPU weight-preparation run completed. The latter's
executed notebook and data audit are saved in the patent topic directory. No GPU
training result is claimed until the corresponding run completes and is checked.

The preparation now has draft PR #3 in the fork. The course repository also has
open PR #127 for the Lab 1/Lab 5 corrections and PR #160 for the completed GPT-2
lab. These open pull requests have not been merged.

Nothing in this folder submits a competition entry or merges a pull request
automatically. Submission should use completed, verified artifacts.
