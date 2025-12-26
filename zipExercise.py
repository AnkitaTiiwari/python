import zipfile, os  
from pathlib import Path

p = Path.cwd()

exampleZip = zipfile.ZipFile(p / 'example.zip')
# print(exampleZip.namelist())

# spamInfor = exampleZip.getinfo('spam.txt')
# print(spamInfor.file_size)
# print(spamInfor.compress_size)
# print(f"Compressed file is {round(spamInfor.file_size / spamInfor.compress_size, 2)} times smaller!")   
# exampleZip.close()

#Exatract everything
exampleZip.extractall('/Users/kimi/Documents/PythonProjects/python/AddSpamInBeginning')
exampleZip.close()

#Exatract only one file
exampleZip.extract('spam.txt')
