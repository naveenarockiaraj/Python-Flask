from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# creates Flask object
app = Flask(__name__)

# configuration
app.config['SECRET_KEY'] = 'your secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# creates SQLALCHEMY object
db = SQLAlchemy(app)

from app import models
