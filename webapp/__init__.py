from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from webapp.config import Config

# Reading configs from config file
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Importing route handlers for main routes and error routes
from webapp.main.routes import main
#from webapp.errors.handlers import errors
app.register_blueprint(main)
#app.register_blueprint(errors)
