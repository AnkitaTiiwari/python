#renaming file to european date format DD-MM-YYYY from MM-DD-YYYY

import shutil,os
from pathlib import Path
import re

USDatePattern = re.compile(r'(0[1-9]|1[0-2])_(0[1-9]|[12][0-9]|3[01])_(\d{4})')

#check in current WD if we have a file
p = Path.cwd()

print(p)
folderToCheck = p / 'RenamingDates'

hasFilesOrNot = ''

print(folderToCheck)

for foldername, subfolders, filenames in os.walk(folderToCheck):
    #print('reached here')
    for filename in filenames:
        #print(filename)
        hasFilesOrNot = 'Y'

#print(hasFilesOrNot)

#check if it has date in american style
if hasFilesOrNot == 'Y':
    #print(filenames)
    for filename in filenames:
        mo = USDatePattern.search(filename)
        print(f"Found US date format in file: {mo.group()}")
        if mo != None:
            Filemonth = mo.group(1)
            Filedate = mo.group(2)
            Fileyear = mo.group(3)
            EuroFilename = 'file1' + Filedate +'-' + Filemonth+'-' + Fileyear + '.txt'
            print(f'Renaming {filename} to {EuroFilename}...')
            shutil.move(folderToCheck / filename, folderToCheck /EuroFilename)

#make file name 
            