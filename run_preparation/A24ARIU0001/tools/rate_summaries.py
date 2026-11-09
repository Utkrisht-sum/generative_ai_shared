#!/usr/bin/env python3
"""Record actual human ratings for the six blind QLoRA examples. No ML packages needed."""
import argparse
import csv
from pathlib import Path
import random

FIELDS=['example','A_faithful','A_coverage','B_faithful','B_coverage','note']

def score(prompt):
    while True:
        value=input(prompt+' (0/1/2): ').strip()
        if value in {'0','1','2'}:return int(value)
        print('Enter 0, 1 or 2.')

def review(folder):
    if not (folder/'summary_predictions.csv').exists():
        matches=list(folder.rglob('summary_predictions.csv'))
        if len(matches)!=1:raise ValueError('Choose a folder containing exactly one QLoRA summary_predictions.csv')
        folder=matches[0].parent
    with (folder/'summary_predictions.csv').open(encoding='utf-8',newline='') as f:
        rows=list(csv.DictReader(f))
    if len(rows)!=60:raise ValueError('Expected the prescribed 60 validation predictions; send a changed run for review first.')
    ids=random.Random(42).sample(range(60),6)
    records=[]
    path=folder/'blind_ratings.csv'
    print('Faithfulness: 2=no unsupported/contradictory claim; 1=minor issue; 0=major issue.')
    print('Coverage: 2=main points covered; 1=partial; 0=main event missing. Read the dialogue, not just the reference.')
    print('Model identities will be revealed after all six examples have been rated.')
    for i in ids:
        row=rows[i];a_model=random.Random(42+i).choice(['base','QLoRA'])
        b_model='QLoRA' if a_model=='base' else 'base'
        print('\n'+'='*60+'\nExample '+str(i))
        print('DIALOGUE:\n'+row['dialogue']+'\nREFERENCE:\n'+row['reference'])
        print('\nA:\n'+row[a_model]+'\n\nB:\n'+row[b_model])
        rating={'example':i}
        for key in FIELDS[1:-1]:rating[key]=score(key)
        note=''
        while not note:note=input('Specific note grounded in the dialogue: ').strip()
        rating['note']=note;records.append(rating)
        with path.open('w',newline='',encoding='utf-8') as f:
            w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(records)
    totals={'base':[0,0],'QLoRA':[0,0]}
    for record in records:
        i=record['example'];a=random.Random(42+i).choice(['base','QLoRA']);b='QLoRA' if a=='base' else 'base'
        for model,prefix in ((a,'A'),(b,'B')):
            totals[model][0]+=record[prefix+'_faithful'];totals[model][1]+=record[prefix+'_coverage']
        print('Example',i,': A =',a,', B =',b)
    for model,(faithful,coverage) in totals.items():
        print(f'{model}: faithfulness {faithful/6:.2f}/2; coverage {coverage/6:.2f}/2')
    print('Saved genuine ratings:',path)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('qlora_output_folder',type=Path)
    a=p.parse_args();review(a.qlora_output_folder)
