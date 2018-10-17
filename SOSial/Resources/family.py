from flask import session, redirect, request, jsonify
from flask_restful import Resource
import pickle

from SOSial.Models.details import UserDetailModel

class UserFamily(Resource):
    def post(self):
        username = session.get("username", None)
        if username:
            json_data = request.get_json()
            user_id = session["user_id"]
            user_details = UserDetailModel.fetch_using_id(user_id=user_id)
            if user_details is None:
                user_details = UserDetailModel(user_id=user_id, location=json_data["location"], family=pickle.dumps(json_data["family"]))

            user_details.location = pickle.dumps(json_data["family"])
            user_details.save_to_db()
            return {"message": "Family updated."}, 200

        else:
            return {"message": "User not logged in."}, 401

