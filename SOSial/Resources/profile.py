from flask import session, jsonify, request
from flask_restful import Resource
from SOSial.Models.user import UserModel, UserDetailModel
from SOSial.Schemas.user import UserSchema
from marshmallow import ValidationError
import pickle

class UserProfile(Resource):
    def get(self):
        username = session.get("username", None)
        user_id = session.get("user_id", None)
        if username:
            user = UserModel.fetch_using_username(username)

            user_schema = UserSchema()
            user_data = user_schema.dump(user).data
            user_detail = UserDetailModel.fetch_using_id(user_id)

            family_id = []
            family_name = []
            family_email = []

            if user_detail:
                family = pickle.loads(user_detail.family)
                if family:
                    for member_id in family:
                        member = UserModel.fetch_using_id(member_id)
                        family_id.append(str(member.user_id))
                        family_email.append(member.email)
                        family_name.append(member.first_name + member.last_name)

            return {"user_id": user_data["user_id"],
                    "email": user_data["email"],
                    "mobile": user_data["mobile"],
                    "name": user_data["first_name"] + " " + user_data["last_name"],
                    "family_id": ",".join(family_id),
                    "family_email": ",".join(family_email),
                    "family_name": ",".join(family_name)
                    }, 200
        else:
            return {"message": "User not logged in."}, 401

    def put(self):
        username = session.get("username", None)
        if username:
            user = UserModel.fetch_using_username(username)
            json_data = request.get_json()
            user_schema = UserSchema()

            try:
                data = user_schema.load(json_data, partial=True).data
            except ValidationError as err:
                return {"message", err.messages}, 400

            user.email = data.email
            user.password = data.password
            user.first_name = data.first_name
            user.last_name = data.last_name

            try:
                user.save_to_db()
            except:
                return {"message": "An error occurred while updating details.."}, 500

            return {"message": "User details updated."}, 200
        else:
            return {"message": "User not logged in."}, 401

    def delete(self):
        username = session.get("username", None)
        if username:
            user = UserModel.fetch_using_username(username)
            if user:
                try:
                    user.delete_from_db()
                except:
                    return {"message": "An error occurred while deleting."}, 500
                session.clear()
                return {"message": "User successfully deleted."}
            else:
                return {"message": "User doesn't exist."}
        else:
            return {"message": "User not logged in."}
