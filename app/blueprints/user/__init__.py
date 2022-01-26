
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, logout_user, current_user

from app.controllers import user_controller as uc
from app.controllers import event_controller as ec
from app.controllers.user_controller import add_country

bp_user = Blueprint("bp_user", __name__)


@bp_user.get("/")
def user():
    # De-comment to create database posts!
    # uc.create_user()
    # ec.create_event()
    return render_template("user.html")


@bp_user.before_request
def before_request():
    if not current_user.is_authenticated:
        return redirect(url_for('bp_open.index'))


@bp_user.get("/signout")
def signout_get():
    logout_user()
    return redirect(url_for("bp_open.index"))


@bp_user.get("/schedules")
# @login_required
def schedules_get():
    return render_template("schedules.html")


@bp_user.get("/disciplines")
# @login_required
def select_disciplines_get():
    return render_template("selectdisciplines.html")


@bp_user.get("/countries")
def select_countries_get():
    countries = get_countries()  # Continue here!
    return render_template("selectcountries.html")


@bp_user.post("/countries")
def select_countries_post():
    country = request.form["myCountry"]
    email = current_user.email
    # schedule_name = ''  # How do we get this?
    # if schedule_name == None:
    schedule_name = "First"
    add_country(email, country, schedule_name)
    return redirect(url_for("bp_user.select_countries_get"))
