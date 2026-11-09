# Gradio lab results - A24ARIU0001

Utkrisht Suman. Results supplied from a Kaggle run. This is a partial submission awaiting the partner study; no missing observations have been filled in.

## Automated evaluation

The original and revised functions each pass 7 of the same 10 literal checks. The additional revised allergen guard check passes. These checks measure expected substrings, not complete factual correctness or user experience.

| Run | Core passes | Median completion seconds | Maximum seconds |
| --- | ---: | ---: | ---: |
| Original | 7/10 | 0.791 | 1.423 |
| Revised | 7/10 | 0.766 | 1.460 |

The cancellation reply incorrectly gives the free-within-60-seconds rule when the restaurant has already accepted. The grocery reply claims an unsupported service. The Bitcoin reply invents a restriction to INR/app-wallet payments instead of refusing an unanswered question. These remain unresolved in the supplied revised results.

The original action-request response already passes by directing the user to support. The revision gives an explicit deterministic statement that it cannot issue refunds, cancel orders or access order details; this preserves the pass rather than increasing the pass count. Its very small measured runtime reflects a fixed response, not faster language-model inference. The allergen guard explicitly avoids guaranteeing safety.

## Decoding probes

All three greedy replies state the same UPI refund timeline. The sampled replies vary; one introduces an unsupported two-hour transit explanation. This shows that greater variation can add unsupported details. The CSV does not establish token truncation behaviour or streaming time to first text.

## Pending evidence

- Genuine partner session and chat_log.csv.
- Completed partner_observations.csv, partner_ratings.csv and observed_problems.csv (currently blank templates).
- Final findings, partner-based improvement analysis and reflection after those records are supplied.

The CSVs are preserved as uploaded. This draft does not claim a completed human study, higher automated accuracy after revision, or that the partner session took place.
