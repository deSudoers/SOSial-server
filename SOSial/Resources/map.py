from flask import session, request, jsonify
from flask_restful import Resource

from SOSial.Models.trigger import TriggerModel
from SOSial.Models.details import UserDetailModel

class Map(Resource):
    def get(self):

        users = UserDetailModel.fetch_all()
        triggered_users = []

        for user in users:
            lat, long = [float(val) for val in user.location.split(", ")]
            trigger = TriggerModel.fetch_using_location(lat, long)
            if trigger is not None:
                triggered_users.append([lat,long])

        return {k: triggered_users[k] for k in range(len(triggered_users))}, 200


