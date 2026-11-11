# Gradio lab - A24ARIU0001

I tested Qwen2.5-1.5B-Instruct on Kaggle. The notebook and CSVs contain that run's outputs, and the written answers explain the results below.

| Run | Passed | Median seconds | Maximum seconds |
| --- | ---: | ---: | ---: |
| Original | 7/10 | 0.791 | 1.423 |
| Revised | 7/10 | 0.766 | 1.460 |

The extra allergy check passed. The revision did not increase the ten-test pass count. Cancellation after restaurant acceptance, grocery delivery and Bitcoin remain incorrect. The fixed action reply is faster because it does not use the language model.

Greedy probes gave the same UPI timeline three times. One sampled reply added an unsupported two-hour explanation. Streaming first text took 0.23-0.24 s; full replies took 0.80-2.48 s.

The executed notebook reports Gradio 6.30.0, Transformers 5.20.2 and torch 2.11.0+cu130. Those are the runtime versions, even though the install cell requests other versions.

## Still needed

The partner observation, rating and problem CSVs remain blank, and the anonymized chat log is missing. This run used `RUN_UI=False`, so it did not launch the app for a partner. I still need that session and its findings to complete the lab.
