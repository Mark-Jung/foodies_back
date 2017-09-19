import requests, re
from lxml import html
from bs4 import BeautifulSoup, SoupStrainer

url = 'https://www.nytimes.com/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")


# headline
def getHeadline():
    for headline in soup.find_all('article', class_='story'):
        for a in headline.find_all('a'):
            print (a.text)

#head = soup.find_all('a')
#headline = head.string
#headline = soup.find_all('article', class_='story')
#head = soup.find_all(class_='story-heading')

getHeadline();