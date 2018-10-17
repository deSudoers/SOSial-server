from flask import session, request, jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash, check_password_hash


from marshmallow import ValidationError

from SOSial.Models.user import UserModel
from SOSial.Schemas.user import UserSchema


class UserRegister(Resource):
    def post(self):
        json_data = request.get_json()

        user_schema = UserSchema()

        try:
            data = user_schema.load(json_data).data
        except ValidationError as err:
            return {"message": err.messages}, 400

        hashed = generate_password_hash(data.password.encode("utf-8"))
        user = UserModel.fetch_using_username(data.username)

        if user is None:
            user = UserModel.fetch_using_email(data.email)

            if user is None:
                try:
                    data.password = hashed
                    data.save_to_db()
                except:
                    return {"message": "An error occurred while registering."}, 500

                session["username"] = user.username
                session["user_id"] = user.user_id
                return {"message": "User successfully registered."}, 200
            else:
                return {"message": "A user with the same email already exists."}, 400
        else:
            return {"message": "A user with the same username already exists."}, 400
