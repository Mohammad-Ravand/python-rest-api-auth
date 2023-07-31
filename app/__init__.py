from flask import Flask, request,jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app = Flask(__name__)
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

api = Api(app)


# api.add_resource(login.Login, '/auth/<string:type>')


db_path = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'data', 'mydatabase.db')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

# Silence the deprecation warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# adding models
from app.models.user import User


# adding routes
from app.routes.auth import login,register
from app.routes.user.user import UserList
api.add_resource(login.Login, '/auth/login')
api.add_resource(register.Register, '/auth/register')
api.add_resource(UserList, '/user/<string:user_id>')



application = app