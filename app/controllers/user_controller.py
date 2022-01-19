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
        "password": "jkldfa",
        "date_created": "2021-01-17",
        "last_signin": "2021-01-18",
        "status": "online",
        "activated": "True",
        "avatar": "",
        "schedules": [
            {
                "schedule_name": "My first schedule",
                "events": [
                    {
                        "event_no": "104",  # Should be event numbers from mongodb
                        "priority_col": "1"
                    },
                    {
                        "event_no": "098",
                        "priority_col": "1"
                    },
                    {
                        "event_no": "086",
                        "priority_col": "2"
                    },
                    {
                        "event_no": "076",
                        "priority_col": "2"
                    }
                ]
            }
          ]
        }

    ur.create_user(user)
