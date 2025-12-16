#get phone numbers and emails from a text file
from pydoc import text
import re, pyperclip

text = str(pyperclip.paste())

phoneRegex = re.compile(
                        r'''(\d){4}
                        (\s|\.|-)?
                        (\d){3}
                        (\s|\.|-)?
                        (\d){4}'''
                        ,re.IGNORECASE|re.DOTALL|re.VERBOSE
                        )

emailRegex = re.compile(
                    r'''[a-zA-Z0-9._]
                    @
                    [a-zA-Z0-9._]
                    .com
                    '''
                    ,re.IGNORECASE|re.DOTALL|re.VERBOSE
                       
                        )

#get the text 


allPhoneNumbers = []
allEmails = []
#find the phone numbers and emails


for group in phoneRegex.findall(text):
    allPhoneNumbers.append('-'.join([group[0],group[2],group[4]]))   

for groups in emailRegex.findall(text):
    allEmails.append(groups[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(allEmails)
if len(results) > 0:
    pyperclip.copy(results)
    print('Copied to clipboard:')
    print(results)
else:
    print('No phone numbers or email addresses found.')