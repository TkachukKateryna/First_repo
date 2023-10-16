 
"""
Завдання: Сортування файлів у папці.
Cкопіювати файли із зазначеної папки та покласти в нову папку з розширенням цього файлу.
"""
​
import argparse
from pathlib import Path
from shutil import copyfile
​
# python main.py --source picture --output destination
parser = argparse.ArgumentParser(description='Sorting directory')
parser.add_argument('--source', '-s', required=True, help='Source folder')
parser.add_argument('--output', '-o', default='destination', help='Output folder')
​
args = vars(parser.parse_args())
source = args.get('source')
output = args.get('output')
print(source, output)
​
​
def read_folder(path: Path):
    for element in path.iterdir():
        if element.is_dir():
            read_folder(element)
        else:
            copy_file(element)
​
​
def copy_file(file: Path):
    ext = file.suffix  # .png
    new_path = output_folder / ext  # destination/.png
    new_path.mkdir(exist_ok=True, parents=True)  # створюємо відповідну папку
    copyfile(file, new_path / file.name)
​
​
output_folder = Path(output)
read_folder(Path(source))
        