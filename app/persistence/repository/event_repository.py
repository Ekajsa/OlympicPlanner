from app.persistence.model import Event


def get_all_events():
    return Event.all()


def create_event(event):
    Event(event).save()
