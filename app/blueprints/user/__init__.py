from flask import Blueprint, redirect, url_for, render_template
from flask_login import logout_user, current_user

# from app.controllers.user_controller import add_country, get_user_by_email
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
    # countries = []
    # # How do I return all countries who has been clicked and therefore has a value of true?
    # country = request.form["country"]
    # countries.append(country)
    # country = request.form["myCountry"]
    # email = current_user.email
    # # schedule_name = ''  # How do we get this?
    # # if schedule_name == None:
    # schedule_name = "First"
    # add_country(email, country, schedule_name)
    return redirect(url_for("bp_user.select_countries_get"))


@bp_user.get("/create_schedule/step4")
# @login_required
def filtered_schedule_get():
    schedule = create_base_schedule("2022-02-05")
    personal_schedule = create_empty_personal_schedule()
    return render_template("create_schedule_step_4.html", schedule=schedule, personal_schedule=personal_schedule)


@bp_user.get("/my_schedule")
# @login_required
def my_schedules_get():
    schedule = create_empty_personal_schedule()
    return render_template("my_schedule.html", schedule=schedule)
