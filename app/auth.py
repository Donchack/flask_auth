from flask import Blueprint, render_template, url_for, redirect
from werkzeug.security import check_password_hash
from flask_login import login_user, current_user

from . import users
from .forms import Login_form


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    form = Login_form()
    return render_template('login.html', the_part1='prj', the_part2='log',
            form=form
            )

@auth.route('/login', methods=['POST'])
def login_post():
    form = Login_form()
    if form.validate_on_submit():
        name = form.user_login.data
        for user in users:
            if (user.user_name == name 
                    and check_password_hash(user.psw_hash, form.user_psw.data)
                    ):
                


                login_user(user)
                print(current_user.get_id())
                return redirect(url_for('main.profile'))
        return redirect(url_for('auth.login'))