import json

from flask import Blueprint, redirect, url_for, render_template, request
from flask_login import logout_user, current_user

from app.controllers.user_controller import edit_user, add_step3, add_step2
from app.controllers.schedule_controller import create_base_schedule, create_empty_personal_schedule



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
    # old_email = current_user.email
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
    return render_template("create_schedule_step_2.html")


@bp_user.post("/create_schedule/step2")
def select_disciplines_post():
    email = current_user.email
    the_list = request.form["hiddenList"]
    disciplines = json.loads(the_list)
    add_step2(email, disciplines)
    return redirect(url_for('bp_user.select_countries_get'))


@bp_user.get("/create_schedule/step3")
def select_countries_get():
    return render_template("create_schedule_step_3.html")


@bp_user.post("/create_schedule/step3")
def select_countries_post():
    email = current_user.email
    the_list = request.form["theList"]
    countries = json.loads(the_list)

    print()
    add_step3(email, countries)
    return redirect(url_for("bp_user.filtered_schedule_get"))


@bp_user.get("/create_schedule/step4")
# @login_required
def filtered_schedule_get():
    schedule = create_base_schedule("2022-02-07")
    personal_schedule = create_empty_personal_schedule()
    return render_template("create_schedule_step_4.html", schedule=schedule, personal_schedule=personal_schedule)


@bp_user.post("/create_schedule/step4")
def filtered_schedule_post():
    chosen_countries = request.json
    return redirect(url_for("bp_user.filtered_schedule_get"))


@bp_user.get("/my_schedule")
# @login_required
def my_schedules_get():
    schedule = create_empty_personal_schedule()
    return render_template("my_schedule.html", schedule=schedule)
