import os

from datetime import timedelta
from flask import Flask, jsonify
from flask import send_from_directory
from flask_restful import Api
from flask_jwt import JWT

from db import db
from security import authenticate, identity as identity_function
from resources.home import Home
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__, static_folder='./front_react/build', static_url_path='')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app.secret_key = 'jose'
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] ='/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=18000)
# app.config['JWT_AUTH_USERNAME_KEY'] = 'email'  # key : email
jwt = JWT(app, authenticate, identity_function )  # /auth

@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return jsonify({
        'access_token' : access_token.decode('utf-8'),
        'user_id' : identity.id
    })

@jwt.jwt_error_handler
def customized_error_handler(error):
    return jsonify({
        'message':error.description,
        'code' : error.status_code
    }), error.status_code


# @app.before_first_request
# def create_tables():
#     db.create_all()

# @app.route('/')
# def index():
#     return app.send_static_file('index.html')

api.add_resource(UserRegister,'/register') #

api.add_resource(Home,'/') #

api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/park
api.add_resource(ItemList, '/items')  # http://127.0.0.1:5000/items

api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/store/<string:name>')


if __name__ == '__main__' :
    db.init_app(app)
    app.run(port=5000, debug=True)
