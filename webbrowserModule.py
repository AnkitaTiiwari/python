# import webbrowser
# webbrowser.open('http://www.python.org')


# import pyperclip,webbrowser
# address = pyperclip.paste()
# print(address)
# webbrowser.open(address)

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
print(len(res.text))
print(res.text[:250])
res.status_code == requests.codes.ok