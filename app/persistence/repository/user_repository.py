from app.persistence.model import User


def get_all_users():
    return User.all()


def create_user(user):
    User(user).save()
