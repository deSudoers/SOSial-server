from flask import session, request, jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import ValidationError

from SOSial.Models.user import UserModel
from SOSial.Schemas.user import UserSchema


class UserLogin(Resource):
    def post(self):
        username = session.get("username", None)
        if username:
            return {"message": "User is already logged in."}, 400
        else:
            json_data = request.get_json()
            user_schema = UserSchema()
            try:
                data = user_schema.load(json_data, partial=True).data
            except ValidationError as err:
                return "message", err.messages, 400

            user = UserModel.fetch_using_username(data.username)
            if user:
                if check_password_hash(user.password, data.password.encode("utf-8")):
                    session["username"] = user.username
                    session["user_id"] = user.user_id
                    return {"message": "User successfully logged in."}, 200
                else:
                    return {"message": "The username or password entered is incorrect."}, 400
            else:
                return {"message": "The username or password entered is incorrect."}, 400


