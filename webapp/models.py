from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from webapp import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    rank = db.Column(db.Integer, nullable=False, default=0)

    team = db.Column(db.Integer, default=0) 
    company = db.Column(db.String(20), nullable=False, default='QTMA')
    position = db.Column(db.String(20), nullable=False, default='New Hire')
    linkedin = db.Column(db.String(100), nullable=False, default='https://www.linkedin.com')
    other_link = db.Column(db.String(100), nullable=False, default='https://www.google.com')

class Team(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
