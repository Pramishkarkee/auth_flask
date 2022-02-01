from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from urllib.parse import quote
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (
    create_access_token, create_refresh_token, jwt_required, get_jwt_identity,)

from dotenv import load_dotenv
import os
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

# JWT Secret key
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")

app.config['MONGO_URI'] = os.getenv("DB_URL")
# Creating different objects
jwt = JWTManager(app)
api = Api(app)
mongo = PyMongo(app)

# Required arguments from Request for RegisterUser and LoginUser Resource
user_args = reqparse.RequestParser()
user_args.add_argument('first_name', type=str, help='First Name')
user_args.add_argument('last_name', type=str, help='Last Name')
user_args.add_argument(
    'email', type=str, help='Email is required', required=True)
user_args.add_argument('password', type=str,
                       help='Password is required', required=True)

jwt = JWTManager(app)
api = Api(app)
mongo = PyMongo(app)