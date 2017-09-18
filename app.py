import os
from flask import Flask
from flask_restful import Api

from resources.image import Words

app = Flask(__name__)
api = Api(app)

api.add_resource(Image, '/<string:name>')

app.run(port=5000, debug=True)
