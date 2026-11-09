"""Recompute the reported statistics from saved predictions, without training."""
import json
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent

def pearson(frame):
    return float(np.corrcoef(frame.score, frame.pred)[0, 1])

experiments = pd.read_csv(HERE / 'experiments.csv').set_index('name')
paths = {
    'section_baseline': 'val_section_baseline.csv',
    'minilm_no_training': 'val_minilm.csv',
    'context_none': 'val_context_none.csv',
    'context_code': 'val_context_code.csv',
}
frames = {name: pd.read_csv(HERE / path) for name, path in paths.items()}
reference = frames['section_baseline']
assert len(reference) == 7559 and reference.id.is_unique
for name, frame in frames.items():
    assert frame.id.equals(reference.id) and frame.score.equals(reference.score)
    assert np.isfinite(frame.pred).all()
    assert abs(pearson(frame) - experiments.loc[name, 'pearson']) < 1e-8
config = json.loads((HERE / 'best_config.json').read_text())
trained = experiments.loc[['section_baseline', 'context_none', 'context_code']]
assert config['name'] == trained.pearson.idxmax()
best = pd.read_csv(HERE / 'val_predictions.csv')
pd.testing.assert_frame_equal(best, frames[config['name']])
sections = pd.read_csv(HERE / 'section_scores.csv').set_index('section')
for section, group in best.groupby(best.context.str[0]):
    assert len(group) == sections.loc[section, 'n']
    assert abs(pearson(group) - sections.loc[section, 'pearson']) < 1e-8
means = pd.read_csv(HERE / 'score_means.csv')
computed = best.groupby('score').agg(n=('pred', 'size'), mean_pred=('pred', 'mean')).reset_index()
pd.testing.assert_frame_equal(computed, means)
errors = pd.read_csv(HERE / 'top_errors_for_review.csv')
expected = best.assign(abs_error=(best.pred - best.score).abs()).nlargest(10, 'abs_error')
assert errors.id.tolist() == expected.id.tolist()
assert np.allclose(errors.abs_error, expected.abs_error)
assert 2 <= errors.failure_type.nunique() <= 3
for column in ('failure_type', 'evidence', 'label_debatable'):
    assert errors[column].notna().all() and errors[column].str.strip().ne('').all()
final = pd.read_csv(HERE / 'final_val_predictions.csv')
assert final.id.equals(reference.id) and final.score.equals(reference.score)
summary = json.loads((HERE / 'run_summary.json').read_text())
assert abs(pearson(final) - summary['validation_pearson']) < 1e-10
submission = pd.read_csv(HERE / 'submission.csv')
assert submission.columns.tolist() == ['id', 'score'] and len(submission) == 36
assert submission.id.is_unique and submission.score.between(0, 1).all()
ledger = pd.read_csv(HERE / 'leaderboard_submissions.csv')
official = json.loads((HERE / 'kaggle_submission_status.json').read_text())
assert len(official) == len(ledger) == 1 and official[0]['ref'] == '58176236'
assert official[0]['status'] == 'SubmissionStatus.COMPLETE'
for column in ('public_score', 'private_score'):
    assert float(official[0][column]) == float(ledger.iloc[0][column])
print('Verified four paired comparisons, selection, section/score tables, ten reviewed errors, final predictions and the one recorded Kaggle result.')
print('Submissions-tab screenshot and course-platform acceptance require separate evidence.')
