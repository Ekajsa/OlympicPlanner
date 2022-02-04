from app.persistence.repository import event_repository as er


def get_all_events():
    return er.get_all_events()


def get_all_events_by_date(date):
    return er.get_all_events_by_date(date)
