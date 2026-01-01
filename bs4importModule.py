import bs4, requests,logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# res = requests.get('https://www.w3schools.com/python/')
# res.raise_for_status()

# resSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(resSoup))

# resSoup.select('title')
# print(resSoup.select('title')[0].getText())

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(elems[0].getText())
print(str(elems[0]))
print(elems[0].attrs)   