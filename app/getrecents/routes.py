from flask import Blueprint, jsonify,render_template
from ..extensions import mongo
from datetime import datetime, timedelta
from pymongo import DESCENDING

getrecents = Blueprint('getrecents', __name__, url_prefix='/getrecents')

@getrecents.route('/recent', methods=["GET"])
def get_recent_data():
    # Calculate the datetime 15 seconds ago from the current time
    fifteen_seconds_ago = datetime.utcnow() - timedelta(seconds=15)
    
    collection = mongo.db.my_collection  # Replace with your actual collection name
    # Query MongoDB to find documents with timestamp greater than or equal to fifteen_seconds_ago
    recent_data = list(collection.find({'timestamp': {'$gte': fifteen_seconds_ago}}).sort('_id', DESCENDING))
    
    for data in recent_data:
        data['_id'] = str(data['_id'])

    print(recent_data)
    
    return jsonify(recent_data), 200

@getrecents.route('/dashboard', methods=["GET"]) #rendering frontend html
def show_dashboard():
    return render_template('dashboard.html')