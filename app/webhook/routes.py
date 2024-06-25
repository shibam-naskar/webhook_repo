from flask import Blueprint, request, jsonify
from app.extensions import mongo
from datetime import datetime

webhook = Blueprint('webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    data = request.get_json()
    event_type = request.headers.get('X-GitHub-Event') #getting event type grom heager
    # print(event_type)

    collection = mongo.db.my_collection

    
    
    if data:
        # seperating actions based on X-Github-Event header
        if(event_type=="pull_request"):

            pr_id = data['pull_request']['id']
            from_branch = data['pull_request']['head']['ref']
            to_branch = data['pull_request']['base']['ref']
            author = data['pull_request']['user']['login']
            merge = data['pull_request']['merged']


            # varring the field action based on if data.pull_request.merged
            pr_data = {
                'request_id': str(pr_id),
                'author': author,
                'action' :"MERGE" if merge else "PULL_REQUEST",
                'from_branch' : from_branch,
                'to_branch' : to_branch,
                'timestamp' : datetime.now()
            }

            #inserting to the database
            collection.insert_one(pr_data).inserted_id
        elif(event_type=="push" and data['commits'][0]['distinct']==True): #an aditional push is creating from merge ommiting it based on distinct field commits[0]
            
            commit_id = data['head_commit']['id']
            from_branch = str(data['ref']).split('/')[-1]
            to_branch = str(data['ref']).split('/')[-1]
            author = data['head_commit']['author']['name']

            pr_data = {
                'request_id': commit_id,
                'author': author,
                'action' :'PUSH',
                'from_branch' : from_branch,
                'to_branch' : to_branch,
                'timestamp' : datetime.now()
            }

            #data base insertion
            collection.insert_one(pr_data).inserted_id
        
        
        return jsonify({'success':True}), 200
    else:
        return jsonify({'success': False}), 400
