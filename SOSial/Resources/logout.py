from flask import session, jsonify
from flask_restful import Resource


class UserLogout(Resource):
    def post(self):
        session.clear()
        return jsonify({"message": "User successfully logged out."})