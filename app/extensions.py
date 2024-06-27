from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

mongo = PyMongo()

def init_app(app):#loading MONGO_URI from env and initializing databse
    load_dotenv()
    

    app.config['MONGO_URI'] = "mongodb://mongo:27017/ACTIONS"
    mongo.init_app(app)
