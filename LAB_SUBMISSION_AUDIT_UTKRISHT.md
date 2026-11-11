# Submission names and locations — Utkrisht Suman

Checked **10 November 2026 (India)**. All **12 submission notebooks** are uploaded
in the fork's review branch, with matching remote file hashes. They represent ten
lab topics; the patent project has separate weight, experiment and final files.

Submission states were checked again on **11 November 2026 (India)**. All twelve
local notebook SHA-256 hashes still match the original manifest. Saved model
outputs and the blank human-evaluation files are unchanged.

The filename convention is:

```text
A24ARIU0001_<LAB_TOPIC>_LAB_UTKRISHT_SUMAN.ipynb
```

All twelve already followed this convention, so no notebook rename was needed.
Each contains the matching student name and roll number. The course briefs do
not state a stricter repository-wide filename rule. Modules 1–2 retain the
existing student-submission layout; Module 3 uses each lab's topic directory.
Supporting CSVs/figures stay in the corresponding `A24ARIU0001_results` folder
(U-Net uses `A24ARIU0001_UNET_results`). Kaggle's required `submission.csv` name
is preserved.

| Lab | Uploaded notebook | Course submission state |
| --- | --- | --- |
| Lab 1 | [Encoder–decoder](module1/labs/submissions/lab1/A24ARIU0001_ENCODER_DECODER_LAB_UTKRISHT_SUMAN.ipynb) | Course PR #127 closed, unmerged |
| Lab 2 | [Face VAE](module1/labs/submissions/lab2/A24ARIU0001_VAE_FACES_LAB_UTKRISHT_SUMAN.ipynb) | Fork uploaded; clean course branch ready |
| Lab 3 | [GAN](module1/labs/submissions/lab3/A24ARIU0001_GAN_LAB_UTKRISHT_SUMAN.ipynb) | Fork uploaded; clean course branch ready |
| Lab 4 | [Seq2Seq attention](module2/labs/submissions/seq2seq_attention/A24ARIU0001_SEQ2SEQ_ATTENTION_LAB_UTKRISHT_SUMAN.ipynb) | Fork uploaded; clean course branch ready |
| Lab 5 | [Text to BERT](module2/labs/submissions/lab5/A24ARIU0001_TEXT_TO_BERT_LAB_UTKRISHT_SUMAN.ipynb) | Course PR #127 closed, unmerged |
| Optional U-Net | [Pet segmentation](module1/labs/submissions/optional/A24ARIU0001_UNET_PET_SEGMENTATION_LAB_UTKRISHT_SUMAN.ipynb) | Public Kaggle notebook; clean course branch ready |
| GPT-2 | [Recipe fine-tuning](module3/labs/gpt2_lora_recipes/A24ARIU0001_GPT2_LORA_RECIPES_LAB_UTKRISHT_SUMAN.ipynb) | Course PR #160 closed, unmerged |
| Gradio | [Chatbot](module3/labs/gradio_chatbot/A24ARIU0001_GRADIO_CHATBOT_LAB_UTKRISHT_SUMAN.ipynb) | Automated outputs uploaded; partner session pending in draft PR #2 |
| QLoRA | [DialogSum](module3/labs/qlora/A24ARIU0001_QLORA_DIALOGSUM_LAB_UTKRISHT_SUMAN.ipynb) | Training/automatic evaluation uploaded; six human ratings pending |
| Patent preparation | [Offline weights](module3/labs/patent_phrase_matching/A24ARIU0001_PATENT_DOWNLOAD_WEIGHTS_LAB_UTKRISHT_SUMAN.ipynb) | Input preparation, not a separate final deliverable |
| Patent experiments | [Controlled experiments](module3/labs/patent_phrase_matching/A24ARIU0001_PATENT_EXPERIMENTS_LAB_UTKRISHT_SUMAN.ipynb) | Public Kaggle experiment evidence |
| Patent final | [Offline final](module3/labs/patent_phrase_matching/A24ARIU0001_PATENT_FINAL_LAB_UTKRISHT_SUMAN.ipynb) | Kaggle entry complete; screenshot/course upload pending |

The [machine-readable manifest](LAB_SUBMISSION_MANIFEST_UTKRISHT.json) lists every
exact filename, path, content hash and pinned GitHub URL. It verifies remote commit
`9ee89ddfd118665988862c24eaa726763dbaa7e9` on
`a24ariu0001-remaining-labs-preparation`. The default-branch index links to these
reviewed copies rather than older files. Preparation templates under
`run_preparation/` are not the executed submissions.

## Fixes made

- Corrected five broken course-reference links across Lab 1, Lab 5, GPT-2 and
  QLoRA. Executable code, recorded outputs and execution counts are unchanged.
- Replaced the old Lab 1 dashboard link with the current corrected notebook.
- Included the eight existing Gradio notebook/evidence files in the common
  review branch, byte-for-byte from draft PR #2. Its human-study fields remain
  blank; this consolidation does not claim that the partner study is complete.
- Made the completed U-Net saved version public and checked its exact
  [Kaggle version link](https://www.kaggle.com/code/utkrishtsuman/a24ariu0001-unet-pet-segmentation?scriptVersionId=367827217)
  without authentication. A visibility quick save did not rerun training.
- Updated the existing Lab 1/Lab 5 and GPT-2 PR branches with the reference fixes,
  without creating duplicate course PRs.

All notebooks pass format validation. Their 197 nonempty code cells have saved
execution counts and no recorded error output. This is inspection of saved
evidence, not a new training run or proof of human evaluation/course acceptance.

## Required destinations and remaining access

The [patent brief](module3/labs/patent_phrase_matching/project_brief.md) requires
the **course platform** to receive a PDF of at most four pages, the scored Kaggle
version link and a genuine Submissions-tab screenshot. Its
[scored notebook](https://www.kaggle.com/code/utkrishtsuman/a24ariu0001-patent-final?scriptVersionId=367835971)
is public and submission 58176236 completed (public 0.7922, private 0.8084).
The report remains marked draft until its required screenshot is added. GitHub
storage does not replace that course-platform upload.

The [optional U-Net brief](module1/labs/optional/optional_unet_pet_segmentation.md)
asks for a Kaggle notebook; its completed public version is linked above.

Course PRs [#127](https://github.com/bk-anupam/generative_ai_shared/pull/127)
and [#160](https://github.com/bk-anupam/generative_ai_shared/pull/160) were closed
by `bk-anupam` on 11 November, at 13:34:55 and 13:35:30 India time respectively.
Neither was merged; no explanatory comment was provided. Neither was duplicated
or reopened. A new course PR attempt for the clean completed-labs branch again
failed with `Resource not accessible by integration (createPullRequest)`.
The [clean VAE/GAN/attention/U-Net branch](https://github.com/bk-anupam/generative_ai_shared/compare/master...Utkrisht-sum:generative_ai_shared:a24ariu0001-completed-lab-submissions?expand=1)
is uploaded and ready for the owner to open its PR. All four notebooks on that
branch pass format validation and contain 44 saved code-cell execution counts
with no recorded errors; their bytes match the audited review copies.

The course repository at `8c8e8595ef51867ef4be168de336bf98a5c8b57c` still specifies
the course platform for patent delivery but provides no assignment URL. Its
briefs, notebook submission sections, syllabus document and a public search did
not establish the actual upload destination. The shared cloud browser inventory
contains only Chrome with no tabs; the requested signed-in Brave session is not
connected. The screenshot, final PDF and course receipt remain pending.

The saved patent verifier passed on 11 November. All four existing draft PDF
pages were rendered and inspected, and the default report command still rejects
the missing screenshot. No course upload or acceptance is claimed.
