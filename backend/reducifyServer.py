from flask import Flask, jsonify, request
from flask_jwt import JWT, jwt_required, current_identity

from peewee import *
from db_manager import User, getShared
import datetime
from ReceiptParse import receiptToIngredients
from Recipes import getRecipes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lit_haxx3rs'
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=60 * 60) #Have the token last one hour
app.debug=True

#Authenticate Users when they login
def authenticate(username, password):

    print("Attempted to connect", username," ",password)


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
    return "Hello world"

@app.route('/postTest',methods=['GET', 'POST'])
def postTest():
     print(request.data)
     return request.data



# Should be protected
# When receives a GET request, returns JSON array of what's in the fridge
@app.route('/fridge')
@jwt_required()
def user_home():
    return current_identity.getFridge()

@app.route('/receipt', methods=['POST'])
@jwt_required()
def updateWithReceipt():

    out = request.json
    print(out["image"])
    items = receiptToIngredients(base64.decodestring(out["image"]))
    current_identity.updateFridge(items)
    return jsonify({"data":items})


@app.route('/recipes')
@jwt_required()
def serveRecipes():
    return jsonify({"data":getRecipes(current_identity.foodList())})

@app.route('/recipes/consume', methods=['POST'])
@jwt_required()
def consumeRecipe():
    usedRecipe = request.form.get("recipe")

@app.route('/shared')
@jwt_required()
def serveShared():
    return jsonify({"data":getShared(7)})
