from flask import Flask, render_template
from flask_restful import Api
from db import db

from resources.words import Words
from scraper.update_all import update_all

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.before_first_request
def fill_tables():
    update_all()

api.add_resource(Words, '/words/<string:name>')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True, threaded=True)
