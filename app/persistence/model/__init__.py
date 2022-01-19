from app.persistence.db import Document, db


class User(Document):
    collection = db.users

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email


class Event(Document):
    collection = db.events


class Schedule(Document):
    collection = db.schedules
