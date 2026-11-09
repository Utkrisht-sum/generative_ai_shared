# Patent project evidence — A24ARIU0001

The online weight-preparation notebook completed on Kaggle CPU. Its version is
https://www.kaggle.com/code/utkrishtsuman/a24ariu0001-patent-offline-weights/1.
The saved output contains DeBERTa-v3-small, MiniLM-L6-v2 and 53 dependency wheels.
The large checkpoints stay in Kaggle; they are not included in this repository.
The executed notebook beside this directory has both code cells executed and no
recorded errors. This step prepares inputs; it does not train or evaluate a model.

The official competition archive contains 36,473 training rows with 733 distinct
anchors and a 36-row visible test file without labels. The seed-42 grouped split
holds out 147 complete anchors: 28,914 training rows and 7,559 validation rows,
with no shared anchor. The row fraction is slightly different from 20% because
anchors have different numbers of pairs.

Splitting rows at random would let the same anchor appear on both sides. Holding
out anchors makes the evaluation test generalization to unseen anchors instead.
All model comparisons must keep this split. Section D has only 199 validation
pairs, compared with 1,926 in section B, so section-level results will also need
their sample sizes reported.

`weight_preparation.json` records the actual completed preparation. `data_audit.json`
records counts from the official training data. Model scores, training times,
error-analysis findings and leaderboard evidence remain pending until those
experiments execute. No hidden test labels or later fully rated data were used.

The first offline experiment attempt stopped during setup, before model training.
Its original bootstrap tried to reproduce every CPU-image dependency version and
requested a kernel restart whenever any scientific package was already loaded.
The corrected bootstrap resolves the required packages only from attached wheels,
preserves compatible installed dependencies and pins Kaggle's working CUDA torch.
It refuses to replace a package whose own code is already loaded. Attempt 2 passed
setup with four package changes and is running the unchanged experiments offline.
