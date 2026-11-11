# Generative AI lab submissions — Utkrisht Suman

Roll number: **A24ARIU0001**

This index links to my latest notebooks and results on the fork's `master`
branch. I reviewed the written explanations on 11 November 2026 and kept the
code, saved outputs and experiment settings unchanged. The
[audit](LAB_SUBMISSION_AUDIT_UTKRISHT.md) and
[file manifest](LAB_SUBMISSION_MANIFEST_UTKRISHT.json) record the checks.

Seven lab topics have completed notebooks. QLoRA still needs human ratings,
Gradio needs a partner session, and the patent project needs its screenshot and
course-platform upload. The table distinguishes those remaining requirements
from completed training. The original course files and other students' work
are preserved.

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

The patent project also includes the [offline-input notebook](module3/labs/patent_phrase_matching/A24ARIU0001_PATENT_DOWNLOAD_WEIGHTS_LAB_UTKRISHT_SUMAN.ipynb)
and [experiment notebook](module3/labs/patent_phrase_matching/A24ARIU0001_PATENT_EXPERIMENTS_LAB_UTKRISHT_SUMAN.ipynb).
Submission **58176236** used [final version 1](https://www.kaggle.com/code/utkrishtsuman/a24ariu0001-patent-final?scriptVersionId=367835971):
validation Pearson **0.820194478**, public **0.7922**, private **0.8084**.
The four-page report is still labelled draft because its required Submissions-tab
screenshot is missing.

The patent brief asks for a PDF of at most four pages, the scored Kaggle version
link and a genuine leaderboard screenshot on the course platform. It provides
no assignment URL, and the repository and syllabus did not identify one. Course
delivery therefore remains unverified.

Course PRs [#127](https://github.com/bk-anupam/generative_ai_shared/pull/127) and
[#160](https://github.com/bk-anupam/generative_ai_shared/pull/160) were closed
without merging on 11 November. The separate
[VAE/GAN/attention/U-Net branch](https://github.com/bk-anupam/generative_ai_shared/compare/master...Utkrisht-sum:generative_ai_shared:a24ariu0001-completed-lab-submissions?expand=1)
is ready, but course PR creation is blocked by the integration's permissions.
[Draft fork PR #3](https://github.com/Utkrisht-sum/generative_ai_shared/pull/3)
retains preparation material. Neither fork storage nor a draft PR confirms
course acceptance.

## Reproduce

For the earlier labs, install `lab_requirements_UTKRISHT.txt` in a Python 3 environment and run the cells in order. Those recorded CPU runs used Python 3.12, PyTorch 2.15.0 and torchvision 0.29.2. The newer Kaggle U-Net and QLoRA runs used Python 3.13.16 and T4. Follow the Module 3 notebooks' setup cells for their additional dependencies, preserving Kaggle's CUDA torch. Seeds and runtime details are recorded with each run; CPU and GPU results can differ numerically.

- **VAE data:** The recorded run uses the LFW **funneled** release from the scikit-learn-maintained [Figshare mirror](https://ndownloader.figshare.com/files/5976015), because the original deep-funneled endpoint was unavailable. This alignment variant differs from the scaffold's default deep-funneled release. The remaining preprocessing is unchanged: central crop, RGB 45×45 pixels, identities with fewer than 25 photos, seeded 80/20 image split. Set `LFW_DATASET_PATH` to the extracted `lfw_funneled` directory, or attach LFW on Kaggle. Do not compare results across alignment variants as if the input data were identical. Archive SHA-256: `b47c8422c8cded889dc5a13418c4bc2abbda121092b3533a83306f90d900100a`.
- **GAN data:** MNIST is downloaded on the first run. For offline execution, set `OFFLINE_MNIST_DIR` to a directory containing the four original IDX files. Set `TRAIN_LIMIT=None` for the full training split; keeping 5,000 records the executed limited-data configuration.
- **Translation data:** Download `bentrevett/multi30k` with Hugging Face datasets. Vocabulary is fitted on training pairs only. Set `MAX_TRAIN_PAIRS=12000` to restore the scaffold's original training budget or `None` for the complete train split. The notebook prints actual split sizes and model parameter counts. BLEU uses generated translations; perplexity uses reference-token evaluation.
- **Optional U-Net data:** The completed Kaggle run downloaded the original Oxford-IIIT Pet images and trimaps through torchvision. It used `SMOKE_TEST=False`, `DOWNLOAD=True`, 128×128 images, batch 16 and ten epochs. The seed-42 split was 5,912/739/739 images. Checkpoint selection used validation Dice; epoch 10 was selected before the held-out test evaluation. The notebook and [results](module1/labs/submissions/optional/A24ARIU0001_UNET_results/README.md) contain the actual plots and two displayed failure cases.

Outputs are embedded in the executed notebooks. Downloaded data and model checkpoints are excluded from version control. Model quality conclusions apply only to the displayed run and budget; these educational experiments do not establish production performance.
