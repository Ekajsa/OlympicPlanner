# def event_html(event):
#     event_html_string = f"<div class='event' id='{event._id}'>"
#     event_html_string += f"<span class='start-time'>{event.local_start_time[-5:]}</span>-<span class='end-time'>" \
#                          f"{event.local_end_time[-5:]}</span>\n <span class='discipline'>{event.discipline}</span> "
#
#     if len(event.sex) == 2:
#         event_html_string += f"<span class='sex'>{event.sex[0]}, {event.sex[1]}</span>. "
#     else:
#         event_html_string += f"<span class='sex'>{event.sex}</span>. "
#
#     if event.description == "":
#         if len(event.competition_type) == 2:
#             event_html_string += f"<span class='competition_type'>{event.competition_type[0].capitalize()}, " \
#                                  f"{event.competition_type[1]}</span>."
#         else:
#             event_html_string += f"<span class='competition_type'>{event.competition_type.capitalize()}</span>. "
#     else:
#         event_html_string += f"<span class='description'>{event.description}</span>, "
#         if len(event.competition_type) == 2:
#             event_html_string += f"<span class='competition_type'>{event.competition_type[0]}, " \
#                                  f"{event.competition_type[1]}</span>. "
#         else:
#             event_html_string += f"<span class='competition_type'>{event.competition_type}</span>. "
#
#     event_html_string += "<p class='participating-countries'>"
#     if len(event.participating_countries) == 2:
#         event_html_string += f"{event.participating_countries[0]}-{event.participating_countries[1]}"
#     else:
#         for country in event.participating_countries:
#             event_html_string += f"{country}, "
#         event_html_string = event_html_string[:-2]
#     event_html_string += "</p>"
#
#     event_html_string += "</div>"
#
#     return event_html_string


# start_time = cell[0].partition("start-time'>")[2].partition("</span>")[0]
# end_time = cell[0].partition("end-time'>")[2].partition("</span>")[0]
# discipline = cell[0].partition("discipline'>")[2].partition("</span>")[0]
# td_class = discipline.lower().replace(" ", "-")
# # td_class = cell[0].partition("discipline'>")[2].partition('</span>')[0].lower().replace(" ", "-")
# if cell[-1] is None:
#     table_html += f"<td class='{td_class}-event'>"
# else:
#     table_html += f"<td class='{td_class}-event' rowspan ='{cell[-1]}'> "
# for i in range(0, len(cell), 2):
#     sex = cell[i].partition("sex'>")[2].partition("</span>")[0]
#     description = cell[i].partition("description'>")[2].partition("</span>")[0]
#     competition_type = cell[i].partition("competition_type'>")[2].partition("</span>")[0]
#     countries = cell[i].partition("countries'>")[2].partition('</p>')[0]
#     event_id = cell[i].partition("id='")[2].partition("'>")[0]
#     table_html += f"<div class='event' id='{event_id}'><a href='#' data-toggle='tooltip' " \
#                   f"title='{countries}'>{start_time}-" \
#                   f"{end_time} {discipline} {sex} {description} {competition_type}<a/></div>"


# if schedule[row_start_index][col_index] != "":
#     try:
#         schedule[row_start_index][col_index].append(event_html(event))
#     except AttributeError:
#         pass
#
# else:
#     schedule[row_start_index][col_index] = [event_html(event)]
