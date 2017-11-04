from flask_restful import Resource, reqparse
from models.business import BusinessModel

class Start(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('lat',
        type=float,
        required=True,
        help="This field cannot be left blank: lattitude"
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
