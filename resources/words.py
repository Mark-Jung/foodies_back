import os
from flask import send_file
from flask_restful import Resource, reqparse
from models.image import ImageModel

class Words(Resource):
    def get(self, name):
        return {'message': 'testmothi'}
