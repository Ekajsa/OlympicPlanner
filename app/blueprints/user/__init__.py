from flask import Blueprint, redirect, url_for, render_template
from flask_login import logout_user, current_user

bp_user = Blueprint("bp_user", __name__)


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
