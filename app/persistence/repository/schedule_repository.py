from app.persistence.model import Schedule


def get_all_schedules():
    return Schedule.all()


def create_schedule(schedule):
    Schedule(schedule).save()
