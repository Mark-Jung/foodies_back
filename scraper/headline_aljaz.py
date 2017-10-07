import requests, re
from bs4 import BeautifulSoup, SoupStrainer

url = 'http://www.aljazeera.com/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

# Lastest News
def getLatestNews():
    result = ''
    for div in soup.find_all('div', class_='latest-news-topic'):
        for a in div.find_all('h4'):
            result = result + ' ' + a.text
    return result

# Trend News
def getTrendNews():
    trendResult = ''
    for div in soup.find_all('div', class_='news-trending-txt'):
        for p in div.find_all('p'):
            trendResult = trendResult + ' ' + p.text
    return trendResult

def get_aljaz_words():
    text = getLatestNews() + getTrendNews()
    return text
