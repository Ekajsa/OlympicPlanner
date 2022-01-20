from flask import Blueprint, render_template
from flask_login import login_required

from app.controllers import user_controller as uc
from app.controllers import event_controller as ec

bp_user = Blueprint('bp_user', __name__)


@bp_user.get('/')
def user():
    # De-comment to create database posts!
    # uc.create_user()
    # ec.create_event()
    return render_template('user.html')


@bp_user.get('/')
@login_required
def first_sorting_get():
    return render_template('firstsorting.html')
