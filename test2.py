import os
from pathlib import *

current_dir = Path.cwd()

print (current_dir)

home_dir = Path.home()
print(home_dir)

print(os.getcwd())