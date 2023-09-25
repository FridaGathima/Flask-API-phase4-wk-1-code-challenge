#creating instance of the application in init.py

from flask import Flask
from flask_restful import Api # to convert the app into restful api
from api.models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

#create instance of the database
db.init_app(app)

api = Api(app)

#configure db url & secret key
# app.config['SECRET KEY'] = 'fbe881f521d60de3df806e887306d1dc'

from api import routes # to avoid circular importation when running projects
