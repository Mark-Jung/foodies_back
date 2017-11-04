import os
import json
import time
import sqlite3
from db import db

class BusinessModel(db.Model):
    __tablename__ = 'business'

    name = db.Column(db.String(100), primary_key=True)
    address = db.Column(db.String(600))
    ratings = db.Column(db.String(10))
    price = db.Column(db.Integer)
    phone_number = db.Column(db.String(20))
    photo_ids = db.Column(db.String(10000))

    def __init__(self, name, address, ratings, price, phone_number):
        self.name = name
        self.address = address
        self.ratings = ratings
        self.price = price
        self.phone_number = phone_number
        self.photo_ids = ''

    def json(self):
        return {'name': self.name, 'words': self.words}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def get_words(self):
        return self.json();
