from flask import Blueprint, render_template
from flask_login import login_required

from app.controllers import user_controller as uc
from app.controllers import event_controller as ec

bp_user = Blueprint("bp_user", __name__)


@bp_user.get("/")
def user():
    # De-comment to create database posts!
    # uc.create_user()
    # ec.create_event()
    return render_template("user.html")


@bp_user.get("/disciplines")
# @login_required
def select_disciplines_get():
    return render_template("selectdisciplines.html")


@bp_user.get("/countries")
def select_countries_get():
    return render_template("selectcountries.html")
