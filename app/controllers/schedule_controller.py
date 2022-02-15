import datetime

import pytz
from tzlocal import get_localzone

from app.controllers.event_controller import get_all_events_by_date
from app.controllers.user_controller import get_chosen_countries_and_disciplines


def convert_time_slot_to_local(beijing_time_slots):
    converted_time_slots = []
    beijing_time_zone = pytz.timezone("Asia/Shanghai")

    for beijing_time in beijing_time_slots:
        beijing_time_with_time_zone = beijing_time_zone.localize(beijing_time)
        target_time = beijing_time_with_time_zone.astimezone(get_localzone())
        converted_time_slots.append(target_time.strftime("%H:%M"))

    return converted_time_slots


time_slots = ["08:30", "08:45", "09:00", "09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00",
              "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45",
              "14:00", "14:15", "14:30", "14:45", "15:00", "15:15", "15:30", "15:45", "16:00", "16:15", "16:30",
              "16:45", "17:00", "17:15", "17:30", "17:45", "18:00", "18:15", "18:30", "18:45", "19:00", "19:15",
              "19:30", "19:45", "20:00", "20:15", "20:30", "20:45", "21:00", "21:15", "21:30", "21:45", "22:00",
              "22:15", "22:30", "22:45", "23:00", "23:15", "23:30", "23:45"]

# Will this arbitrary date (to prevent the year to automatically be 1900) become a problem?
time_slots_with_date = ["2022-02-02 " + time for time in time_slots]
date_time_slots = [datetime.datetime.strptime(time, "%Y-%m-%d %H:%M") for time in time_slots_with_date]
local_time_slots = convert_time_slot_to_local(date_time_slots)


def create_empty_base_schedule():
    disciplines = ["Alpine skiing", "Biathlon", "Bobsleigh", "Cross-country skiing", "Curling", "Figure skating",
                   "Freestyle skiing", "Ice hockey", "Luge", "Nordic combined", "Short track speed skating",
                   "Skeleton", "Ski jumping", "Snowboard", "Speed skating", "Ceremony"]

    schedule = [["",
                 "<span class='alpine'>" + "Alpine skiing" + "</span>",
                 "<span class='biathlon'>" + "Biathlon" + "</span>",
                 "<span class='bobsleigh'>" + "Bobsleigh" + "</span>",
                 "<span class='cross-country'>" + "Cross-country skiing" + "</span>",
                 "<span class='curling'>" + "Curling" + "</span>",
                 "<span class='figure-skating'>" + "Figure skating" + "</span>",
                 "<span class='freestyle'>" + "Freestyle skiing" + "</span>",
                 "<span class='ice-hockey'>" + "Ice hockey" + "</span>",
                 "<span class='luge'>" + "Luge" + "</span>",
                 "<span class='noc'>" + "Nordic combined" + "</span>",
                 "<span class='short-track'>" + "Short track speed skating" + "</span>",
                 "<span class='skeleton'>" + "Skeleton" + "</span>",
                 "<span class='ski-jumping'>" + "Ski jumping" + "</span>",
                 "<span class='snowboard'>" + "Snowboard" + "</span>",
                 "<span class='speed-skating'>" + "Speed skating" + "</span>",
                 "<span class='ceremony'>" + "Ceremony" + "</span>"]]

    for i in range(len(local_time_slots)):
        row = ["<span class='time-slot'>" + local_time_slots[i] + "</span>"]
        for _ in range(len(disciplines)):
            row.append("")
        schedule.append(row)

    return schedule, disciplines, local_time_slots


def convert_times_to_nearest_quarter(hour, minute):
    time_nearest_quarter = hour

    if 53 <= int(minute) <= 59:
        if int(time_nearest_quarter[:2]) < 10:
            time_nearest_quarter = "0" + str(int(time_nearest_quarter[:2]) + 1) + ":"
        else:
            time_nearest_quarter = str(int(time_nearest_quarter[:2]) + 1) + ":"
        time_nearest_quarter += "00"

    elif int(minute) <= 7:
        time_nearest_quarter += "00"

    elif 8 <= int(minute) <= 22:
        time_nearest_quarter += "15"

    elif 23 <= int(minute) <= 37:
        time_nearest_quarter += "30"

    elif 38 <= int(minute) <= 52:
        time_nearest_quarter += "45"

    return time_nearest_quarter


def convert_beijing_time_to_local(event):
    beijing_date_time_start = datetime.datetime.strptime(f"{event.date} {event.local_start_time}:00.000000",
                                                         "%Y-%m-%d %H:%M:%S.%f")
    beijing_date_time_end = datetime.datetime.strptime(f"{event.date} {event.local_end_time}:00.000000",
                                                       "%Y-%m-%d %H:%M:%S.%f")

    beijing_time_zone = pytz.timezone("Asia/Shanghai")

    beijing_start_time_with_time_zone = beijing_time_zone.localize(beijing_date_time_start)
    target_time_start = beijing_start_time_with_time_zone.astimezone(get_localzone())

    beijing_end_time_with_time_zone = beijing_time_zone.localize(beijing_date_time_end)
    target_time_end = beijing_end_time_with_time_zone.astimezone(get_localzone())

    event.local_start_time = target_time_start.strftime("%Y-%m-%d %H:%M")
    event.local_end_time = target_time_end.strftime("%Y-%m-%d %H:%M")


