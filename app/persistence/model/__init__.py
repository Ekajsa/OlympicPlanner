from app.persistence.db import Document, db


class User(Document):
    collection = db.users


class Event(Document):
    collection = db.events


class Schedule(Document):
    collection = db.schedules
