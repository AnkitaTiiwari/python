
import shutil,os
from pathlib import Path

p = Path.cwd()

print(p)
src = p / 'spam' / 'test.txt'
dst = p / 'spam2/test3' 

print(src)
print(dst)

print(src.exists(), src.is_file())  # Check if the source file exists and is a file
print(dst.exists(), dst.is_dir())  # Check if the destination directory exists and is a directory

#shutil.copy(src, dst)

#shutil.move(src, dst)

##if extension not given , it copies with same name