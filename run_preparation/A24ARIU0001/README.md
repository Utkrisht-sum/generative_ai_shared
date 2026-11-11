# Remaining labs — A24ARIU0001

This folder holds the runnable continuation sources and helper tools. Completed
notebooks with genuine outputs now live in their topic submission directories;
the source copies here remain rerun templates.
The notebooks are adapted from the course material and the continuation package
provided by Utkrisht Suman. Dataset, model and paper references are retained in
the notebooks. Existing lab submissions are kept in their original directories.

## Current status

Submission status checked on 11 November 2026 (India).

| Work | Verified state | Still needed |
| --- | --- | --- |
| Labs 1–5 | Submission notebooks exist in the fork | Check the course platform for acceptance; a fork file alone is not submission evidence |
| GPT-2 recipes | Fork PR #1 is merged; executed notebook and measured evidence are present | No rerun needed |
| Gradio chatbot | Fork PR #2 is a draft with recorded automated outputs | A real partner session, chat log, observations and ratings |
| QLoRA DialogSum | T4 training and automatic evaluation completed; ROUGE-L 23.00 → 37.11 | Six genuine human ratings |
| Optional U-Net | Completed ten-epoch pet run; test Dice 0.8793, IoU 0.7846 | Course pull-request creation is blocked by integration permissions |
| Patent project | Four comparisons, error review and offline final completed; Kaggle public/private 0.7922/0.8084 | Submissions-tab screenshot and course-platform upload; four-page draft report is ready |

The course repository's current master does not contain the fork's A24ARIU0001
submission files. GPT-2's fork merge does not establish course acceptance.

## Run order

Keep GPU training jobs sequential; independent CPU weight preparation can run
alongside them. Preserve the supplied seeds, training limits, batch sizes, lengths
and epoch budgets. The preparation branch does not change those settings.

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
Its default final-report mode refuses a missing Submissions-tab screenshot. An
explicit `--draft-without-screenshot` option produces a marked `.DRAFT.pdf` only.
The completed official API result, submission ledger and reviewed evidence are in
`module3/labs/patent_phrase_matching/A24ARIU0001_results`.

## Local checks and access

All seven notebooks in the original continuation package passed format validation
and their 116 code cells compiled. The QLoRA check was tested with the specified
Transformers version: the original failed, the corrected version accepted the
intended configuration, and six incorrect configurations were rejected. These
are implementation checks, not experiment measurements.

The preparation machine has zero CUDA devices. After the access settings were
published, both GitHub API and Kaggle authentication succeeded. Kaggle reported
about 28.3 of 30 GPU hours remaining at the start. QLoRA and U-Net finished and
their actual outputs are saved in their topic directories. Patent experiment
version 2 and final version 1 also completed after a setup correction. The initial bootstrap tried
to copy every CPU-image dependency version into the GPU runtime and demanded a
restart even when only an unrelated package was loaded. The revised bootstrap
keeps compatible installed dependencies, resolves the required packages from the
attached wheels, pins working CUDA torch and checks the files of any distribution
that would be replaced before continuing. Only bootstrap cells changed; training
and evaluation controls were preserved.

The continuation results are in draft PR #3 in the fork. Course PR #127 for the
Lab 1/Lab 5 corrections and PR #160 for GPT-2 were closed by the maintainer on
11 November without merging or an explanatory comment. No duplicate was opened.

The completed U-Net has a separate clean branch based on the course master:
`a24ariu0001-unet-pet-completed`. Creating its course PR returned
`Resource not accessible by integration`. The prepared comparison is
https://github.com/bk-anupam/generative_ai_shared/compare/master...Utkrisht-sum:generative_ai_shared:a24ariu0001-unet-pet-completed?expand=1.
That branch is ready for a PR; it is not evidence that a PR was created.
The combined `a24ariu0001-completed-lab-submissions` branch also includes VAE,
GAN and attention. Its course PR attempt on 11 November returned the same
integration-permission error.

The authorized Kaggle late submission (58176236) used final notebook version 1
and completed successfully. The scored version and its inputs are public for
instructor access; later visibility quick saves did not run new jobs or entries.
No course-platform upload or course PR merge has been performed.
