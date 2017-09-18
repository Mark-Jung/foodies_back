import os
from flask import Flask
from flask_restful import Api

from resources.words import Words

app = Flask(__name__)
api = Api(app)

api.add_resource(Words, '/words/<string:name>' )

app.run(port=5000, debug=True)
