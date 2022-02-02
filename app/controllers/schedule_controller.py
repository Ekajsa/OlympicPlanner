# Schedule_controller is probably not needed anymore, since schedule is inserted into user db
#
# from app.persistence.repository import schedule_repository as sr

from app.controllers.event_controller import get_all_events_by_date


def create_empty_schedule():
    disciplines = ["Alpine skiing", "Biathlon", "Bobsleigh", "Cross-country skiing", "Curling", "Figure skating",
                   "Freestyle skiing", "Ice hockey", "Luge", "Nordic combined", "Short track speed skating",
                   "Skeleton", "Ski jumping", "Snowboard", "Speed skating", "Ceremony"]
    time_slots = ["08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00",
                  "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45",
                  "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30",
                  "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15",
                  "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00",
                  "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45"]

    schedule = []
    for _ in range(len(time_slots)):
        row = []
        for _ in range(len(disciplines)):
            row.append("")
        schedule.append(row)

    return schedule, disciplines, time_slots


def create_schedule(date):
    schedule, disciplines, time_slots = create_empty_schedule()
    events = get_all_events_by_date(date)
    for event in events:
        col_index = disciplines.index(event.discipline)
        start_time_nearest_quarter = event.local_start_time[:3]

        if 53 <= int(event.local_start_time[3:]) <= 59:
            if int(start_time_nearest_quarter[:2]) < 10:
                start_time_nearest_quarter = str(int(start_time_nearest_quarter[:2]) + 1) + ":"
            else:
                start_time_nearest_quarter = str(int(start_time_nearest_quarter[:2]) + 1) + ":"
            start_time_nearest_quarter += "00"

        elif int(event.local_start_time[3:]) <= 7:
            start_time_nearest_quarter += "00"

        elif 8 <= int(event.local_start_time[3:]) <= 22:
            start_time_nearest_quarter += "15"

        elif 23 <= int(event.local_start_time[3:]) <= 37:
            start_time_nearest_quarter += "30"

        elif 38 <= int(event.local_start_time[3:]) <= 52:
            start_time_nearest_quarter += "45"

        row_index = time_slots.index(start_time_nearest_quarter)
        schedule[row_index][col_index] = event

    return schedule, disciplines, time_slots


# def create_schedules():
#     empty_schedule, disciplines, time_slots = create_empty_schedule()
#     all_day_schedules = []
#     for i in range(2, 21):
#         date = "2022-02-"
#         if i < 10:
#             date += "0" + str(i)
#         else:
#             date += str(i)
#         all_day_schedules.append(create_schedule(date, empty_schedule, disciplines, time_slots))
#     return all_day_schedules, disciplines, time_slots


# def get_all_schedules():
#     return sr.get_all_schedules()
#
#
# def create_schedule():
#     pass
#     sr.create_schedule(schedule)
