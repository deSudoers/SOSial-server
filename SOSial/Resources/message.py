from flask import session, request, jsonify
from flask_restful import Resource

from SOSial.Models.user import UserModel
from SOSial.Models.message import MessageModel


class Message(Resource):
    def put(self):
        username = session.get("username", None)
        if username:
            json_data = request.get_json()
            for value in json_data.values():
                if MessageModel.fetch_using_unique_key(value["unique_key"]) is None:
                    message = MessageModel(sender_id=value["sender_id"], receiver_id=value["receiver_id"], message=value["message"], unique_key=value["unique_key"])
                    try:
                        message.save_to_db()
                    except:
                        return {"message": "An error occurred while saving message."}, 500
            return {"message": "Messages saved."}, 200

        else:
            return {"message": "User not logged in."}, 401

    def post(self):
        username = session.get("username", None)
        if username:
            json_data = request.get_json()

            response_messages = []
            for value in json_data.values():
                messages = MessageModel.fetch_using_id(value)
                for message in messages:
                    user = UserModel.fetch_using_id(value)
                    response_messages.append({
                        "sender_name": user.first_name + " " + user.last_name,
                        "receiver_id": message.receiver_id,
                        "message": message.message
                                     })
            return {k: response_messages[k] for k in range(len(response_messages))}, 200

        else:
            return {"message": "User not logged in."}, 401

