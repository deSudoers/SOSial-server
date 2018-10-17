from  flask import session, redirect
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, ForeignKey

from SOSial import db


class UserDetailModel(db.Model):

    __tablename__ = "UserDetail"

    id = db.Column("id", db.Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('User.UserID'))
    user = relationship("UserModel", back_populates="details")
    location = db.Column("LastLocation", db.String(200))
    family = db.Column("Family", db.PickleType())

    def __init__(self, user_id=None, location=None, family=None):
        self.user_id = user_id
        self.location = location
        self.family = family

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def get_family_info(self):
        pass

    @classmethod
    def fetch_using_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()

