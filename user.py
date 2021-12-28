
from flask import Blueprint
from flask import request, url_for, redirect
import requests
import time
import json
user = Blueprint('user', __name__)

'''
users =  {"user_1": {"first_name": "John", "last_name": "Wick"},
           "user_2": {"first_name": "Cory", "last_name": "Tailor"}}

'''
users = {}


@user.route('/', methods=['POST', 'GET', 'PUT', 'UPDATE', ])
def login():
    if request.method == 'POST':
        '''
        POST - update  ‘users.json’ ,  body like {“user_1”: {“first_name”: “John”, “last_name”: “Wick”}},
        “SUCCESS” if file exist and user if unique return status code 200
        or “FILE NOT EXIST” if file not created return status code 400
        Or “USER ALREADY EXIST” if user is not unique return status code 400
        Or “BAD BODY” if Body in bad format (types, structure)  return status code 400
        '''
        request_data = request.get_json(force=True)
        for num_user in request_data.keys():
            if num_user not in users.keys():
                return json.dumps('USER ALREADY EXIST'), 400
            if not users:
                return json.dumps('FILE NOT EXIST'), 400

            for user_in_list in users.keys():
                if num_user == user_in_list:
                    first_name = request_data[num_user]['first_name']
                    last_name = request_data[num_user]['last_name']
                    if not first_name or not last_name:
                        return json.dumps('BAD BODY'), 400

                    users[num_user] = {'first_name': first_name, 'last_name': last_name}

        return json.dumps(users), 200



    elif request.method == 'PUT':
        '''
        PUT - create file ‘users.json’
        “SUCCESS” if file not exist return status code 200
        or “FILE ALREADY EXIST” if file was created return status code 400
        '''
        request_data = request.get_json(force=True)
        for num_user in request_data.keys():
            if users and users == {}:
                return json.dumps('FILE ALREADY EXIST'), 400

            first_name = request_data[num_user]['first_name']
            last_name = request_data[num_user]['last_name']

            result_up = [(num_user, {'first_name': first_name, 'last_name': last_name})]
            users.update(result_up)

        return json.dumps(users), 200



    elif request.method == 'GET':
        print(request.get_json())
        # return redirect(url_for('SUCCESS', name=user))
        return json.dumps(users), 200, {'ContentType': 'application/json'}

    elif request.method == 'UPDATE':
        '''
        UPDATE - update  ‘users.json’, update user info ,  body like {“user_1": {“first_name”: “John”, “last_name”: “Wick”}}
        “SUCCESS” if file exist and user exist return status code 200
        or “FILE NOT EXIST” if file not created return status code 400
        Or “USER NOT EXIST” if user is not unique return status code 400
        Or “BAD BODY” if Body in bad format (types, structure)  return status code 400
        '''
        request_data = request.get_json(force=True)
        for num_user in request_data.keys():
            if num_user not in users.keys():
                return json.dumps('USER ALREADY EXIST'), 400
            if not users:
                return json.dumps('FILE NOT EXIST'), 400

            for user_in_list in users.keys():
                if num_user == user_in_list:
                    first_name = request_data[user_in_list]['first_name']
                    last_name = request_data[user_in_list]['last_name']
                    if not first_name or not last_name:
                        return json.dumps('BAD BODY'), 400

                    users[num_user] = {'first_name': first_name, 'last_name': last_name}

        return json.dumps(users), 200

    elif request.method == 'DELETE':
        '''
        DELETE - update  ‘users.json’ delete user , params like (user_id=user_1)
        “SUCCESS” if file exist and user exist return status code 200
        or “FILE NOT EXIST” if file not created return status code 400
        Or “USER NOT EXIST” if user is not unique return status code 400
        Or “BAD PARAMS” if param in bad format return status code 400        
        '''
        request_data = request.get_json(force=True)
        for user_id in request_data.values():
            print(user_id)
            if user_id not in users.keys():
                return json.dumps('USER NOT EXIST'), 400
            if not users:
                return json.dumps('FILE NOT EXIST'), 400

            users.pop(user_id)

        return json.dumps(users), 200