# noinspection PyProtectedMember
def event_html(event):
    discipline_class = event.discipline.lower().replace(" ", "-") + "-event"
    event_html_string = f"<div class='event {discipline_class}' id='{event._id}'>"
    event_html_string += f"<span class='start-time'>{event.local_start_time[-5:]}</span>-<span class='end-time'>" \
                         f"{event.local_end_time[-5:]}</span>\n <span class='discipline'>{event.discipline}</span> "

    if len(event.sex) == 2:
        event_html_string += f"<span class='sex'>{event.sex[0]}, {event.sex[1]}</span>. "
    else:
        event_html_string += f"<span class='sex'>{event.sex}</span>. "

    if event.description == "":
        if len(event.competition_type) == 2:
            event_html_string += f"<span class='competition_type'>{event.competition_type[0].capitalize()}, " \
                                 f"{event.competition_type[1]}</span>."
        else:
            event_html_string += f"<span class='competition_type'>{event.competition_type.capitalize()}</span>. "
    else:
        event_html_string += f"<span class='description'>{event.description}</span>, "
        if len(event.competition_type) == 2:
            event_html_string += f"<span class='competition_type'>{event.competition_type[0]}, " \
                                 f"{event.competition_type[1]}</span>. "
        else:
            event_html_string += f"<span class='competition_type'>{event.competition_type}</span>. "

    if len(event.participating_countries) == 2:
        event_html_string += f"<p class='participating-countries'>{event.participating_countries[0]}-" \
                             f"{event.participating_countries[1]}</p>"

    event_html_string += "</div>"

    return event_html_string


def schedule_html(schedule, date):
    table_html = f"<div id='{date}'>"
    table_html += " <table> "
    for row in schedule:
        table_html += "<tr>"
        for cell in row:
            if schedule.index(row) == 0:
                if row.index(cell) == 0:
                    table_html += "<th class='time'>" + cell + "</th>"
                else:
                    table_html += "<th>" + cell + "</th>"
            else:
                if row.index(cell) == 0:
                    table_html += "<td class='time'>" + cell + "</td>"
                elif cell == "":
                    table_html += "<td>" + cell + "</td>"
                elif cell == "ROWSPAN":
                    pass
                else:
                    start_time = cell[0].local_start_time[-5:]
                    end_time = cell[0].local_end_time[-5:]
                    discipline = cell[0].discipline
                    td_class = discipline.lower().replace(" ", "-")
                    if cell[-1] is None:
                        table_html += f"<td class='{td_class}-event'>"
                    else:
                        table_html += f"<td class='{td_class}-event' rowspan ='{cell[-1]}'> "
                    for i in range(0, len(cell), 2):
                        if len(cell[i].sex) == 2:
                            sex = f"{cell[i].sex[0]}, {cell[i].sex[1]}"
                        else:
                            sex = cell[i].sex
                        if cell[i].description == "":
                            if len(cell[i].competition_type) == 2:
                                description_competition_type = f"{cell[i].competition_type[0].capitalize()}, " \
                                                               f"{cell[i].competition_type[1]}."
                            else:
                                description_competition_type = f"{cell[i].competition_type.capitalize()}. "
                        else:
                            description_competition_type = f"{cell[i].description}, "
                            if len(cell[i].competition_type) == 2:
                                description_competition_type += f"{cell[i].competition_type[0]}, " \
                                                               f"{cell[i].competition_type[1]}. "
                            else:
                                description_competition_type += f"{cell[i].competition_type}. "
                        if len(cell[i].participating_countries) == 2:
                            countries = f"{cell[i].participating_countries[0]}-{cell[i].participating_countries[1]}"
                        else:
                            countries = ""
                            for country in cell[i].participating_countries:
                                countries += f"{country}, "
                            countries = countries[:-2]
                        # noinspection PyProtectedMember
                        event_id = cell[i]._id
                        table_html += f"<div class='event' id='{event_id}'><a href='#' data-toggle='tooltip' " \
                                      f"title='{countries}'>{start_time}-" \
                                      f"{end_time} {discipline} {sex} {description_competition_type}<a/></div>"
                    table_html += "</td>"
        table_html += "</tr>"
    table_html += "</table>"
    table_html += "</div>"

    return table_html


