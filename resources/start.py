from flask_restful import Resource, reqparse
from models.business import BusinessModel
import requests, json

TOKEN = 'A1Xn64Z9lcm2Hm5a1IfPTwSndnPyKG_GH5IlbKW7g8L2oLkHu-jE8RJVKprnNjNNiIKaUI7Fs5bzEH7s1eGJxuLvY7iZrQYUmmvpgzNAVbficRLxXyW_wQlanfr7WXYx'

# API constants, you shouldn't have to change these.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
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

    parser.add_argument('price',
        type=int,
        required=True,
        help="This field cannot be left blank: price"
    )

    parser.add_argument('range',
        type=int,
        required=True,
        help="This field cannot be left blank: range"
    )


    def post(self):
        """
        receives longitude, lattitude, price, and range
        needs to make call to yelp.
        save each business to the db
        check if the business have url
        if not, scrape and save
        return objects in form url, name
        """
        data = Start.parser.parse_args()
        if 5 < data["price"] < 0:
            return {"message": "price should be in range of 1 to 5"}, 400
        url_params = {
            'term': 'restaurants',
            'latitude': data['lat'],
            'longitude': data['long'],
            'price': data['price'],
            'limit': 30
        }
        headers = {
            'Authorization': 'Bearer %s' % TOKEN,
        }
        url = API_HOST + SEARCH_PATH
        response = requests.request('GET', url, headers=headers, params=url_params)

        for each in response.json()['businesses']:
            if BusinessModel.find_by_name(each['name']) is None:
                address = '\n'.join(each['location']['display_address']).strip('[]')
                business = BusinessModel(each['name'], address, each['id'], each['rating'], each['price'], each['display_phone'])
                business.save_to_db()


        return {"result": BusinessModel.find_by_name('The Barn').address}



    # def get(self, name):
    #     # pass on name to models
    #     item = WordModel.find_by_name(name)
    #     if item is None:
    #         return {'message': 'Item not allowed. Check spelling.'}, 400
    #     elif item.path == '':
    #         return {'message': 'Sorry, the scraping script for this news organization is not working properly.'}, 500
    #     else:
    #         return send_file(item.path, mimetype='image/gif')
    #
    # def put(self, name):
    #     if name == 'update':
    #         update_all()
    #         return {'message': 'update success!'}
    #     else:
    #         return {'message': 'bad route. try again.'}, 400
