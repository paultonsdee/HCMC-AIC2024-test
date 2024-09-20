import os
import sys
import subprocess
from pathlib import Path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # Root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]  # Root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

print(sys.path)

path = './db'

# print(os.listdir(path))

import os

import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
print(project_root)

print(os.path.exists('/home/octoopt/Desktop/Lab/Personal/HCMC-AIC2024/db/features/blip2fe.bin'))