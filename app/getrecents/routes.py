from flask import Blueprint, jsonify,render_template
from ..extensions import mongo
from datetime import datetime, timedelta
from pymongo import DESCENDING

getrecents = Blueprint('getrecents', __name__, url_prefix='/getrecents')

def get_ordinal_suffix(day):
    if 10 <= day % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
    return suffix

@getrecents.route('/recent', methods=["GET"])
def get_recent_data():
    # Calculate the datetime 15 seconds ago from the current time
    fifteen_seconds_ago = datetime.now() - timedelta(seconds=15)
    
    collection = mongo.db.my_collection
    # Query MongoDB to find documents with timestamp greater than or equal to fifteen_seconds_ago
    recent_data = list(collection.find({'timestamp': {'$gte': fifteen_seconds_ago}}).sort('_id', DESCENDING))
    
    for data in recent_data:
        day = data['timestamp'].day
        suffix = get_ordinal_suffix(day)
        formatted_timestamp = data['timestamp'].strftime(f"%d{suffix} %B %Y - %-I:%M %p UTC")

        data['_id'] = str(data['_id'])
        data['timestamp'] = str(formatted_timestamp)
    
    return jsonify(recent_data), 200

@getrecents.route('/dashboard', methods=["GET"]) #rendering frontend html
def show_dashboard():
    return render_template('dashboard.html')