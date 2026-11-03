# Generative AI lab submissions — Utkrisht Suman

Roll number: **A24ARIU0001**

**These notebooks were reviewed and approved before publication to this fork.**

The original course templates and other students' files are preserved. These notebooks are separate student submissions.

| Lab | Notebook | Execution scope |
|---|---|---|
| Lab 1: Encoder–decoder | [Existing submission on lab1 branch](https://github.com/Utkrisht-sum/generative_ai_shared/blob/lab1/module1/labs/submissions/lab1/A24ARIU0001_ENCODER_DECODER_LAB_UTKRISHT_SUMAN.ipynb) | Already submitted; untouched |
| Lab 2: Face VAE | [Notebook](module1/labs/submissions/lab2/A24ARIU0001_VAE_FACES_LAB_UTKRISHT_SUMAN.ipynb) | LFW faces; 10-epoch main run and fresh beta=0/1 comparisons |
| Lab 3: GAN | [Notebook](module1/labs/submissions/lab3/A24ARIU0001_GAN_LAB_UTKRISHT_SUMAN.ipynb) | Fixed 5,000-image MNIST subset; 10 epochs each for baseline, faster D, conditional DCGAN |
| Seq2Seq attention | [Notebook](module2/labs/submissions/seq2seq_attention/A24ARIU0001_SEQ2SEQ_ATTENTION_LAB_UTKRISHT_SUMAN.ipynb) | CPU-limited Multi30k: 3,000 train pairs; up to 8 epochs/model; 200 test pairs |
| Optional U-Net | [Notebook](module1/labs/submissions/optional/A24ARIU0001_UNET_PET_SEGMENTATION_LAB_UTKRISHT_SUMAN.ipynb) | Implementation + synthetic shape/backprop checks; pet training remains pending dataset access |

## Reproduce

Install the packages in `lab_requirements_UTKRISHT.txt` in a Python 3 environment, open each notebook, and run its cells in order. Recorded runs used Python 3.12 and CPU PyTorch 2.15.0 with torchvision 0.29.2. Seeds are specified in each notebook. CPU and GPU runs can differ numerically.

- **VAE data:** The recorded run uses the LFW **funneled** release from the scikit-learn-maintained [Figshare mirror](https://ndownloader.figshare.com/files/5976015), because the original deep-funneled endpoint was unavailable. This alignment variant differs from the scaffold's default deep-funneled release. The remaining preprocessing is unchanged: central crop, RGB 45×45 pixels, identities with fewer than 25 photos, seeded 80/20 image split. Set `LFW_DATASET_PATH` to the extracted `lfw_funneled` directory, or attach LFW on Kaggle. Do not compare results across alignment variants as if the input data were identical. Archive SHA-256: `b47c8422c8cded889dc5a13418c4bc2abbda121092b3533a83306f90d900100a`.
- **GAN data:** MNIST is downloaded on the first run. For offline execution, set `OFFLINE_MNIST_DIR` to a directory containing the four original IDX files. Set `TRAIN_LIMIT=None` for the full training split; keeping 5,000 records the executed limited-data configuration.
- **Translation data:** Download `bentrevett/multi30k` with Hugging Face datasets. Vocabulary is fitted on training pairs only. Set `MAX_TRAIN_PAIRS=12000` to restore the scaffold's original training budget or `None` for the complete train split. The notebook prints actual split sizes and model parameter counts. BLEU uses generated translations; perplexity uses reference-token evaluation.
- **Optional U-Net data:** Attach the Oxford-IIIT Pet dataset with original images and trimaps. Set `PET_DATASET_PATH` to its root and `SMOKE_TEST=False`; alternatively set `DOWNLOAD=True` with working internet. Oxford download endpoints returned HTTP 503 in the execution environment and the attempted public Kaggle endpoint returned 404. No pet Dice/IoU, learning curves, real test masks, or visual failure findings have been fabricated. The complete real-data training/evaluation path is included, but this optional experiment is not yet an executed submission.

Outputs are embedded in the executed notebooks. Downloaded data and model checkpoints are excluded from version control. Model quality conclusions apply only to the displayed run and budget; these educational experiments do not establish production performance.
