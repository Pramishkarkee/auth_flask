from flask import Flask, request
from flask_pymongo import PyMongo
from data import user_args,mongo,jwt
from flask_restful import Resource, Api, reqparse
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required, get_jwt_identity,)

class RegisterUser(Resource):

    def post(self):
        try:
            args = user_args.parse_args()
            users = mongo.db.users
            if users.find_one({'email': args['email']}) == None:
                password = sha256.hash(args['password'])
                users.insert_one(
                    {'first_name': args['first_name'], 'last_name': args['last_name'], 'email': args['email'], 'password': password})
                return {'status': 'SUCCESS', 'message': "User {} successfully registered".format(users['first_name'])}, 201
            else:
                return {'status': 'ERROR', 'message': "User email exist"}, 201
        except Exception as e:
            return {'status': 'ERROR'}, 400

class LoginUser(Resource):

    def post(self):
        try:
            args = user_args.parse_args()
            user = mongo.db.users.find_one_or_404({'email': args['email']})
            if sha256.verify(args['password'], user['password']):
                access_token = create_access_token(identity=user['email'])
                return {'status': 'SUCCESS', 'message': "Successfully Loged In",
                        'access_token': access_token, }, 201
            else:
                return {'status': 'FAILED', 'message': "Failed Loged In"}, 400
        except Exception as e:
            print(e)
            return {'status': 'ERROR'}, 400


class GetUserData(Resource):
    decorators = [jwt_required()]
    def get(self):
        try:
            current_user = get_jwt_identity()
            user = mongo.db.users.find_one_or_404({'email': current_user})
            return {'status': 'SUCCESS',
                    'data': {
                        'id': str(user['_id']),
                        'first_name': user['first_name'],
                        'last_name': user['last_name'],
                        'email': user['email']
                    }}, 200
        except Exception as e:
            return {'status': 'ERROR'}, 400