# Oxford pet U-Net results — A24ARIU0001

I completed the ten-epoch Oxford-IIIT Pet run on Kaggle T4:
https://www.kaggle.com/code/utkrishtsuman/a24ariu0001-unet-pet-segmentation?scriptVersionId=367827217.
This exact saved version is public for instructor access.
All five code cells completed without recorded errors. The notebook includes
the saved outputs and my observations from the prediction figures.

| Split / selection | Dice | IoU |
| --- | ---: | ---: |
| Best validation, epoch 10 | 0.8750 | 0.7778 |
| Held-out test, 739 images | 0.8793 | 0.7846 |

The seed-42 split has 5,912 training, 739 validation and 739 test image–mask pairs.
Images are 128×128, batch size is 16, and boundary pixels count as foreground
(`trimap != 2`). Metrics pool intersections and mask areas over the complete split.
The test set is used after validation checkpoint selection. The training/evaluation
cell took 628.91 seconds including evaluation, plotting and checkpoint operations;
that is not an isolated training-time benchmark.

- `history.json`: all ten training and validation records.
- `test_metrics.json`: the actual held-out loss, Dice and IoU.
- `run_summary.json`: configuration, split sizes and selection metadata.
- `data_examples.png`: the five inspected image–mask pairs.
- `training_curves.png`: actual loss and Dice curves.
- `test_predictions.png`: all eight displayed test cases.

The lowest displayed case is index 4 (Dice 0.7269), where the held dog's head is
partly missed and a mirror-area patch is falsely marked. Index 1 (0.8024) misses
part of the window-side cat's body and paws. These findings refer to the actual
displayed masks and do not identify the worst examples across the whole test set.

The earlier synthetic smoke checks remain in Git history. This notebook records
the completed pet-data experiment. Downloaded images and checkpoint weights are
kept outside the repository.

Data source: [Oxford-IIIT Pet](https://www.robots.ox.ac.uk/~vgg/data/pets/),
Parkhi et al. (2012), downloaded with torchvision. Architecture follows the
course's small U-Net specification; see Ronneberger et al. (2015),
[U-Net](https://arxiv.org/abs/1505.04597), for the original architecture.
