import json

from flask import Blueprint, redirect, url_for, render_template, request
from flask_login import logout_user, current_user, login_required

# from app.controllers.user_controller import add_country, get_user_by_email
from app.controllers.schedule_controller import create_schedule

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


@bp_user.get("/create_schedule/step1")
# @login_required
def schedules_get():
    # list of schedules, only for test purpose
    # schedules = [{"name": "My first schedule"}, {"name": "My second schedule"}]
    schedules = ["My first schedule", "My second schedule"]
    return render_template("create_schedule_step_1.html", schedules=schedules)


@bp_user.get("/create_schedule/step2")
def select_disciplines_get():
    return render_template("create_schedule_step_2.html")


@bp_user.get("/create_schedule/step3")
def select_countries_get():
    # countries = get_country()  # Continue here!
    return render_template("create_schedule_step_3.html")


@bp_user.post("/create_schedule/step3")
def select_countries_post():
    the_list = request.form["theList"]
    countries = json.loads(the_list)

    print()
    return redirect(url_for("bp_user.filtered_schedule_get"))



@bp_user.get("/create_schedule/step4")
# @login_required
def filtered_schedule_get():
    schedule, disciplines, time_slots = create_schedule("2022-02-03")
    return render_template("create_schedule_step_4.html", schedule=schedule, disciplines=disciplines,
                           time_slots=time_slots)


@bp_user.post("/create_schedule/step4")
def filtered_schedule_post():
    chosen_countries = request.json
    return redirect(url_for("bp_user.filtered_schedule_get"))


@bp_user.get("/my_schedule")
# @login_required
def my_schedules_get():
    return render_template("my_schedule.html")
