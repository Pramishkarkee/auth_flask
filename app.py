from flask_restful import Resource, Api, reqparse
from user import GetUserData,RegisterUser,LoginUser
from data import api,app
# api = data.api
# app =data.app

api.add_resource(GetUserData,'/getmydata')
api.add_resource(RegisterUser, '/register')
api.add_resource(LoginUser, '/login')

if __name__ == "__main__":
    # App level secret key
    app.secret_key = "\x00\xfb\xdfB\xbf\xcd\x7f|X\xcc\x81\x92U\x1c\xc7^\xe1\x99\xbb\xfd\x9b\x93\xe2\xd4"
    app.run(debug=True)