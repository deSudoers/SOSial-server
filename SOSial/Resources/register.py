from flask import session, request, jsonify
from flask_restful import Resource
from bcrypt import hashpw, gensalt
from marshmallow import ValidationError

from SOSial.Models.user import UserModel
from SOSial.Schemas.user import UserSchema
from SOSial.Models.details import UserDetailModel


class UserRegister(Resource):
    def post(self):
        json_data = request.get_json()

        user_schema = UserSchema()

        try:
            data = user_schema.load(json_data).data
        except ValidationError as err:
            return jsonify({"message": err.messages})

        hashed = hashpw(data.password.encode("utf-8"), gensalt())
        user = UserModel.fetch_using_username(data.username)

        if user is None:
            user = UserModel.fetch_using_email(data.email)

            if user is None:
                try:
                    data.password = hashed
                    data.save_to_db()
                except:
                    return {"message": "An error occurred while registering."}, 500

                return jsonify({"message": "User successfully registered."})
            else:
                return {"message": "A user with the same email already exists."}, 500
        else:
            return {"message": "A user with the same username already exists."}, 500
