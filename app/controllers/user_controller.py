from app.persistence.repository import user_repository as ur


def get_all_users():
    return ur.get_all_users()


def create_user():
    # Just to create a test user. Should be swapped against input from website later on.
    user = {
        "first_name": "Peps",
        "last_name": "Persson",
        "full_name": "Peps Persson",
        "e-mail": "peps@email.com",
        "password": "jklö",
        "date_created": "2021-01-17",
        "last_signin": "2021-01-18",
        "status": "online",
        "activated": "True",
        "avatar": ""
    }

    ur.create_user(user)
