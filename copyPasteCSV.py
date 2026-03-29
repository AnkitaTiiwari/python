import csv,os,shutil
from pathlib import Path

landing_folder = Path('/Users/kimi/Documents/PythonProjects/python/RemoveHeader')
print(landing_folder)

for files in landing_folder.iterdir():
    print(files.name)

archive_folder = landing_folder / 'archive'
if not archive_folder.exists():
    os.makedirs(archive_folder)

for files in landing_folder.iterdir():
    shutil.move(files, archive_folder)