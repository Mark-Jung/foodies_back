import os
import time
import sqlite3
from db import db

class WordModel(db.Model):
    __tablename__ = 'words'

    name = db.Column(db.String(80), primary_key=True)
    link = db.Column(db.String(200))
    time = db.Column(db.Integer)

    def __init__(self, name, link, time):
        self.name = name
        self.link = link
        self.time = time

    def json(self):
        return {'name': self.name, 'link': self.link, 'time': self.time}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def get_link(self, name):
        # check if that object's link is "current" done
        # if so, return link done
        # if not, call autoscripts, return updated object.link
        now = int(time.time())
        then = self.time
        seconds = now - then
        if seconds > 21600:
            # run script
            pass
        return { 'link': self.link }
