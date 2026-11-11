# Gradio lab - A24ARIU0001

The notebook and CSVs come from the Kaggle run with Qwen2.5-1.5B-Instruct. The written answers use this run's results. No new inference was run during this review.

| Run | Passed | Median seconds | Maximum seconds |
| --- | ---: | ---: | ---: |
| Original | 7/10 | 0.791 | 1.423 |
| Revised | 7/10 | 0.766 | 1.460 |

The extra allergy check passed. The revision did not increase the ten-test pass count. Cancellation after restaurant acceptance, grocery delivery and Bitcoin remain incorrect. The fixed action reply is faster because it does not use the language model.

Greedy probes gave the same UPI timeline three times. One sampled reply added an unsupported two-hour explanation. Streaming first text took 0.23-0.24 s; full replies took 0.80-2.48 s.

The executed notebook reports Gradio 6.30.0, Transformers 5.20.2 and torch 2.11.0+cu130. Those are the runtime versions, even though the install cell requests other versions.

## Still needed

The partner observation, rating and problem CSVs are blank, and no chat_log.csv was supplied. The app was not launched in this run (RUN_UI=False). The partner session and its findings must be added before this is a complete lab submission.
