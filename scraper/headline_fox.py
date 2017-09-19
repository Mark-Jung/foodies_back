import requests, re
from bs4 import BeautifulSoup, SoupStrainer

url = 'http://www.foxnews.com/'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")

# Latest News
def getLatestNews():
    for section in soup.find_all('article', class_='article'):
        for div in section.find_all('div', class_='info'):
            for a in div.find_all('a'):
                print (a.text)

getLatestNews()
