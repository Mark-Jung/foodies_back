from flask_restful import Resource, reqparse
from models.business import BusinessModel
from models.photo import PhotoModel
import requests, json, random, ast
from scraper.photo import get_id, get_count

TOKEN = 'A1Xn64Z9lcm2Hm5a1IfPTwSndnPyKG_GH5IlbKW7g8L2oLkHu-jE8RJVKprnNjNNiIKaUI7Fs5bzEH7s1eGJxuLvY7iZrQYUmmvpgzNAVbficRLxXyW_wQlanfr7WXYx'

# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search?'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
TOKEN_PATH = '/oauth2/token'
GRANT_TYPE = 'client_credentials'

class Start(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('lat',
        type=float,
        required=True,
        help="This field cannot be left blank: latitude"
    )

    parser.add_argument('long',
        type=float,
        required=True,
        help="This field cannot be left blank: longitude"
    )

    parser.add_argument('low_price',
        type=int,
        required=True,
        help="This field cannot be left blank: low_price"
    )

    parser.add_argument('high_price',
        type=int,
        required=True,
        help="This field cannot be left blank: high_price"
    )

    parser.add_argument('radius',
        type=int,
        required=True,
        help="This field cannot be left blank: radius"
    )


    def post(self):
        """
        receives longitude, lattitude, price, and range
        needs to make call to yelp.
        save each business to the db
        scrape and save
        return objects in form url, name
        """
        data = Start.parser.parse_args()
        if data["low_price"] < 1 or data["low_price"] > 4:
            return {"message": "price should be in range of 1 to 4"}, 400
        if data["high_price"] < 1 or data["high_price"] > 4:
            return {"message": "price should be in range of 1 to 4"}, 400
        price_range = ''
        for price in range(data['low_price'], data['high_price']):
            price_range += (str(price) + ', ')
        price_range += str(data['high_price'])
        url_params = {
            'term': 'restaurants',
            'latitude': data['lat'],
            'longitude': data['long'],
            'price': price_range,
            'limit': 15,
            'radius': data['radius']
        }
        headers = {
            'Authorization': 'Bearer %s' % TOKEN,
        }
        url = API_HOST + SEARCH_PATH
        response = requests.request('GET', url, headers=headers, params=url_params)
        if response is None:
            return {"message": "Yelp api call went wrong"}, 500

        try:
            businesses = response.json()['businesses']
        except:
            return response.json(), 500

        unrandomized = []
        for each in businesses:
            business = BusinessModel.find_by_yelp_id(each['id'])
            if business is None:
                address = '\n'.join(each['location']['display_address']).strip('[]')
                business = BusinessModel(each['name'], address, each['id'], each['rating'], each['price'], each['display_phone'])
                print("new! " + business.yelp_id)
                photo_ids = get_id(business.yelp_id)
                print("done scraping photo urls!")

                for x in range(0, 3):
                    photomodel = PhotoModel(photo_ids[x], business.yelp_id)
                    photomodel.save_to_db()
                print("done saving photo urls to db!")
                business.photo_ids = str(photo_ids)
                business.save_to_db()
            for x in range(0, 3):
                unrandomized.append(ast.literal_eval(business.photo_ids)[x])
        randomized = []
        for x in range(0, 30):
            photo_id = unrandomized[random.randint(0, 30)]
            randomized.append(PhotoModel.find_by_photo_id(photo_id).json())
        return randomized
