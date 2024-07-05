from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

mongo = PyMongo()

def init_app(app):#loading MONGO_URI from env and initializing databse
    load_dotenv()
    print(os.getenv('MONGO_URI'))

    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    mongo.init_app(app)