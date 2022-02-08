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
    user.personal_schedules.disciplines = disciplines
    user.save()


def add_step3(email, countries):
    user = get_user_by_email(email)
    user.personal_schedules.countries = countries
    date = datetime.datetime.now()
    user.personal_schedules.schedule_name = f'Created {date}'
    user.save()


