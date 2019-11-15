from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from webapp.config import Config
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Reading configs from config file
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'main.login'
login_manager.login_message_category = 'info'

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

# Importing route handlers for main routes and error routes
from webapp.main.routes import main
from webapp.errors.handlers import errors
app.register_blueprint(main)
app.register_blueprint(errors)
