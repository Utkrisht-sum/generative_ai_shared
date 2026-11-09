"""Run online once in Kaggle to save offline non-CUDA dependencies beside the model weights."""
from importlib import metadata
import json
from pathlib import Path
import subprocess
import sys
from packaging.requirements import Requirement
from packaging.utils import canonicalize_name

ROOTS = ['transformers==5.22.2','accelerate==1.15.0','datasets==5.1.0',
         'scikit-learn>=1.4','sentencepiece==0.2.3','protobuf','pandas>=2.1','matplotlib>=3.8']

def dependency_pins(roots):
    pending = [Requirement(r).name for r in roots]
    seen = set(); pins = []
    while pending:
        name = canonicalize_name(pending.pop())
        if name in seen or name in {'torch','torchvision','torchaudio','triton'} or name.startswith(('nvidia-','cuda-')):
            continue
        seen.add(name)
        dist = metadata.distribution(name)
        pins.append(f'{dist.metadata["Name"]}=={dist.version}')
        for spec in dist.requires or []:
            dep = Requirement(spec)
            if dep.marker is None or dep.marker.evaluate({'extra': ''}):
                pending.append(dep.name)
    return sorted(pins, key=str.lower)

def prepare(out):
    out.mkdir(parents=True,exist_ok=True)
    # Keep Kaggle's working CUDA torch installation. Do not download CUDA wheels.
    torch_version = metadata.version('torch')
    constraints = out/'keep_cuda_torch.txt'
    constraints.write_text('torch=='+torch_version+'\n')
    subprocess.run([sys.executable,'-m','pip','install','-q','-c',str(constraints),*ROOTS],check=True)
    pins=dependency_pins(ROOTS)
    subprocess.run([sys.executable,'-m','pip','download','--only-binary=:all:','--no-deps',
                    '--dest',str(out),*pins],check=True)
    (out/'wheels_manifest.json').write_text(json.dumps({'python':sys.version.split()[0],
        'torch':torch_version,'requirements':pins},indent=2))
    print('Offline runtime saved:',out,flush=True)
    return pins

if __name__=='__main__':
    base=Path('/kaggle/working') if Path('/kaggle/working').exists() else Path('patent_weights')
    prepare(base/'patent_runtime_wheels')
