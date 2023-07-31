from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, request
from app.services.auth.login_service import LoginService
class Register(Resource):

    def put(self, todo_id):
        todo_id = request.form['data']
        return {todo_id: todo_id}
    
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('username')
        parser.add_argument('password')
        args = parser.parse_args()

        user = LoginService()
        user = user.create_user(args['username'],args['password'])
        print(user)
        return args, 201