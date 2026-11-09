# Generative AI lab submissions — Utkrisht Suman

Roll number: **A24ARIU0001**

**The earlier submissions were reviewed before publication to this fork.** New execution results below state their current completion status.

The original course templates and other students' files are preserved. These notebooks are separate student submissions.

| Lab | Notebook | Execution scope |
|---|---|---|
| Lab 1: Encoder–decoder | [Existing submission on lab1 branch](https://github.com/Utkrisht-sum/generative_ai_shared/blob/lab1/module1/labs/submissions/lab1/A24ARIU0001_ENCODER_DECODER_LAB_UTKRISHT_SUMAN.ipynb) | Already submitted; untouched |
| Lab 2: Face VAE | [Notebook](module1/labs/submissions/lab2/A24ARIU0001_VAE_FACES_LAB_UTKRISHT_SUMAN.ipynb) | LFW faces; 10-epoch main run and fresh beta=0/1 comparisons |
| Lab 3: GAN | [Notebook](module1/labs/submissions/lab3/A24ARIU0001_GAN_LAB_UTKRISHT_SUMAN.ipynb) | Fixed 5,000-image MNIST subset; 10 epochs each for baseline, faster D, conditional DCGAN |
| Seq2Seq attention | [Notebook](module2/labs/submissions/seq2seq_attention/A24ARIU0001_SEQ2SEQ_ATTENTION_LAB_UTKRISHT_SUMAN.ipynb) | CPU-limited Multi30k: 3,000 train pairs; up to 8 epochs/model; 200 test pairs |
| Lab 5: Text to BERT | [Notebook](module2/labs/submissions/lab5/A24ARIU0001_TEXT_TO_BERT_LAB_UTKRISHT_SUMAN.ipynb) | Executed notebook; included in the open Lab 1/Lab 5 corrections PR |
| Optional U-Net | [Notebook](module1/labs/submissions/optional/A24ARIU0001_UNET_PET_SEGMENTATION_LAB_UTKRISHT_SUMAN.ipynb) | Completed ten-epoch Oxford pet run; test Dice 0.8793 and IoU 0.7846 on 739 held-out images |

## Module 3 continuation

| Work | Evidence | Status |
| --- | --- | --- |
| GPT-2 recipes | [Notebook](module3/labs/gpt2_lora_recipes/A24ARIU0001_GPT2_LORA_RECIPES_LAB_UTKRISHT_SUMAN.ipynb) | Complete; course-repository PR #160 is open |
| QLoRA DialogSum | [Notebook](module3/labs/qlora/A24ARIU0001_QLORA_DIALOGSUM_LAB_UTKRISHT_SUMAN.ipynb) | Training and automatic evaluation complete; six human ratings still pending |
| Gradio chatbot | [Draft fork PR #2](https://github.com/Utkrisht-sum/generative_ai_shared/pull/2) | Recorded automated run; real partner session still pending |
| Patent project | [Weight preparation](module3/labs/patent_phrase_matching/A24ARIU0001_PATENT_DOWNLOAD_WEIGHTS_LAB_UTKRISHT_SUMAN.ipynb) | Weights/wheels prepared; offline experiments are running |

## Reproduce

For the earlier labs, install `lab_requirements_UTKRISHT.txt` in a Python 3 environment and run the cells in order. Those recorded CPU runs used Python 3.12, PyTorch 2.15.0 and torchvision 0.29.2. The newer Kaggle U-Net and QLoRA runs used Python 3.13.16 and T4. Follow the Module 3 notebooks' setup cells for their additional dependencies, preserving Kaggle's CUDA torch. Seeds and runtime details are recorded with each run; CPU and GPU results can differ numerically.

- **VAE data:** The recorded run uses the LFW **funneled** release from the scikit-learn-maintained [Figshare mirror](https://ndownloader.figshare.com/files/5976015), because the original deep-funneled endpoint was unavailable. This alignment variant differs from the scaffold's default deep-funneled release. The remaining preprocessing is unchanged: central crop, RGB 45×45 pixels, identities with fewer than 25 photos, seeded 80/20 image split. Set `LFW_DATASET_PATH` to the extracted `lfw_funneled` directory, or attach LFW on Kaggle. Do not compare results across alignment variants as if the input data were identical. Archive SHA-256: `b47c8422c8cded889dc5a13418c4bc2abbda121092b3533a83306f90d900100a`.
- **GAN data:** MNIST is downloaded on the first run. For offline execution, set `OFFLINE_MNIST_DIR` to a directory containing the four original IDX files. Set `TRAIN_LIMIT=None` for the full training split; keeping 5,000 records the executed limited-data configuration.
- **Translation data:** Download `bentrevett/multi30k` with Hugging Face datasets. Vocabulary is fitted on training pairs only. Set `MAX_TRAIN_PAIRS=12000` to restore the scaffold's original training budget or `None` for the complete train split. The notebook prints actual split sizes and model parameter counts. BLEU uses generated translations; perplexity uses reference-token evaluation.
- **Optional U-Net data:** The completed Kaggle run downloaded the original Oxford-IIIT Pet images and trimaps through torchvision. It used `SMOKE_TEST=False`, `DOWNLOAD=True`, 128×128 images, batch 16 and ten epochs. The seed-42 split was 5,912/739/739 images. Checkpoint selection used validation Dice; epoch 10 was selected before the held-out test evaluation. The notebook and [results](module1/labs/submissions/optional/A24ARIU0001_UNET_results/README.md) contain the actual plots and two displayed failure cases.

Outputs are embedded in the executed notebooks. Downloaded data and model checkpoints are excluded from version control. Model quality conclusions apply only to the displayed run and budget; these educational experiments do not establish production performance.
