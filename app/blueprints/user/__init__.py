<<<<<<< HEAD
from flask import Blueprint, render_template
from flask_login import login_required

from app.controllers import user_controller as uc
from app.controllers import event_controller as ec
=======
from flask import Blueprint, redirect, url_for, render_template
from flask_login import logout_user, current_user
>>>>>>> 43096225245274b6abc58310eb08575887961957

bp_user = Blueprint("bp_user", __name__)


<<<<<<< HEAD
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
=======
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
>>>>>>> 43096225245274b6abc58310eb08575887961957
