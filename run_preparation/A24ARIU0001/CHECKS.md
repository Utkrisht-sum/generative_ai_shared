# Checks performed for this preparation

These checks used the current cloud machine. They do not represent completed
training runs or new model-quality measurements.

- All five pending notebooks passed notebook-format validation. All 61 code cells
  compiled, and all five helper scripts compiled.
- The QLoRA check failed with the original optimizer-enum comparison and passed
  after comparing the enum value. Both the enum and its string value were
  accepted. Disabled fp16, enabled bf16, ordinary AdamW, paged 32-bit AdamW,
  incorrect effective batch size and incorrect adapter parameter count were
  rejected. The model and training settings were preserved.
- The U-Net notebook executed cells 1–8 in synthetic smoke mode on CPU. The final
  shape was (2, 1, 128, 128), all skip-connection shapes matched, and the model had
  1,925,601 parameters. One optimizer update produced a finite loss and changed
  the output-layer weights. No Oxford pet accuracy, Dice or IoU was measured.
- The committed U-Net defaults remain real-data mode, downloading enabled,
  128×128 images, batch 16 and ten epochs. Smoke mode was a command-line override
  for the local check, with the executed prefix saved outside this repository.
- Existing Labs 1–5 and GPT-2 notebooks in the fork have execution counts in every
  nonempty code cell and no recorded error outputs. This is an inspection of
  saved outputs, not a new run or proof of course acceptance.
- Live GitHub pages confirmed GPT-2 fork PR #1 is merged and Gradio fork PR #2 is
  still a draft. The Gradio head is f6831dc2139662ddd829d84e6e9bed6d9670e0b0.
- Native Git reads succeeded. At preparation time, the GitHub API request returned
  Forbidden, and no Kaggle token or CUDA device was present. GPU training and
  final submissions were not performed by these checks.
- After the environment was published, GitHub API reads succeeded and preparation
  draft PR #3 was created. The current Kaggle token binding reports ready, but
  authentication through the official client's api.kaggle.com endpoint returned
  proxy HTTP 403. The running policy and the credential destination list do not
  include that host. A network-rule addition is saved in the draft; the settings
  tool requires editing the existing credential destination list in the UI.
- Course-repository PR #127 (Lab 1/Lab 5 corrections) and PR #160 (GPT-2) were
  confirmed open, unmerged and clean. No duplicate submission PR was created.

The Gradio partner study and QLoRA human ratings remain pending. Their blank
templates have not been filled with simulated observations.
