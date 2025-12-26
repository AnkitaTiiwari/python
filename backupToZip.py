import shutil, os, zipfile
from pathlib import Path

#get current folder which needs to be archived
p = Path.cwd()
folder = p / 'AddSpamInBeginning'

zipName = ''

while True:
    #create zipfile name here
    number = 1
    zipName = os.path.basename(folder) + '_' + str(number) + '.zip'
    if not os.path.exists(zipName):
        break
    number = number + 1


#make zip file
zipf = zipfile.ZipFile(zipName, 'w', zipfile.ZIP_DEFLATED) 

for foldername, subfolders, filenames in os.walk(folder):
    zipf.write(foldername)

    for filename in filenames:
        newbase = os.path.basename(folder) + '_'
        if filename.startswith(newbase) and filename.endswith('.zip'):
            continue
        filePath = os.path.join(foldername, filename)
        zipf.write(filePath)
zipf.close()
print('Done')
