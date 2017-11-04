from flask_restful import Resource, reqparse
from models.business import BusinessModel
from models.photo import PhotoModel
import requests, json, random, ast

class Done(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('liked_photo_id',
        type=str,
        required=True,
        help="This field cannot be left blank: liked_photo_id"
    )
    parser.add_argument('liked_yelp_id',
        type=str,
        required=True,
        help="This field cannot be left blank: liked_yelp_id"
    )

    def post(self):
        data = Done.parser.parse_args()
        liked_yelp_id_list = data['liked_yelp_id'].split()
        liked_photo_id_list = data['liked_photo_id'].split()
        if len(liked_photo_id_list) != len(liked_yelp_id_list):
            return {"message": "liked_photo_id and liked_yelp_id lengths must match!"}, 400
        result = []

        for single_yelp_id, single_photo_id in zip(liked_yelp_id_list, liked_photo_id_list):
            result.append(BusinessModel.find_by_yelp_id(single_yelp_id).json(single_photo_id))

        return result, 200
