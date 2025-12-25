import shutil,os,re
from pathlib import Path

regex = re.compile(r'00*')

p = Path.cwd()

folder = p / 'removeZero'

for foldernames, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith('.txt'):
            newFilename = regex.sub('', filename)
            src = Path(foldernames) / filename
            dst = Path(foldernames) / newFilename
            print('moving', src, 'to', dst)
            shutil.move(src, dst)  # Rename the file    