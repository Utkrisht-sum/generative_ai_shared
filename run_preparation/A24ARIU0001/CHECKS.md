# Verification — A24ARIU0001

Updated 9 November 2026 UTC. Executed artifacts live in the topic directories;
preparation notebook copies are source templates.

| Run | Genuine execution evidence |
| --- | --- |
| QLoRA DialogSum | All 28 code cells completed on T4; 122 optimizer steps, 14.4251 minutes, 6.3716 GB peak allocated memory. Independently recomputed ROUGE-L 23.0003 → 37.1122 on 60 fixed validation pairs. Six human ratings remain blank. |
| Oxford pet U-Net | All five code cells completed on T4 with original data, 5,912/739/739 split and ten epochs. Test Dice 0.879322 and IoU 0.784634. Real figures inspected; code/output cells match the collected executed artifact. |
| Patent weight preparation | Both code cells completed; both checkpoints verified and 53 wheels saved. |
| Patent experiments v2 | All 15 code cells completed offline on T4. Four comparison CSVs have identical validation IDs and labels; independent correlations agree within 1e-8. Section/score summaries and all ten largest-error IDs recomputed. |
| Patent final v1 | All 11 code cells completed offline on T4. Validation Pearson 0.820194478; visible CSV has exactly id,score, 36 unique IDs in official sample order and finite scores in [0,1]. Code/output cells match the executed artifact. |
| Kaggle late submission | One entry, 58176236, completed: public 0.7922 and private 0.8084. Official API response and ledger agree. No baseline entry or leaderboard-driven model change. |
| Patent report | Four pages; rendered and read. Explicitly marked DRAFT because the required Submissions-tab screenshot is missing. Default final-report mode still rejects that omission. |

The first patent attempt failed only in offline dependency setup before training.
The corrected bootstrap keeps compatible installed dependencies and CUDA torch,
resolves required roots offline, and checks imported distribution files before
replacement. Model, data, evaluation and training controls were preserved.

The QLoRA optimizer assertion compares the enum value `paged_adamw_8bit`; the
original lowercase substring check failed against its uppercase enum name. The
corrected check was validated with the intended settings and rejected six
incorrect configurations. That fix did not change the optimizer or budget.

Existing Labs 1–5 and GPT-2 were inspected rather than retrained: every nonempty
code cell has an execution count and no recorded error. Their original limits
and data variants remain disclosed in the main submission dashboard.

GitHub authentication and Kaggle SDK authentication now work. The scored patent
version and its two notebook inputs are public, verified using the official
metadata API. Quick saves changed visibility without launching new GPU jobs.
Course PRs #127 and #160 are open and unmerged; Gradio fork PR #2 remains draft.
The attempt to create a course U-Net PR was denied by integration permissions.
Its clean comparison branch is pushed; no PR creation or course acceptance is
claimed. Fork draft PR #3 collects the continuation results.

The required human ratings, real Gradio partner session, official Kaggle UI
screenshot and course-platform upload remain outside the completed evidence.
No observations, scores, screenshots or submission receipts were simulated.