# Version with outer join
def filter_events(date):
    events = get_all_events_by_date(date)
    countries, disciplines = get_chosen_countries_and_disciplines()
    filtered_events = []
    if len(countries) == 0 | len(disciplines) == 0:
        filtered_events = events
    else:
        for event in events:
            event_countries = [post.lower() for post in event.participating_countries]
            if event.discipline.lower() in disciplines:
                filtered_events.append(event)
            else:
                for country in event_countries:
                    if country in countries:
                        filtered_events.append(event)
    return filtered_events


def remove_columns(schedule):
    new_schedule = []
    empty_columns = {i: True for i in range(17)}

    for j in range(len(schedule[0])):
        if any(not "" == row[j] for row in schedule[1:]):
            empty_columns[j] = False

    for row in schedule:
        row_copy = []
        for j, cell in enumerate(row):
            if not empty_columns[j]:
                row_copy.append(row[j])
        new_schedule.append(row_copy)

    return new_schedule


def create_base_schedule(date):
    schedule, disciplines, converted_time_slots = create_empty_base_schedule()
    events = filter_events(date)
    for event in events:
        col_index = disciplines.index(event.discipline) + 1

        convert_beijing_time_to_local(event)

        start_time_nearest_quarter = convert_times_to_nearest_quarter(event.local_start_time[11:14],
                                                                      event.local_start_time[14:])
        row_start_index = converted_time_slots.index(start_time_nearest_quarter[-5:]) + 1

        end_time_nearest_quarter = convert_times_to_nearest_quarter(event.local_end_time[11:14],
                                                                    event.local_end_time[14:])
        row_end_index = converted_time_slots.index(end_time_nearest_quarter[-5:])

        if schedule[row_start_index][col_index] != "":
            try:
                schedule[row_start_index][col_index].append(event_html(event))
            except AttributeError:
                pass

        else:
            schedule[row_start_index][col_index] = [event_html(event)]

        row_span = row_end_index - row_start_index + 1
        if row_span == 0:
            row_span = 1

        if row_end_index == row_start_index:
            row_span = None

        try:
            schedule[row_start_index][col_index].append(str(row_span))
        except AttributeError:
            pass

        row_index = row_start_index + 1
        while row_index <= row_end_index:
            schedule[row_index][col_index] = "ROWSPAN"
            row_index += 1

    schedule = remove_columns(schedule)

    return schedule_html(schedule, date)


def create_empty_personal_schedule(date):
    schedule = [["",
                 "<span class='first-prio'>" + "First priority" + "</span>",
                 "<span class='second-prio'>" + "Second priority" + "</span>",
                 "<span class='third-prio'>" + "Third priority" + "</span>",
                 "<span class='fourth-prio'>" + "Fourth priority" + "</span>",
                 "<span class='fifth-prio'>" + "Fifth priority" + "</span>"]]

    for i in range(len(local_time_slots)):
        row = ["<span class='time-slot'>" + local_time_slots[i] + "</span>"]
        for _ in range(len(schedule[0]) - 1):
            row.append("")
        schedule.append(row)

    return schedule_html(schedule, date)


def create_all_schedules():
    all_day_schedules = []
    all_personal_schedules = []
    for i in range(2, 21):
        date = "2022-02-"
        if i < 10:
            date += "0" + str(i)
        else:
            date += str(i)
        base_schedule = create_base_schedule(date)
        all_day_schedules.append((date, base_schedule))
        personal_schedule = create_empty_personal_schedule(date)
        all_personal_schedules.append(("<p class='schedule-date'>" + date + "</p>", personal_schedule))
    return all_day_schedules, all_personal_schedules


def set_shown_date(shown_date="", date_action=""):
    if shown_date == "":
        shown_date = datetime.datetime.today().strftime("%Y-%m-%d")
        return shown_date

    date_strings = ["2022-02-02", "2022-02-03", "2022-02-04", "2022-02-05", "2022-02-06",
                    "2022-02-07", "2022-02-08", "2022-02-09", "2022-02-10", "2022-02-11",
                    "2022-02-12", "2022-02-13", "2022-02-14", "2022-02-15", "2022-02-16",
                    "2022-02-17", "2022-02-18", "2022-02-19", "2022-02-20"]
    min_index = 0
    max_index = len(date_strings) - 1
    shown_date_index = date_strings.index(shown_date)

    if date_action == "Next":
        shown_date_index = min(shown_date_index + 1, max_index)
        shown_date = date_strings[shown_date_index]
        return shown_date
    elif date_action == "Previous":
        shown_date_index = max(shown_date_index - 1, min_index)
        shown_date = date_strings[shown_date_index]
        return shown_date
    elif date_action == "First day":
        shown_date = date_strings[min_index]
        return shown_date
    elif date_action == "Last day":
        shown_date = date_strings[max_index]
        return shown_date
    elif date_action == "Today":
        shown_date = datetime.datetime.today().strftime("%Y-%m-%d")
        return shown_date
    else:
        return shown_date
