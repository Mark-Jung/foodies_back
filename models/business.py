import os
import json
import time
import sqlite3
from db import db

class BusinessModel(db.Model):
    __tablename__ = 'business'

    yelp_id = db.Column(db.String(100), primary_key=True)
    address = db.Column(db.String(100))
    name = db.Column(db.String(100))
    rating = db.Column(db.String(10))
    price = db.Column(db.Integer)
    phone_number = db.Column(db.String(20))
    photo_ids = db.Column(db.String(10000))

    def __init__(self, name, address, yelp_id, rating, price, phone_number):
        self.name = name
        self.address = address
        self.yelp_id = yelp_id
        self.rating = rating
        self.price = price
        self.phone_number = phone_number
        self.photo_ids = ''

    def json(self, photo_id):
        return {
                'name': self.name,
                'price': self.price,
                'phone_number': self.phone_number,
                'address': self.address,
                'photo_id': photo_id
            }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_yelp_id(cls, yelp_id):
        return cls.query.filter_by(yelp_id=yelp_id).first()
