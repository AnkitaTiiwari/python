from pathlib import Path
import os
#Path.cwd()

#os.chdir('/Users/kimi/Documents/')

#Path.home()

#Path(r'/Users/kimi/Documents/PythonProjects/python/spam').mkdir()
#os.mkdir('/Users/kimi/Documents/PythonProjects/python/spam2')

#os.path.abspath('.')
#os.path.abspath('workingWithFiles.py')
#print(os.path.isabs('.'))

####Writing and reading into a file
# p = Path('spam/test.txt')
# p.write_text('Hello, world!')
# p.read_text()

##Opening the file and reading and writing
# testFile = open('spam/test.txt', 'r')
# content = testFile.read()
# print(content)
# print(testFile.readline())

#opening a file and write into it, in write and append mode
baconFile = open('Bacon.txt','w')
baconFile.write('This is a new world for me \n')
baconFile.close()

baconFile = open('Bacon.txt','a')
baconFile.write('this is whole fucking new world \n')
baconFile.close()

baconFile = open('Bacon.txt')
content = baconFile.read()
print(content)
baconFile.close()