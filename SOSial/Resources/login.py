from flask import session, redirect, request, jsonify
from flask_restful import Resource
from bcrypt import checkpw
from marshmallow import ValidationError

from SOSial.Models.user import UserModel
from SOSial.Schemas.user import UserSchema


class UserLogin(Resource):
    def post(self):
        username = session.get("username", None)
        if username:
            return jsonify({"message": "User is already logged in."})
        else:
            json_data = request.get_json()
            user_schema = UserSchema()

            try:
                data = user_schema.load(json_data, partial=True).data
            except ValidationError as err:
                return jsonify("message", err.messages)

            user = UserModel.fetch_using_username(data.username)
            if user:
                if checkpw(data.password.encode("utf-8"), user.password):
                    session["username"] = user.username
                    session["user_id"] = user.user_id
                    return jsonify({"message": "User successfully logged in."})
                else:
                    return jsonify({"message": "The username or password entered is incorrect."})
            else:
                return jsonify({"message": "The username or password entered is incorrect."}), 500


