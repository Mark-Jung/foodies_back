import os
from flask import send_file
from flask_restful import Resource, reqparse
from models.words import WordModel

class Words(Resource):
    def get(self, name):
        message = name
        return {'message': message }
