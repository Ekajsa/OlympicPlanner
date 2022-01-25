
from app.controllers import user_controller as uc
from app.controllers import event_controller as ec

from flask import Blueprint, redirect, url_for, render_template, request
from flask_login import logout_user, current_user, login_required

from app.controllers.user_controller import add_countries, get_user_by_email

bp_user = Blueprint("bp_user", __name__)


@bp_user.get("/")
def user():
    # De-comment to create database posts!
    # uc.create_user()
    # ec.create_event()
    return render_template("user.html")


# @bp_user.before_request
# def before_request():
#     if not current_user.is_authenticated:
#         return redirect(url_for('bp_open.index'))


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
    return render_template("selectcountries.html")


@bp_user.post("/countries")
def select_countries_post():
    countries = []
    # How do I return all countries who has been clicked and therefore has a value of true?
    country = request.form["country"]
    countries.append(country)
    email = {{current_user.email}}
    add_countries(email, countries)
    # In add_countries I want
