from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '8bf453d6ee5d32678889844e83bb649f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# login_required definieren
login_manager.login_view = "login"
login_manager.login_message_category = "info"
login_manager.login_message = "Du musst angemeldet sein, um diese Seite sehen zu können."

from morpheus import routes