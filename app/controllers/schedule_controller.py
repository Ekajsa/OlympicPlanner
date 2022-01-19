from app.persistence.repository import schedule_repository as sr


def get_all_schedules():
    return sr.get_all_schedules()


def create_schedule():
    # Just to create a test schedule. Should be swapped against input from website later on.
    schedule = {
        "schedule_name": "My first schedule",
        "events": [
            {
                "event_no": "104",  # Should be event numbers from mongodb
                "discipline": "Cross-country",
                "description": "15 km classic technique",
                "competition_type": "Final",
                "sex": "Men's",
                "date": "2022-02-16",
                "local_start_time": "15.00",
                "local_end_time": "16.35",
                "tv_channel": ["Channel 5"],
                "priority_col": "1"
            },
            {
                "event_no": "098",
                "discipline": "Cross-country",
                "description": "10 km classic technique",
                "competition_type": "Final",
                "sex": "Women's",
                "date": "2022-02-10",
                "local_start_time": "15.00",
                "local_end_time": "16.30",
                "tv_channel": ["Discovery Channel"],
                "priority_col": "1"
            },
            {
                "event_no": "086",
                "discipline": "Skating",
                "description": "Single Skating - Free Skating",
                "competition_type": "Final",
                "sex": "Men's",
                "date": "2022-02-10",
                "local_start_time": "09.37",
                "local_end_time": "13.27",
                "tv_channel": ["Channel 5"],
                "priority_col": "2"
            },
            {
                "event_no": "076",
                "discipline": "Skating",
                "description": "Single Skating - Short Program",
                "competition_type": "Prologue",
                "sex": "Men's",
                "date": "2022-02-08",
                "local_start_time": "09.22",
                "local_end_time": "13.30",
                "tv_channel": ["Discovery Channel"],
                "priority_col": "2"
            }
        ]
    }

    sr.create_schedule(schedule)
