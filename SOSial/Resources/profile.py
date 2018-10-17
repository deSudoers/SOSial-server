from flask import session, jsonify, request
from flask_restful import Resource
from SOSial.Models.user import UserModel
from SOSial.Schemas.user import UserSchema
from marshmallow import ValidationError


class UserProfile(Resource):
    def get(self):
        username = session.get("username", None)
        if username:
            user = UserModel.fetch_using_username(username)
            user_schema = UserSchema()
            return jsonify(user_schema.dump(user).data), 200
        else:
            return jsonify({"message": "User not logged in."}), 401

    def put(self):
        username = session.get("username", None)
        if username:
            user = UserModel.fetch_using_username(username)
            json_data = request.get_json()
            user_schema = UserSchema()

            try:
                data = user_schema.load(json_data, partial=True).data
            except ValidationError as err:
                return jsonify("message", err.messages)

            user.email = data.email
            user.password = data.password
            user.first_name = data.first_name
            user.last_name = data.last_name

            try:
                user.save_to_db()
            except:
                return {"message": "An error occurred while updating details.."}, 500

            return jsonify({"message": "User details updated."})
        else:
            return jsonify({"message": "User not logged in."})

    def delete(self):
        username = session.get("username", None)
        if username:
            user = UserModel.fetch_using_username(username)
            if user:
                try:
                    user.delete_from_db()
                except:
                    return jsonify({"message": "An error occurred while deleting."}), 500
                session.clear()
                return jsonify({"message": "User successfully deleted."})
            else:
                return jsonify({"message": "User doesn't exist."})
        else:
            return jsonify({"message": "User not logged in."})
