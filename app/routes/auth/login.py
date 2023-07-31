from flask import Flask,request,jsonify,Response
from flask_restful import reqparse, abort, Api, Resource
from app.models.user import User
from app.services.auth.login_service import LoginService
from flask_jwt_extended import create_access_token

class Login(Resource):
    def get(self):
        abort(404, message="page does not exist")
    
    def post(self):
        
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        
        
        userService = LoginService()
        user = userService.get_user_by_username(username)
        if isinstance(user,User)==False:
            return Response('{"msg": "Bad username or password"}', status=401, content_type='application/json')
            
        verify_password =  userService.verify_password(user,password)
        if verify_password==False:
            return Response('{"msg": "Bad username or password"}', status=401, content_type='application/json')
            
        # generate access_token
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
