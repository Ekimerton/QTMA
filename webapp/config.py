import os

class Config:
    # General app configs
    try:
        SECRET_KEY = os.environ['SECRET_KEY']
        DEBUG = False
    except:
        SECRET_KEY = 'test'
        DEBUG = True
    # Database configs
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db";
    SQLALCHEMY_TRACK_MODIFICATIONS = False;

