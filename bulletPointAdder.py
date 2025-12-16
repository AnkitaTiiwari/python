#bullet point adder

import sys,pyperclip

text = pyperclip.paste()
#print(text)

#now here we'd add the bullet points
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)


pyperclip.copy(text)
print("Added bullet points to clipboard text.")
print(text)