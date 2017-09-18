import os
import time
from flask import send_file
from flask_restful import Resource, reqparse
from models.words import WordModel

class Words(Resource):

    # for testing
    parser = reqparse.RequestParser()
    parser.add_argument('link',
        type=str,
        required=True,
        help="This field cannot be blank."
    )

    def get(self, name):
        # pass on name to models, if the name exists
        item = WordModel.find_by_name(name)
        if item is None:
            return {'message': 'Item not found. Check name.'}, 400
        else:
            return item.get_link(name)

    def post(self, name):
        item = WordModel.find_by_name(name)
        if item is None:
            data = Words.parser.parse_args()
            timestamp = int(time.time())
            word_cloud = WordModel(name, data['link'], timestamp)
            word_cloud.save_to_db()
            item = WordModel.find_by_name(name)
            return item.json(), 201
        return {'message': 'item already exists'}, 400
