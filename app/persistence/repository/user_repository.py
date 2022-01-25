from app.persistence.model import User


# Do we need this?
def get_all_users():
    return User.all()


def create_user(user):
    User(user).save()


def get_user_by_email(email):
    user = User.find(email=email).first_or_none()
    return user


def add_countries(email, countries):
    user = get_user_by_email(email)




