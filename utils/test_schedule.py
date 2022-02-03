import datetime
import pytz
from tzlocal import get_localzone  # $ pip install tzlocal


from app import create_app
import dotenv

dotenv.load_dotenv()
create_app()

from app.controllers.schedule_controller import create_empty_schedule, create_schedule
from app.controllers.event_controller import get_all_events_by_date


def convert_string_to_date_time(the_event):
    beijing_date_time_start = datetime.datetime.strptime(f"{the_event.date} {the_event.local_start_time}:00.000000",
                                                         "%Y-%m-%d %H:%M:%S.%f")
    beijing_date_time_end = datetime.datetime.strptime(f"{the_event.date} {the_event.local_end_time}:00.000000",
                                                       "%Y-%m-%d %H:%M:%S.%f")

    beijing_time_zone = pytz.timezone("Asia/Shanghai")

    beijing_start_time_with_time_zone = beijing_time_zone.localize(beijing_date_time_start)
    target_time_start = beijing_start_time_with_time_zone.astimezone(get_localzone())

    beijing_end_time_with_time_zone = beijing_time_zone.localize(beijing_date_time_end)
    target_time_end = beijing_end_time_with_time_zone.astimezone(get_localzone())

    the_event.local_start_time = target_time_start.strftime("%Y-%m-%d %H:%M")
    the_event.local_end_time = target_time_end.strftime("%Y-%m-%d %H:%M")

    # print("Beijing:", beijing_date_time_start)
    # print("My time:", the_event.local_start_time)
    # print(the_event.local_end_time)


events = get_all_events_by_date("2022-02-20")
for event in events:
    convert_string_to_date_time(event)
    # print("Starts: ", event.local_start_time)
    # print("Ends: ", event.local_end_time)


# empty_schedule, disciplines, time_slots = create_empty_schedule()
# all_day_schedules = []
#
# for i in range(2, 21):
#     date = "2022-02-"
#     if i < 10:
#         date += "0" + str(i)
#     else:
#         date += str(i)
#     #print(date)
#     day_schedule = create_schedule(date, empty_schedule, disciplines, time_slots)
#     # for row in day_schedule:
#     #     print(row)
#     all_day_schedules.append(day_schedule)
# for schedule in all_day_schedules:
#     for row in schedule:
#         print(row)

# disciplines = ["Alpine skiing", "Biathlon", "Bobsleigh", "Cross-country skiing", "Curling", "Figure skating",
#                "Freestyle skiing", "Ice hockey", "Luge", "Nordic combined", "Short track speed skating", "Skeleton",
#                "Ski jumping", "Snowboard", "Speed skating", "Ceremony"]

def convert_time_slot_to_local(beijing_time_slots):
    local_time_slots = []
    beijing_time_zone = pytz.timezone("Asia/Shanghai")

    for beijing_time in beijing_time_slots:
        beijing_time_with_time_zone = beijing_time_zone.localize(beijing_time)
        target_time = beijing_time_with_time_zone.astimezone(get_localzone())
        local_time_slots.append(target_time.strftime("%H:%M"))

    return local_time_slots

time_slots = ["08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00",
              "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45",
              "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30",
              "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15",
              "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00",
              "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45"]

time_slots_with_date = ["2022-02-02 " + time for time in time_slots]
date_time_slots = [datetime.datetime.strptime(time, "%Y-%m-%d %H:%M") for time in time_slots_with_date]
local_slots = convert_time_slot_to_local(date_time_slots)
for time in local_slots:
    print(time)

# dynamic_time_slots = [datetime.datetime.strptime(time, "%H:%M").time() for time in time_slots]
# for time_slot in dynamic_time_slots:
#     print(str(time_slot)[:5])
#
# schedule = []
# for _ in range(len(time_slots)):
#     row = []
#     for _ in range(len(disciplines)):
#         row.append("")
#     schedule.append(row)
#
# for i in range(2, 21):
#     date = "2022-02-"
#     if i < 10:
#         date += "0" + str(i)
#     else:
#         date += str(i)
#     events = get_all_events_by_date(date)
#     for event in events:
#         col_index = disciplines.index(event.discipline)
#         start_time_nearest_quarter = event.local_start_time[:3]
#         if int(event.local_start_time[3:]) >= 53 or int(event.local_start_time[3:]) <= 7:
#             start_time_nearest_quarter += "00"
#         elif 8 <= int(event.local_start_time[3:]) <= 22:
#             start_time_nearest_quarter += "15"
#         elif 23 <= int(event.local_start_time[3:]) <= 37:
#             start_time_nearest_quarter += "30"
#         elif 38 <= int(event.local_start_time[3:]) <= 52:
#             start_time_nearest_quarter += "45"
#         row_index = time_slots.index(start_time_nearest_quarter)
#         schedule[row_index][col_index] = event
#
# for row in schedule:
#     print(row)
#