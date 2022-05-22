from flask import Blueprint, render_template
from flask_login import login_required, current_user

from . import users


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html', the_part1='prj', the_part2='ind')

@main.route('/profile')
# @login_required
def profile():
    return render_template(
            'profile.html', the_part1='prj', the_part2='profile',
            the_users=tuple(users), name = current_user.get_id()
            )