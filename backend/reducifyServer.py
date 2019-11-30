from flask import Flask, jsonify, request
from flask_jwt import JWT, jwt_required, current_identity

from peewee import *
from db_manager import User

app = Flask(__name__)


#Authenticate Users when they login
def authenticate(username, password):
    user = User.get(User.username == username)
    if user.password.encode('utf-8') == password.encode('utf-8'):
        return user

#Will decode the JWT, be given a payload with user.id - should return the appropriate user
def identity(payload):
    user_id = payload["identity"]
    return User.get(User.id == user_id)

#Tell jwt which functions to use
jwt = JWT(app, authenticate, identity)


@app.route('/')
def hello_world():
    return 'Hello, World!'



#Should be protected
@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity
