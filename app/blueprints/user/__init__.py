import json
from flask import Blueprint, redirect, url_for, render_template, request
from flask_login import logout_user, current_user

from app.controllers.user_controller import edit_user, add_step3, add_step2
from app.controllers.schedule_controller import create_all_schedules, set_shown_date


bp_user = Blueprint("bp_user", __name__)


# @bp_user.get("/")
# def user():
#     return render_template("user.html")

# Is this the same thing as restricted access in base_template?
@bp_user.before_request
def before_request():
    if not current_user.is_authenticated:
        return redirect(url_for('bp_open.index'))


@bp_user.get("/signout")
def signout_get():
    logout_user()
    return redirect(url_for("bp_open.index"))


@bp_user.get("/profile")
# @login_required
def profile_get():
    return render_template("profile.html")


@bp_user.post("/profile")
def profile_post():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    edit_user(first_name, last_name, email)
    return redirect(url_for("bp_user.profile_get"))


@bp_user.get("/create_schedule/step1")
# @login_required
def schedules_get():
    schedules = ["My first schedule", "My second schedule"]
    return render_template("create_schedule_step_1.html", schedules=schedules)


@bp_user.get("/create_schedule/step2")
def select_disciplines_get():
    disciplines = ["Alpine Skiing", "Biathlon", "Bobsleigh", "Cross-Country Skiing", "Curling", "Figure Skating", "Freestyle Skiing", "Ice Hockey", "Luge", "Nordic Combined", "Short Track Speed Skating", "Skeleton", "Ski Jumping", "Snowboard", "Speed Skating"]
    return render_template("create_schedule_step_2.html", disciplines=disciplines)


@bp_user.post("/create_schedule/step2")
def select_disciplines_post():
    disciplines = ["Alpine Skiing", "Biathlon", "Bobsleigh", "Cross-Country Skiing", "Curling", "Figure Skating", "Freestyle Skiing", "Ice Hockey", "Luge", "Nordic Combined", "Short Track Speed Skating", "Skeleton", "Ski Jumping", "Snowboard", "Speed Skating", "Ceremony"]
    chosen = []
    for discipline in request.form:
        if discipline in disciplines:
            chosen.append(discipline)
    print()
    # print('Are we ever here 1?')
    email = current_user.email

    # print('Are we ever here 2?')
    # the_list = request.form["discipline"]
    # print('Are we ever here 3?')
    # disciplines = json.loads(the_list)
    # print('Are we ever here 4?')
    # app_step2 adds schedule_name and disciplines in db but returns only schedule_name, needed for step 3
    schedule_name = add_step2(email, chosen)

    return redirect(url_for('bp_user.select_countries_get', schedule_name=schedule_name))  # , schedule_name


@bp_user.get("/create_schedule/step3")
def select_countries_get():
    schedule_name = request.args['schedule_name']
    return render_template("create_schedule_step_3.html", schedule_name=schedule_name)


@bp_user.post("/create_schedule/step3")
def select_countries_post():
    email = current_user.email
    the_list = request.form["theList"]
    schedule_name = request.form['schedule_name']
    countries = json.loads(the_list)

    print()
    add_step3(email, schedule_name, countries)
    return redirect(url_for("bp_user.filtered_schedule_get"))


@bp_user.get("/create_schedule/step4")
# @login_required
def filtered_schedule_get():
    schedules, personal_schedules = create_all_schedules()
    # personal_schedule = create_empty_personal_schedule()
    return render_template("create_schedule_step_4.html", schedules=schedules, personal_schedules=personal_schedules)


@bp_user.post("/create_schedule/step4")
def filtered_schedule_post():
    chosen_countries = request.json
    return redirect(url_for("bp_user.filtered_schedule_get"))


@bp_user.get("/my_schedule")
# @login_required
def my_schedules_get():
    _, personal_schedule = create_all_schedules()  # Should be replaced by function to get a personal schedule from the database
    shown_date = set_shown_date()
    return render_template("my_schedule.html", personal_schedule=personal_schedule, shown_date=shown_date)


@bp_user.post("/my_schedule/")
# @login_required
def my_schedules_post():
    _, personal_schedule = create_all_schedules()  # Should be replaced by function to get a personal schedule from the database
    date_action = request.form.get("date_action")
    shown_date = request.form.get("shown_date")
    new_shown_date = set_shown_date(shown_date, date_action)
    return render_template("my_schedule.html", personal_schedule=personal_schedule, shown_date=new_shown_date)
