from app.persistence.model import User


# Do we need this?
def get_all_users():
    return User.all()


def create_user(user):
    User(user).save()


def get_user_by_email(email):
    user = User.find(email=email).first_or_none()
    return user


def add_country(email, country, schedule_name):
    user = get_user_by_email(email)
    if len(user.personal_schedules) == 0:
        user.personal_schedules.schedule_name = "First"
    if user.personal_schedules.schedule_name == "First":
        user.personal_schedules.countries.append(country)



