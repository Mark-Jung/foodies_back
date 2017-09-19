import requests, re
from lxml import html
from bs4 import BeautifulSoup, SoupStrainer

url = 'http://www.theblaze.com/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

# headline
def getHeadline():
    for headline in soup.find_all('article', class_='feed'):
        for div in headline.find_all('div', class_='feed-bottom'):
            for head in headline.find_all('h3', class_='feed-title'):
                print (head.text)

getHeadline();
