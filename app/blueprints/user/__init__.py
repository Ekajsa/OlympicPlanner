import json
from flask import Blueprint, redirect, url_for, render_template, request
from flask_login import logout_user, current_user

from app.controllers import user_controller as uc
from app.controllers import schedule_controller as sc


bp_user = Blueprint("bp_user", __name__)


@bp_user.before_request
def before_request():
    if not current_user.is_authenticated:
        return redirect(url_for('bp_open.index'))


@bp_user.get("/signout")
def signout_get():
    logout_user()
    return redirect(url_for("bp_open.index"))


@bp_user.get("/profile")
def profile_get():
    return render_template("profile.html")


@bp_user.post("/profile")
def profile_post():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    uc.edit_user(first_name, last_name, email)
    return redirect(url_for("bp_user.profile_get"))


@bp_user.get("/create_schedule/step1")
def schedules_get():
    return render_template("create_schedule_step_1.html")


@bp_user.get("/create_schedule/step2")
def select_disciplines_get():
    disciplines = ["Alpine Skiing", "Biathlon", "Bobsleigh", "Cross-Country Skiing", "Curling", "Figure Skating",
                   "Freestyle Skiing", "Ice Hockey", "Luge", "Nordic Combined", "Short Track Speed Skating", "Skeleton",
                   "Ski Jumping", "Snowboard", "Speed Skating"]
    return render_template("create_schedule_step_2.html", disciplines=disciplines)


@bp_user.post("/create_schedule/step2")
def select_disciplines_post():
    disciplines = ["Alpine Skiing", "Biathlon", "Bobsleigh", "Cross-Country Skiing", "Curling", "Figure Skating",
                   "Freestyle Skiing", "Ice Hockey", "Luge", "Nordic Combined", "Short Track Speed Skating", "Skeleton",
                   "Ski Jumping", "Snowboard", "Speed Skating"]
    chosen = []
    for discipline in request.form:
        if discipline in disciplines:
            chosen.append(discipline)
    print()
    email = current_user.email
    schedule_name = uc.add_step2(email, chosen)

    return redirect(url_for('bp_user.select_countries_get', schedule_name=schedule_name))


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
    uc.add_step3(email, schedule_name, countries)
    return redirect(url_for("bp_user.filtered_schedule_get"))


@bp_user.get("/create_schedule/step4")
def filtered_schedule_get():
    schedules, personal_schedules = sc.create_all_schedules()
    shown_date = sc.set_shown_date()
    return render_template("create_schedule_step_4.html", schedules=schedules, personal_schedules=personal_schedules,
                           shown_date=shown_date)


@bp_user.post("/create_schedule/step4")
def step4_post():
    schedules, personal_schedules = sc.create_all_schedules()
    date_action = request.form.get("date_action")
    shown_date = request.form.get("shown_date")
    new_shown_date = sc.set_shown_date(shown_date, date_action)
    schedule_to_save = request.form.get("schedule_to_save")
    uc.save_personal_schedule(schedule_to_save)
    return render_template("create_schedule_step_4.html", schedules=schedules, personal_schedules=personal_schedules,
                           shown_date=new_shown_date)


@bp_user.get("/my_schedule")
def my_schedules_get():
    # _, personal_schedule = create_all_schedules()  # Should be replaced by function to get a personal schedule from the database
    personal_schedule = uc.get_saved_schedule()
    shown_date = sc.set_shown_date()
    return render_template("my_schedule.html", personal_schedule=personal_schedule, shown_date=shown_date)


@bp_user.post("/my_schedule/")
def my_schedules_post():
    # _, personal_schedule = sc.create_all_schedules()  # Should be replaced by function to get a personal schedule from the database
    schedule_name = request.form.get("schedule_name")
    personal_schedule = uc.get_saved_schedule(schedule_name)
    date_action = request.form.get("date_action")
    shown_date = request.form.get("shown_date")
    new_shown_date = sc.set_shown_date(shown_date, date_action)
    return render_template("my_schedule.html", personal_schedule=personal_schedule, shown_date=new_shown_date)
