#!/usr/bin/env python3
"""Build a four-page patent report from measured experiments and reviewed evidence."""
import argparse
import json
from pathlib import Path
from xml.sax.saxutils import escape

import pandas as pd
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, KeepTogether


def build(folder, destination, draft_without_screenshot=False):
    experiments = pd.read_csv(folder / 'experiments.csv')
    sections = pd.read_csv(folder / 'section_scores.csv')
    means = pd.read_csv(folder / 'score_means.csv')
    errors = pd.read_csv(folder / 'top_errors_for_review.csv').fillna('')
    ledger = pd.read_csv(folder / 'leaderboard_submissions.csv', dtype={'screenshot_file': str}).fillna({'screenshot_file': '', 'notes': ''})
    config = json.loads((folder / 'best_config.json').read_text())
    expected = {'section_baseline', 'context_none', 'context_code', 'minilm_no_training'}
    if not expected <= set(experiments.name) or not experiments.pearson.notna().all():
        raise ValueError('Run all four baselines/experiments and record finite Pearson values')
    if len(errors) != 10 or any(not errors[c].astype(str).str.strip().ne('').all()
                              for c in ('failure_type', 'evidence', 'label_debatable')):
        raise ValueError('Review all ten errors: fill failure_type, evidence and label_debatable')
    if not 2 <= errors.failure_type.nunique() <= 3:
        raise ValueError('Use two or three supported failure categories')
    if ledger.empty:
        raise ValueError('Record every real Kaggle submission before creating the final report')
    successes = ledger[ledger.status.str.lower().isin(['complete', 'completed', 'success'])]
    if successes.empty:
        raise ValueError('At least one completed Kaggle late submission is required')
    for _, row in successes.iterrows():
        for col in ('public_score', 'private_score'):
            if not -1 <= float(row[col]) <= 1: raise ValueError('Invalid Pearson score')
        if not str(row.notebook_url).strip(): raise ValueError('Missing notebook_url')
        screenshot = Path(str(row.screenshot_file))
        if not screenshot.is_absolute(): screenshot = folder / screenshot
        if not str(row.screenshot_file).strip() or not screenshot.is_file():
            if not draft_without_screenshot:
                raise ValueError('A real Submissions-tab screenshot is required for the final report')
    if draft_without_screenshot and not destination.name.endswith('.DRAFT.pdf'):
        raise ValueError('An evidence-incomplete report must have a .DRAFT.pdf filename')
    destination.parent.mkdir(parents=True, exist_ok=True)
    styles = getSampleStyleSheet()
    # Embed fonts so a reader's Helvetica substitute cannot distort the layout.
    fonts = Path('/usr/share/fonts/truetype/open-sans')
    font_name, bold_name = 'Helvetica', 'Helvetica-Bold'
    if (fonts / 'OpenSans-Regular.ttf').exists() and (fonts / 'OpenSans-Bold.ttf').exists():
        pdfmetrics.registerFont(TTFont('LabSans', str(fonts / 'OpenSans-Regular.ttf')))
        pdfmetrics.registerFont(TTFont('LabSans-Bold', str(fonts / 'OpenSans-Bold.ttf')))
        pdfmetrics.registerFontFamily('LabSans', normal='LabSans', bold='LabSans-Bold')
        font_name, bold_name = 'LabSans', 'LabSans-Bold'
    for name in ('Normal', 'BodyText'):
        styles[name].fontName = font_name
    for name in ('Title', 'Heading2'):
        styles[name].fontName = bold_name
    styles.add(ParagraphStyle('SmallLab', parent=styles['BodyText'], fontSize=8, leading=10, spaceAfter=5))
    styles.add(ParagraphStyle('TitleLab', parent=styles['Title'], fontSize=19, leading=23, textColor=colors.HexColor('#18354a')))
    story = []
    def p(text, style='BodyText'):
        return Paragraph(escape(str(text)).replace('\n', '<br/>'), styles[style])
    def add(text, style='BodyText'):
        story.extend([p(text,style), Spacer(1,6)])
    def heading(text): add(text,'Heading2')
    def table(rows, widths, small=True):
        data = [[p(v,'SmallLab' if small else 'BodyText') for v in row] for row in rows]
        t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e5edf2')),
            ('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),.35,colors.HexColor('#b7c6d0')),
            ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
            ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
        story.extend([t,Spacer(1,8)])
    add('Patent phrase matching','TitleLab')
    add('Utkrisht Suman | A24ARIU0001 | Measured experiment report','SmallLab')
    if draft_without_screenshot:
        add('DRAFT: scores verified through Kaggle API; required Submissions-tab screenshot is missing. Course-platform upload remains pending.','SmallLab')
    heading('1. Validation design and baselines')
    add('The model predicts a continuous similarity score for an anchor-target pair in CPC context. '
        'The supplied baseline uses DeBERTa-v3-small with a regression head and mean squared error. '
        'The seed-42 GroupShuffleSplit holds out 20% of anchor groups. Random row splitting would '
        'allow the same anchor to occur in both sets and could overstate generalization.')
    rows=[['Run / changed factor','Validation r','Training min','Peak GB']]
    for _,r in experiments.iterrows():
        rows.append([str(r['name'])+'\n'+str(r['changed']),f'{r.pearson:.4f}',f'{r.minutes:.2f}',
                     '-' if pd.isna(r.peak_GB) else f'{r.peak_GB:.2f}'])
    table(rows,[245,65,75,66])
    base=float(experiments.set_index('name').loc['section_baseline','pearson'])
    embed=float(experiments.set_index('name').loc['minilm_no_training','pearson'])
    add(f'The pretrained MiniLM bi-encoder, with no task training, obtained r={embed:.4f}; the fine-tuned cross-encoder obtained '
        f'r={base:.4f} (difference {base-embed:+.4f}). MiniLM encodes each phrase separately and compares '
        'normalized mean-pooled embeddings. The cross-encoder attends jointly across both phrases. '
        'The comparison changes the checkpoint and training regime together; it cannot isolate the effect of fine-tuning alone.')
    add('Training: maximum length 64, batch 32, three epochs, learning rate 2e-5, warmup ratio 0.1, '
        'weight decay 0.01. Timings cover Trainer.train(), including epoch evaluation; MiniLM has no training time. '
        'Peak memory is allocated CUDA memory, excluding other processes and some reserved memory.','SmallLab')
    story.append(PageBreak())
    heading('2. Controlled context experiments')
    for name in ('context_none','context_code'):
        row=experiments.set_index('name').loc[name]; delta=float(row.pearson)-base
        add(f'{name}: only the context representation changes; delta r={delta:+.4f}. '+
            ('The difference is at most 0.005 and may be seed noise.' if abs(delta)<=.005 else
             'This result is for one split and seed, so it is not evidence of a universal improvement.'))
    add(f"Selected for the final run: {config['name']} using validation r={config['validation_pearson']:.4f}. "
        'All variants use the same validation IDs and initial checkpoint. No leaderboard score was used for selection.')
    heading('3. Section and score analysis')
    table([['Section','N','Pearson r']]+[[r.section,int(r.n),'-' if pd.isna(r.pearson) else f'{r.pearson:.4f}']
          for _,r in sections.iterrows()],[170,110,171])
    valid=sections.dropna(subset=['pearson']).sort_values('pearson')
    if len(valid):
        add(f"The lowest measured section is {valid.iloc[0].section} (n={int(valid.iloc[0].n)}). "
            'Five of the ten largest errors are in G. The smallest group, D (199 pairs), is not the lowest. '
            'Technical relations under coarse context are a hypothesis to investigate, not an established cause.','SmallLab')
    table([['True score','N','Mean prediction']]+[[f'{r.score:.2f}',int(r.n),f'{r.mean_pred:.3f}'] for _,r in means.iterrows()], [170,110,171])
    add('Zero labels move inward and 0.75 is underpredicted, but the mean at 1 overshoots: compression is not uniform. '
        'The dominant 0.25/0.5 labels and squared-error regression can contribute to central tendency, but do not explain every group. '
        'These are raw predictions; only submission predictions are clipped to [0,1]. Pearson alone does not establish calibration.','SmallLab')
    story.append(PageBreak())
    heading('4. Largest validation errors')
    add('These ten pairs have the largest absolute errors for the validation-selected model. Categories and explanations below come from the reviewed error CSV; disagreement alone does not establish that an expert label is wrong.','SmallLab')
    rows=[['Anchor / target / context','True / predicted','Reviewed failure and evidence']]
    for _,r in errors.iterrows():
        text=f'{r.anchor} / {r.target} [{r.context}]'
        evidence=f'{r.failure_type}: {r.evidence}\nLabel debatable: '+('possibly; expert context needed' if r.label_debatable.startswith('Possibly') else 'no clear issue')
        rows.append([text[:150],f'{r.score:.2f} / {r.pred:.3f}',evidence])
    table(rows,[175,65,211])
    add('The complete unabridged notes and validation predictions accompany this report. Error categories are descriptive observations from these cases; the ten largest errors are not a representative sample of the whole validation set.','SmallLab')
    story.append(PageBreak())
    heading('5. Late submissions and score comparison')
    table([['Version / status','Public r','Private r']]+[[str(r.version)+' / '+str(r.status),str(r.public_score),str(r.private_score)]
          for _,r in ledger.iterrows()],[245,103,103])
    for _,r in successes.iterrows():
        add(f"Version {r.version}: public-minus-validation {float(r.public_score)-config['validation_pearson']:+.4f}; "
            f"private-minus-validation {float(r.private_score)-config['validation_pearson']:+.4f}.",'SmallLab')
    summary_file = folder / 'run_summary.json'
    if summary_file.exists():
        summary = json.loads(summary_file.read_text())
        add(f"The final saved run independently reproduces validation r={summary['validation_pearson']:.9f}; "
            f"its Trainer-reported runtime is {summary['trainer_train_runtime_seconds']:.4f} seconds. "
            'For the recorded submission, both hidden scores are lower and the private result is closer to validation.','SmallLab')
    add('Validation, public and private partitions can differ in anchor mix, CPC sections and size. Selecting settings using validation also introduces selection optimism. The final notebook trains only the validation-selected variant, loads attached local weights with internet off, and writes id,score in submission.csv. The same grouped training budget is retained for reproducibility.')
    add('Every submission is listed above, including failures. Version URLs and screenshot evidence:','SmallLab')
    for _,r in ledger.iterrows():
        add(f'{r.version}: {r.notebook_url}\nScreenshot: {r.screenshot_file or "MISSING"}\nNotes: {r.notes}','SmallLab')
    heading('References and attribution')
    for ref in [
        'Course patent_phrase_starter.ipynb, download_weights.ipynb and project_brief.md, bk-anupam/generative_ai_shared (adapted starter code).',
        'Kaggle: U.S. Patent Phrase to Phrase Matching, competition data and rules. https://www.kaggle.com/competitions/us-patent-phrase-to-phrase-matching',
        'He et al. (2021). DeBERTaV3. arXiv:2111.09543. Model: microsoft/deberta-v3-small (MIT).',
        'Reimers & Gurevych (2019). Sentence-BERT. arXiv:1908.10084. Model: sentence-transformers/all-MiniLM-L6-v2 (Apache-2.0).',
        'Aslanyan & Wetherbee (2022). Patents Phrase to Phrase Semantic Matching Dataset. arXiv:2208.01171. Only competition train/test files used; no released test labels.']:
        add(ref,'SmallLab')
    def footer(canvas,doc):
        canvas.setFont(font_name,8);canvas.setFillColor(colors.HexColor('#50626f'))
        canvas.drawString(72,30,'A24ARIU0001 | Patent phrase matching' + (' | DRAFT: screenshot missing' if draft_without_screenshot else ''))
        canvas.drawRightString(A4[0]-72,30,str(doc.page))
    draft = destination.with_name(destination.stem + '.draft.pdf')
    doc=SimpleDocTemplate(str(draft),pagesize=A4,leftMargin=72,rightMargin=72,topMargin=48,bottomMargin=48)
    doc.build(story,onFirstPage=footer,onLaterPages=footer)
    from pypdf import PdfReader
    pages=len(PdfReader(draft).pages)
    if pages>4:
        draft.unlink(missing_ok=True)
        raise ValueError(f'Report has {pages} pages; shorten the reviewed notes/ledger and regenerate to meet the four-page limit')
    draft.replace(destination)
    print(f'Saved {pages}-page report: {destination}. Render and read it before submitting.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output_folder',type=Path)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--draft-without-screenshot', action='store_true',
                        help='Create an explicitly marked .DRAFT.pdf; final-report evidence checks remain strict')
    a=parser.parse_args()
    name = 'A24ARIU0001_PATENT_REPORT_UTKRISHT_SUMAN' + ('.DRAFT.pdf' if a.draft_without_screenshot else '.pdf')
    build(a.output_folder,a.output or a.output_folder/name,a.draft_without_screenshot)
