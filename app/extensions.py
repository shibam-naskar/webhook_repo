from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

mongo = PyMongo()

def init_app(app):#loading MONGO_URI from env and initializing databse
    load_dotenv()
    

    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    mongo.init_app(app)
