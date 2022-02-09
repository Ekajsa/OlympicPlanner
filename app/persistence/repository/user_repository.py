import datetime

from app.persistence.model import User


# Do we need this?
def get_all_users():
    return User.all()


def create_user(user):
    User(user).save()


def get_user_by_email(email):
    user = User.find(email=email).first_or_none()
    return user


def add_step2(email, disciplines):
    user = get_user_by_email(email)
    date = datetime.datetime.now()
    name = f'Created {date}'
    user.schedules.schedule_name = name
    user.schedules.disciplines = disciplines
    user.save()
    return name


def add_step3(email, countries):
    user = get_user_by_email(email)
    user.schedules.countries = countries

    user.save()


