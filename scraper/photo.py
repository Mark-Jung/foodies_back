import requests, json, random
from bs4 import BeautifulSoup

def get_id(yelp_id):
    base_url = "https://www.yelp.com/biz_photos/" + yelp_id + "?"
    foodtab_url = base_url + "tab=food"

    response = requests.get(foodtab_url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    pic_board = soup.find('ul', {'class': 'photo-box-grid'})
    all_li = pic_board.find_all('li')
    result = []
    
    for x in range(0, 3):
        result.append(base_url + "select=" + all_li[x]['data-photo-id'])

    return result

def get_count(yelp_id):
    base_url = "https://www.yelp.com/biz_photos/" + yelp_id + "?"
    foodtab_url = base_url + "tab=food"

    response = requests.get(foodtab_url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    navigation = soup.find_all('li', {'class': 'tab-nav_item'})
    if navigation:
        food_count = str(navigation[1].find('span', {'class': 'tab-link_count'}).contents).strip('[]')
        stripped_food_count = food_count.strip("'()")

        return int(stripped_food_count)
    else:
        return 0
