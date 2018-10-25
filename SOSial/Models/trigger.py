from SOSial import db


class TriggerModel(db.Model):

    __tablename__ = "TriggerModel"

    trigger_id = db.Column("TriggerID", db.Integer, primary_key=True)
    latitude = db.Column("Latitude", db.Integer)
    longitude = db.Column("Longitude", db.Integer)
    count = db.Column("Count", db.Integer)

    def __init__(self, latitude=None, longitude=None, count=None):
        self.latitude = latitude
        self.longitude = longitude
        self.count = count

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def fetch_using_id(cls, trigger_id):
        return cls.query.filter_by(trigger_id=trigger_id).first()

    def fetch_using_triggered(cls):
        return cls.query.all()


    @classmethod
    def fetch_using_location(cls, latitude, longitude):
        return cls.query.filter(latitude < (cls.latitude + 1), latitude > (cls.latitude - 1), longitude < (cls.longitude + 1), longitude > (cls.longitude - 1)).first()

