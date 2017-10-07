from flask import send_file
from flask_restful import Resource
from models.words import WordModel
from scraper.update_all import update_all

class Words(Resource):

    def get(self, name):
        # pass on name to models
        item = WordModel.find_by_name(name)
        if item is None:
            return {'message': 'Item not allowed. Check spelling.'}, 400
        elif item.path == '':
            return {'message': 'Sorry, the scraping script for this news organization is not working properly.'}, 500
        else:
            return send_file(item.path, mimetype='image/gif')

    def put(self, name):
        if name == 'update':
            update_all()
            return {'message': 'update success!'}
        else:
            return {'message': 'bad route. try again.'}, 400
