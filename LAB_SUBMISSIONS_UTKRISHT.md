# Generative AI lab submissions — Utkrisht Suman

Roll number: **A24ARIU0001**

**Names and upload locations checked on 10 November 2026 (India):** all 12
submission notebooks use `A24ARIU0001_<LAB_TOPIC>_LAB_UTKRISHT_SUMAN.ipynb`.
See the [naming/location audit](LAB_SUBMISSION_AUDIT_UTKRISHT.md) and
[exact-file manifest](LAB_SUBMISSION_MANIFEST_UTKRISHT.json). All are available
in their topic directories; draft and course-acceptance states are listed below.

The fork's default branch contains the latest submission notebooks and their
supporting results. Preparation templates remain on
`a24ariu0001-remaining-labs-preparation`. QLoRA, Gradio and the patent package
retain the pending items listed below.

**Submission status checked on 11 November 2026 (India):** course PRs #127 and
#160 are now closed and unmerged. The maintainer closed them today without an
explanatory comment. No duplicate or replacement PR was created.

**The earlier submissions were reviewed before publication to this fork.** New execution results below state their current completion status.

The original course templates and other students' files are preserved. These notebooks are separate student submissions.

| Lab | Notebook | Execution scope |
|---|---|---|
| Lab 1: Encoder–decoder | [Notebook](module1/labs/submissions/lab1/A24ARIU0001_ENCODER_DECODER_LAB_UTKRISHT_SUMAN.ipynb) | Executed corrections; course PR #127 closed, unmerged |
| Lab 2: Face VAE | [Notebook](module1/labs/submissions/lab2/A24ARIU0001_VAE_FACES_LAB_UTKRISHT_SUMAN.ipynb) | LFW faces; 10-epoch main run and fresh beta=0/1 comparisons |
| Lab 3: GAN | [Notebook](module1/labs/submissions/lab3/A24ARIU0001_GAN_LAB_UTKRISHT_SUMAN.ipynb) | Fixed 5,000-image MNIST subset; 10 epochs each for baseline, faster D, conditional DCGAN |
| Seq2Seq attention | [Notebook](module2/labs/submissions/seq2seq_attention/A24ARIU0001_SEQ2SEQ_ATTENTION_LAB_UTKRISHT_SUMAN.ipynb) | CPU-limited Multi30k: 3,000 train pairs; up to 8 epochs/model; 200 test pairs |
| Lab 5: Text to BERT | [Notebook](module2/labs/submissions/lab5/A24ARIU0001_TEXT_TO_BERT_LAB_UTKRISHT_SUMAN.ipynb) | Executed notebook; course PR #127 closed, unmerged |
| Optional U-Net | [Notebook](module1/labs/submissions/optional/A24ARIU0001_UNET_PET_SEGMENTATION_LAB_UTKRISHT_SUMAN.ipynb) | Completed ten-epoch Oxford pet run; test Dice 0.8793 and IoU 0.7846 on 739 held-out images |

## Module 3 continuation

