import requests
import lxml .html .usedoctest
from bs4 import BeautifulSoup, SoupStrainer

url = 'http://us.cnn.com/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

# headline
def getHeadline():
    for span in soup.find_all('span', class_="cd__headline-text"):
        print (span.text)

def get_cnn_words():
    return getHeadline;
