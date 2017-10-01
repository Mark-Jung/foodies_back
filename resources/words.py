from flask_restful import Resource
from models.words import WordModel

class Words(Resource):

    # for testing
    # parser = reqparse.RequestParser()
    # parser.add_argument('words',
    #     type=str,
    #     required=True,
    #     help="This field cannot be blank."
    # )

    def get(self, name):
        # pass on name to models
        item = WordModel.find_by_name(name)
        if item is None:
            return {'message': 'Item not allowed. Check spelling.'}, 400
        return item.json()

    def post(self, name):
        item = WordModel.find_by_name(name)
        if item is None:
            word_cloud = WordModel(name, data['words'], timestamp)
            word_cloud.save_to_db()
            item = WordModel.find_by_name(name)
            return item.json(), 201
        return {'message': 'item already exists'}, 400
