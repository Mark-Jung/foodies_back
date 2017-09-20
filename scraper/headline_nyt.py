import requests
from lxml import html
from bs4 import BeautifulSoup, SoupStrainer
from sorting import moreThanThreeMentions

url = 'https://www.nytimes.com/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

# headline
def getHeadline():
    result = ''
    for headline in soup.find_all('article', class_='story'):
        for a in headline.find_all('a'):
            result = result + ' ' + a.text
    return result

text = getHeadline()
print(moreThanThreeMentions(text))


