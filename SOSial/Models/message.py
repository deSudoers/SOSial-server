from SOSial import db


class MessageModel(db.Model):

    __tablename__ = "MessageModel"

    message_id = db.Column("MessageID", db.Integer, primary_key=True)
    sender_id = db.Column("SenderID", db.Integer)
    receiver_id = db.Column("ReceiverID", db.Integer)
    message = db.Column("Message", db.String(1000))

    def __init__(self, sender_id=None, receiver_id=None, message=None):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.message = message

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def fetch_using_id(cls, receiver_id):
        return cls.query.filter_by(receiver_id=receiver_id).all()

