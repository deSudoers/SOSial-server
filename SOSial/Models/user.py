from  flask import session, redirect
from datetime import datetime
import functools
from sqlalchemy.orm import relationship
from SOSial.Models.details import UserDetailModel


from SOSial import db


class UserModel(db.Model):

    __tablename__ = "User"

    user_id = db.Column("UserID", db.Integer, primary_key=True)
    username = db.Column("Username", db.String(80))
    password = db.Column("Password", db.String(300))
    first_name = db.Column("FirstName", db.String(80))
    last_name = db.Column("LastName", db.String(80))
    email = db.Column("Email", db.String(80))
    mobile = db.Column("Mobile", db.String(80))
    dtm_added = db.Column("DtmAdded", db.DateTime, default=datetime.utcnow)
    details = relationship("UserDetailModel", uselist=False, back_populates="user")

    def __init__(self, username=None, password=None, first_name=None, last_name=None, email=None, mobile=None):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile = mobile
        self.dtm_dded = datetime.utcnow()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def fetch_using_username(cls, username):
        return cls.query.filter_by(username=username).first()


    @classmethod
    def fetch_using_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def fetch_using_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()

    @classmethod
    def fetch_all(cls):
        return cls.query.all()
