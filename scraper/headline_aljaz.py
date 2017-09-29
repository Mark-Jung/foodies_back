import requests, re
from bs4 import BeautifulSoup, SoupStrainer
from .sorting import moreThanThreeMentions

url = 'http://www.aljazeera.com/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

# Lastest News
def getLatestNews(self):
    result = ''
    for div in soup.find_all('div', class_='latest-news-topic'):
        for a in div.find_all('h4'):
            result = result + ' ' + a.text
    return result

# Trend News
def getTrendNews(self):
    trendResult = ''
    for div in soup.find_all('div', class_='news-trending-txt'):
        for p in div.find_all('p'):
            trendResult = trendResult + ' ' + p.text
    return trendResult

def get_aljaz_words(self):
    text = getLatestNews() + getTrendNews()
    return moreThanThreeMentions(text)
