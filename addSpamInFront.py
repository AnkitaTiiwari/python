import shutil,os
from pathlib import Path


p = Path.cwd()

folder = p / 'AddSpamInBeginning'

for foldernames, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if filename.endswith('.txt'):
            print('here')
            newFFilename = 'spam_' + filename
            src = Path(foldernames) / filename
            dst = Path(foldernames) /  newFFilename
            print('moving', src, 'to', dst)
            dst.parent.mkdir(exist_ok=True)  # Ensure the spam directory exists
            shutil.move(src, dst)  # Copy the file to the spam directory