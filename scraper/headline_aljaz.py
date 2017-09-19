import requests, re
from bs4 import BeautifulSoup, SoupStrainer

url = 'http://www.aljazeera.com/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

# Lastest News
def getLatestNews():
    for div in soup.find_all('div', class_='latest-news-topic'):
        for a in div.find_all('h4'):
            print (a.text)

# Trend News
def getTrendNews():
    for div in soup.find_all('div', class_='news-trending-txt'):
        for p in div.find_all('p'):
            print (p.text)

print ('Latest News:')
getLatestNews()

print ('Trends:')
getTrendNews()
