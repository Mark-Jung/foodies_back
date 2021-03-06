from flask import Flask, render_template
from flask_restful import Api
from db import db

from resources.start import Start
from resources.done import Done

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Start, '/api/start')
api.add_resource(Done, '/api/done')



if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=80, debug=True)
