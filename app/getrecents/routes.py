from flask import Blueprint, jsonify
from ..extensions import mongo
from pymongo import DESCENDING

getrecents = Blueprint('getrecents', __name__, url_prefix='/getrecents')

@getrecents.route('/recent', methods=["GET"])
def get_recent_data():
    
    collection = mongo.db.my_collection
    recent_data = list(collection.find().sort('_id', DESCENDING))

    
    for data in recent_data:
        data['_id'] = str(data['_id'])

    return jsonify(recent_data), 200
