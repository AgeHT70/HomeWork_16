import os.path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


USER_PATH = os.path.join('.', 'data', 'users.json')
ORDER_PATH = os.path.join('.', 'data', 'orders.json')
OFFER_PATH = os.path.join('.', 'data', 'offers.json')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


