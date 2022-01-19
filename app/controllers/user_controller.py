import datetime

from flask_login import login_user
from werkzeug.security import check_password_hash, generate_password_hash

from app.persistence.repository import user_repository as ur, user_repository


def get_all_users():
    return ur.get_all_users()


def create_user(first_name, last_name, email, password):
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": f"{first_name} {last_name}",
        "e-mail": email,
        "password": generate_password_hash(password),
        "date_created": datetime.datetime.now(),
        "last_signin": None,
        "status": "offline",
        "activated": False,
        "avatar": f"https://eu.ui-avatars.com/api/?name={first_name}+{last_name}&background=random"
    }

    ur.create_user(user)


def get_user_by_email(email):
    return user_repository.get_user_by_email(email)


def verify_user(email, password):
    user = user_repository.get_user_by_email(email)
    if user is None:
        return False

    return check_password_hash(user.password, password)


def signin_user(email):
    user = get_user_by_email(email)
    if user is not None:
        login_user(user)
        user.last_signin = datetime.datetime.now()
        user.save()