| Work | Evidence | Status |
| --- | --- | --- |
| GPT-2 recipes | [Notebook](module3/labs/gpt2_lora_recipes/A24ARIU0001_GPT2_LORA_RECIPES_LAB_UTKRISHT_SUMAN.ipynb) | Complete; course PR #160 closed, unmerged |
| QLoRA DialogSum | [Notebook](module3/labs/qlora/A24ARIU0001_QLORA_DIALOGSUM_LAB_UTKRISHT_SUMAN.ipynb) | Training and automatic evaluation complete; six human ratings still pending |
| Gradio chatbot | [Notebook](module3/labs/gradio_chatbot/A24ARIU0001_GRADIO_CHATBOT_LAB_UTKRISHT_SUMAN.ipynb) · [draft fork PR #2](https://github.com/Utkrisht-sum/generative_ai_shared/pull/2) | Recorded automated run; real partner session still pending |
| Patent project | [Final executed notebook](module3/labs/patent_phrase_matching/A24ARIU0001_PATENT_FINAL_LAB_UTKRISHT_SUMAN.ipynb) · [results/report](module3/labs/patent_phrase_matching/A24ARIU0001_results/README.md) | Offline experiments and Kaggle submission complete: public 0.7922, private 0.8084; required screenshot and course upload pending |

The patent entry is Kaggle submission **58176236**, using public notebook
[final version 1](https://www.kaggle.com/code/utkrishtsuman/a24ariu0001-patent-final?scriptVersionId=367835971).
Its validation Pearson is 0.8202. The four-page report is explicitly marked draft
until the required Submissions-tab screenshot is added. Actual API scores are
saved; they do not replace that screenshot.

Creating a new pull request in the course repository returned **Resource not
accessible by integration**. The completed U-Net branch is pushed and ready at
[this comparison](https://github.com/bk-anupam/generative_ai_shared/compare/master...Utkrisht-sum:generative_ai_shared:a24ariu0001-unet-pet-completed?expand=1).
It has no new course PR. Fork [draft PR #3](https://github.com/Utkrisht-sum/generative_ai_shared/pull/3)
collects the verified continuation work; a fork PR is not course acceptance.
Course PRs [#127](https://github.com/bk-anupam/generative_ai_shared/pull/127) and
[#160](https://github.com/bk-anupam/generative_ai_shared/pull/160) closed on
11 November 2026 without merging. They have not been reopened or duplicated.

The existing VAE, GAN and attention notebooks plus the completed U-Net are also
packaged on a clean branch based on the course master, with only this student's
12 submission/dependency files:
[completed-labs comparison](https://github.com/bk-anupam/generative_ai_shared/compare/master...Utkrisht-sum:generative_ai_shared:a24ariu0001-completed-lab-submissions?expand=1).
This is ready for course PR creation. An attempt on 11 November again returned
`Resource not accessible by integration (createPullRequest)`, so no course PR
exists for that branch. The earlier three notebooks were inspected, not retrained.

The current course brief requires the patent PDF, scored notebook link and
genuine screenshot on the **course platform**, but gives no assignment URL.
Repository files, the syllabus and a public search did not identify that URL.
Course delivery remains unverified. The requested signed-in Brave session is
not connected to this cloud chat; the report's screenshot check remains intact.

## Reproduce

For the earlier labs, install `lab_requirements_UTKRISHT.txt` in a Python 3 environment and run the cells in order. Those recorded CPU runs used Python 3.12, PyTorch 2.15.0 and torchvision 0.29.2. The newer Kaggle U-Net and QLoRA runs used Python 3.13.16 and T4. Follow the Module 3 notebooks' setup cells for their additional dependencies, preserving Kaggle's CUDA torch. Seeds and runtime details are recorded with each run; CPU and GPU results can differ numerically.

- **VAE data:** The recorded run uses the LFW **funneled** release from the scikit-learn-maintained [Figshare mirror](https://ndownloader.figshare.com/files/5976015), because the original deep-funneled endpoint was unavailable. This alignment variant differs from the scaffold's default deep-funneled release. The remaining preprocessing is unchanged: central crop, RGB 45×45 pixels, identities with fewer than 25 photos, seeded 80/20 image split. Set `LFW_DATASET_PATH` to the extracted `lfw_funneled` directory, or attach LFW on Kaggle. Do not compare results across alignment variants as if the input data were identical. Archive SHA-256: `b47c8422c8cded889dc5a13418c4bc2abbda121092b3533a83306f90d900100a`.
- **GAN data:** MNIST is downloaded on the first run. For offline execution, set `OFFLINE_MNIST_DIR` to a directory containing the four original IDX files. Set `TRAIN_LIMIT=None` for the full training split; keeping 5,000 records the executed limited-data configuration.
- **Translation data:** Download `bentrevett/multi30k` with Hugging Face datasets. Vocabulary is fitted on training pairs only. Set `MAX_TRAIN_PAIRS=12000` to restore the scaffold's original training budget or `None` for the complete train split. The notebook prints actual split sizes and model parameter counts. BLEU uses generated translations; perplexity uses reference-token evaluation.
- **Optional U-Net data:** The completed Kaggle run downloaded the original Oxford-IIIT Pet images and trimaps through torchvision. It used `SMOKE_TEST=False`, `DOWNLOAD=True`, 128×128 images, batch 16 and ten epochs. The seed-42 split was 5,912/739/739 images. Checkpoint selection used validation Dice; epoch 10 was selected before the held-out test evaluation. The notebook and [results](module1/labs/submissions/optional/A24ARIU0001_UNET_results/README.md) contain the actual plots and two displayed failure cases.

Outputs are embedded in the executed notebooks. Downloaded data and model checkpoints are excluded from version control. Model quality conclusions apply only to the displayed run and budget; these educational experiments do not establish production performance.
