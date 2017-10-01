import os
import json
import time
import sqlite3
from db import db

class WordModel(db.Model):
    __tablename__ = 'words'

    name = db.Column(db.String(80), primary_key=True)
    words = db.Column(db.String(19000))

    def __init__(self, name, words):
        self.name = name
        self.words = words

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
