from flask import session, jsonify
from flask_restful import Resource


class UserLogout(Resource):
    def post(self):
        session.clear()
        return {"message": "User successfully logged out."}, 200