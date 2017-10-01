import requests
from bs4 import BeautifulSoup, SoupStrainer

url = 'http://us.cnn.com/'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html.parser")

# headline
def getHeadline():
    result = ''
    for span in soup.find_all('span', class_="cd__headline-text"):
        result = result + ' ' + a.text
    return result

def get_cnn_words():
    return getHeadline();
