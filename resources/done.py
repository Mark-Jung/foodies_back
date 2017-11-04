from flask_restful import Resource, reqparse
from models.business import BusinessModel
from models.photo import PhotoModel
import requests, json, random, ast

class Done(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('liked',
        type=str,
        required=True,
        help="This field cannot be left blank: liked"
    )

    def post(self):
        data = Done.parser.parse_args()
        result = data["liked"]

        return {"message": result}, 200
