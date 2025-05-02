# config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:micah7:8@localhost/bananaai_new'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 


