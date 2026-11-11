#!/usr/bin/env python3
"""Collect review outputs without datasets, environments or model weights. Standard library only."""
import argparse
from pathlib import Path
import zipfile
import json
import hashlib

SKIP_DIRS={'.venv','venv','.git','__pycache__','.cache','node_modules','site-packages',
           'patent_runtime_wheels','deberta-v3-small','all-MiniLM-L6-v2','data','adapter',
           'trainer','trainer_tmp','patent_weights','reference_evidence'}
JSON_NAMES={'best_config.json','run_summary.json','test_metrics.json','history.json','CHECKS.json'}
SKIP_FILES={'train.csv','test.csv','sample_submission.csv','IndianFoodDatasetCSV.csv',
            'tokenizer.json','config.json','tokenizer_config.json','adapter_config.json'}
SUFFIXES={'.ipynb','.csv','.png','.jpg','.jpeg','.pdf','.log','.txt'}

def eligible(path):
    if path.is_symlink() or not path.is_file():return False
    if any(p in SKIP_DIRS or p.startswith('checkpoint-') for p in path.parts):return False
    if path.name in SKIP_FILES:return False
    if path.suffix.lower()=='.json':return path.name in JSON_NAMES
    if path.suffix.lower() not in SUFFIXES:return False
    if path.suffix.lower()=='.txt' and path.name not in {'notebook_urls.txt','errors.txt','review_notes.txt'}:return False
    return True

def collect(roots,destination):
    destination=destination.resolve();destination.parent.mkdir(parents=True,exist_ok=True)
    count=0;manifest=[]
    with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED) as archive:
        for index,root in enumerate(roots,1):
            root=root.resolve()
            if not root.exists():raise FileNotFoundError(root)
            paths=[root] if root.is_file() else sorted(root.rglob('*'))
            for path in paths:
                if path.resolve()==destination or not eligible(path):continue
                relative=Path(path.name) if root.is_file() else path.relative_to(root)
                arc=Path(f'{index:02d}_{root.stem}')/relative
                archive.write(path,str(arc));count+=1
                manifest.append({'path':str(arc),'bytes':path.stat().st_size,
                                 'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
        archive.writestr('RETURN_MANIFEST.json',json.dumps(manifest,indent=2))
    if count==0:
        destination.unlink();raise ValueError('No review outputs found. Check the input folder.')
    print(f'Saved {count} files: {destination} ({destination.stat().st_size/1e6:.2f} MB)',flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('folders',nargs='+',type=Path)
    p.add_argument('--output',type=Path,default=Path('A24ARIU0001_RESULTS_FOR_REVIEW.zip'))
    a=p.parse_args();collect(a.folders,a.output)
