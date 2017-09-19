import requests, re
from lxml import html
from bs4 import BeautifulSoup, SoupStrainer

url = 'https://www.wsj.com/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

# headline
def getHeadline():
    for headline in soup.find_all('div', class_='wsj-list'):
        for head in headline.find_all('h3', class_='wsj-headline'):
            for a in head.find_all('a'):
                print (a.text)

getHeadline();
