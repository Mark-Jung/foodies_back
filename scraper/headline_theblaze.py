import requests, re
from bs4 import BeautifulSoup, SoupStrainer
from .sorting import moreThanTwoMentions

url = 'http://www.theblaze.com/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

def getHeadline():
    result = ''
    for headline in soup.find_all('article', class_='feed'):
        for div in headline.find_all('div', class_='feed-bottom'):
            for head in headline.find_all('h3', class_='feed-title'):
                result = result + ' ' + head.text
    return result

def get_theblaze_words():
    text = getHeadline()
    return moreThanTwoMentions(text)
