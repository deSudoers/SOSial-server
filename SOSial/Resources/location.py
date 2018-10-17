from flask import session, request, jsonify
from flask_restful import Resource

from SOSial.Models.details import UserDetailModel


class UserLocation(Resource):
    def post(self):
        username = session.get("username", None)
        if username:
            json_data = request.get_json()
            user_id = session["user_id"]
            user_details = UserDetailModel.fetch_using_id(user_id=user_id)
            if user_details is None:
                user_details = UserDetailModel(user_id=user_id, location=json_data["location"])

            user_details.location = json_data["location"]

            try:
                user_details.save_to_db()
            except:
                return {"message": "An error occurred while saving location."}, 500

            return {"message": "Location updated."}, 200

        else:
            return {"message": "User not logged in."}, 401

