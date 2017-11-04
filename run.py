from app import app
from db import db
from scraper.update_all import update_all

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
