from app.persistence.model import User


def get_all_users():
    return User.all()


def create_user(user):
    User(user).save()


def get_user_by_email(email):
    return User.find(email=email).first_or_none()
