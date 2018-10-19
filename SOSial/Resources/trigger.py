from flask import session, request, jsonify
from flask_restful import Resource

from SOSial.Models.trigger import TriggerModel


class Trigger(Resource):
    def put(self):
        username = session.get("username", None)
        if username:
            json_data = request.get_json()
            latitude = int(float(json_data["latitude"]))
            longitude = int(float(json_data["longitude"]))
            trigger = TriggerModel.fetch_using_location(latitude, longitude)

            if trigger is None:
                trigger = TriggerModel(latitude=latitude, longitude=longitude)
                try:
                    trigger.save_to_db()
                except Exception as e:
                    print(e)
                    return {"message": "An error occurred while saving trigger."}, 500

            return {"message": "Trigger added."}, 200


        else:
            return {"message": "User not logged in."}, 401

    def post(self):
        username = session.get("username", None)
        if username:
            json_data = request.get_json()
            latitude = int(float(json_data["latitude"]))
            longitude = int(float(json_data["longitude"]))
            trigger = TriggerModel.fetch_using_location(latitude, longitude)

            if trigger is None:
                return {"triggered": "0"}, 200

            return {"triggered": "1"}, 200

        else:
            return {"message": "User not logged in."}, 401
