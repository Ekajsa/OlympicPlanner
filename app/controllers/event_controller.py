from app.persistence.repository import event_repository as er


def get_all_events():
    return er.get_all_events()


def get_all_events_by_date(date):
    return er.get_all_events_by_date(date)


def create_schedule():
    disciplines = ["Alpine skiing", "Biathlon", "Bobsleigh", "Cross-country skiing", "Curling", "Figure skating",
                   "Freestyle skiing", "Ice hockey", "Luge", "Nordic combined", "Short track speed skating",
                   "Skeleton", "Ski jumping", "Snowboard", "Speed skating"]
    time_slots = ["09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30",
                  "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15",
                  "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30", "16:45", "17:00",
                  "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15", "19:30", "19:45",
                  "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00", "22:15", "22:30",
                  "22:45", "23:00", "23:15", "23:30", "23:45"]


# def create_event():
#     # Just to create some test events. Should be swapped against input from website later on.
#     events = [
#         {
#             "event_no": "104",  # Should be event numbers from mongodb
#             "discipline": "Cross-country",
#             "description": "15 km classic technique",
#             "competition_type": "Final",
#             "sex": "Men's",
#             "date": "2022-02-16",
#             "local_start_time": "15.00",
#             "local_end_time": "16.35",
#             "tv_channel": ["Channel 5"],
#             "priority_col": "1"
#         },
#         {
#             "event_no": "098",
#             "discipline": "Cross-country",
#             "description": "10 km classic technique",
#             "competition_type": "Final",
#             "sex": "Women's",
#             "date": "2022-02-10",
#             "local_start_time": "15.00",
#             "local_end_time": "16.30",
#             "tv_channel": ["Discovery Channel"],
#             "participating_countries": []
#     },
#         {
#             "event_no": "086",
#             "discipline": "Skating",
#             "description": "Single Skating - Free Skating",
#             "competition_type": "Final",
#             "sex": "Men's",
#             "date": "2022-02-10",
#             "local_start_time": "09.37",
#             "local_end_time": "13.27",
#             "tv_channel": ["Channel 5"],
#             "participating_countries": []
#     },
#         {
#             "event_no": "076",
#             "discipline": "Skating",
#             "description": "Single Skating - Short Program",
#             "competition_type": "Prologue",
#             "sex": "Men's",
#             "date": "2022-02-08",
#             "local_start_time": "09.22",
#             "local_end_time": "13.30",
#             "tv_channel": ["Discovery Channel"],
#             "participating_countries": []
#         }
#     ]
#
#     for event in events:
#         er.create_event(event)
