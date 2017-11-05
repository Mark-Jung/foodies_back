import requests, json, random
from bs4 import BeautifulSoup

def get_id(yelp_id):
    base_url = "https://www.yelp.com/biz_photos/" + yelp_id
    # foodtab_url = base_url + "tab=food"

    response = requests.get(base_url)
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
    result = []
    for temp in soup.find_all('ul', class_='photo-box-grid'):
        for div in soup.find_all('div', class_='photo-box'):
            for image in soup.find_all('img', class_='photo-box-img'):
                result.append(image.get('src'));
    length = len(result)
    print("The " + yelp_id + "has " + length + " many pictures!")
    final=[]
    for i in range(0, 3):
      index = random.randint(0,length-1)
      final.append(result[index])
    return final

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
