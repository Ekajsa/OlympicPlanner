from app.persistence.model import Event


def get_all_events():
    return Event.all()


def get_all_events_by_date(date):
    return Event.find(date=date)


# def create_event(event):
#     Event(event).save()

