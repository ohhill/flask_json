'''
get_all_users
GET - return all ‘users.json’
{json with users} if file exist return status code 200
or {empty json} if file not created or file is empty return status code 400

'''
from flask import Blueprint, request
from user import users
import json


all_user = Blueprint('all_user', __name__)
@all_user.route('/')

def login():
    if request.method == 'GET' and users != {}:

        print(request.get_json())
        return json.dumps(users), 200, {'ContentType': 'application/json'}

    else:
        return json.dumps(users), 400
