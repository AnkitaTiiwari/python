# mClip.py
import sys,pyperclip

text_dict = {
    'agree' : 'I agree with you',
    'disagree' : 'I disagree with you!',
    'negotiate' : 'Let\'s negotiate on the matter'
}

next_step  = input('Enter what do you wanna do : ')


if next_step not in text_dict:
    sys.exit('No text found for that key!')

pyperclip.copy(text_dict[next_step]
                      )

sen = pyperclip.paste()
print(sen)
