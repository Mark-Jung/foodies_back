import requests
from lxml import html
from bs4 import BeautifulSoup, SoupStrainer
from sorting import  moreThanThreeMentions

url = 'https://www.wsj.com/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

# headline
def getHeadline():
    result =''
    for headline in soup.find_all('div', class_='wsj-list'):
        for head in headline.find_all('h3', class_='wsj-headline'):
            for a in head.find_all('a'):
                result = result + ' ' + a.text
    return result

text = getHeadline()
print(moreThanThreeMentions(text))
