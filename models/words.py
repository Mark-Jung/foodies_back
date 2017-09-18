import os
import boto3


class WordModel():
    def __init__(self, name, link):
        self.name = name
        self.link = link
