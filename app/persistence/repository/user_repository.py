import datetime

from app.persistence.model import User


def create_user(user):
    User(user).save()


def get_user_by_email(email):
    user = User.find(email=email).first_or_none()
    return user


def add_step2(email, disciplines):
    user = get_user_by_email(email)
    date = datetime.datetime.now()
    name = f'Created {date}'
    num_of_schedules = len(user.schedules)
    new_schedule = {
            "schedule_name": name,
            "disciplines": disciplines,
            "countries": [],
            "events": []
    }
    user.schedules.append(new_schedule)
    user.save()
    return name


def add_step3(email, schedule_name, countries):
    user = get_user_by_email(email)
    for schedule in user.schedules:
        if schedule["schedule_name"] == schedule_name:
            schedule["countries"] = countries
    user.save()


def get_user_schedules(user):
    schedules = user.schedules
    return schedules
