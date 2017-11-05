import sqlite3
from db import db

class PhotoModel(db.Model):
    __tablename__ = 'photo'

    id = db.Column(db.Integer, primary_key=True)
    photo_id = db.Column(db.String(100))
    yelp_id = db.Column(db.String(100))

    def __init__(self, photo_id, yelp_id):
        self.photo_id = photo_id
        self.yelp_id = yelp_id

    def json(self):
        return {'photo_id': self.photo_id, 'yelp_id': self.yelp_id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_photo_yelp_id(cls, photo_id, yelp_id):
        return cls.query.filter_by(photo_id=photo_id).filter_by(yelp_id=yelp_id).first()


    @classmethod
    def find_by_photo_id(cls, photo_id):
        return cls.query.filter_by(photo_id=photo_id).first()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
