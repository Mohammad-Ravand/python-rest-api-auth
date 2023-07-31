from flask_restful import Resource
from flask import Flask, request,jsonify,Response
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import json
class UserList(Resource):
    
    # Protect a route with jwt_required, which will kick out requests
    # without a valid JWT present.
    @jwt_required()
    def get(self, user_id):
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        data = {"logged_in_as": current_user}
        return Response(json.dumps(data), status=200, content_type='application/json')

    # def put(self, user_id):
    #     user_id = request.form['data']
    #     return {user_id: user_id}