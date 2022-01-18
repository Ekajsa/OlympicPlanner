from flask import Blueprint, render_template
from app.controllers import user_controller as uc
from app.controllers import schedule_controller as sc
from app.controllers import event_controller as ec

bp_user = Blueprint('bp_user', __name__)


@bp_user.get('/')
def user():
    # De-comment to create database posts!
    # uc.create_user()
    # sc.create_schedule()
    # ec.create_event()
    return render_template('user.html')
