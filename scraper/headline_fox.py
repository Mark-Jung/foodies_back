import requests, re
from lxml import html
from bs4 import BeautifulSoup, SoupStrainer
from .sorting import moreThanThreeMentions

url = 'http://www.foxnews.com/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

# Latest News
def getLatestNews():
    result = ''
    for section in soup.find_all('article', class_='article'):
        for div in section.find_all('div', class_='info'):
            for h2 in div.find_all('h2', class_='title'):
                for a in h2.find_all('a'):
                    result = result + ' ' + a.text
    return result

def get_fox_words():
    text = getLatestNews()
    return moreThanThreeMentions(text)
