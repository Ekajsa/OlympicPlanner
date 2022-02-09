import datetime
from passlib.hash import argon2
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash

from app.persistence.repository import user_repository as ur


# Do we need this?
def get_all_users():
    return ur.get_all_users()


def create_user(first_name, last_name, email, password):
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": f"{first_name} {last_name}",
        "email": email,
        "password": argon2.using(rounds=12).hash(password),
        "date_created": datetime.datetime.now(),
        "last_signin": None,
        "status": "offline",
        "activated": False,
        "avatar": f"https://eu.ui-avatars.com/api/?name={first_name}+{last_name}&background=random",
        "schedules": [
            {
                "schedule_name": "",
                "disciplines": [],
                "countries": [],
                "events": []

            }
          ]
        }

    ur.create_user(user)


def get_user_by_email(email):
    return ur.get_user_by_email(email)


def verify_user(email, password):
    user = ur.get_user_by_email(email)
    if user is None:
        return False
    if user.password.startswith('pbkdf2:sha256'):
        verified = check_password_hash(user.password, password)
        if verified:
            user.password = argon2.using(rounds=12).hash(password)
            user.save()
        return verified
    return argon2.verify(password, user.password)


def signin_user(email):
    user = get_user_by_email(email)
    if user is not None:
        login_user(user)
        user.last_signin = datetime.datetime.now()
        user.save()


def edit_user(first_name, last_name, email):
    user = current_user
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    user.full_name = f"{user.first_name} {user.last_name}"
    if email:
        user.email = email
    user.save()
    signin_user(user.email)


def add_country(email, country, schedule_name):
    ur.add_country(email, country, schedule_name)


def add_step2(email, disciplines):
    return ur.add_step2(email, disciplines)


def add_step3(email, schedule_name, countries):
    ur.add_step3(email, schedule_name, countries)


