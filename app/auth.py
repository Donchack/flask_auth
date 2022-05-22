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

# при получении данных со страницы /login выполняется авторизация пльзователя
@auth.route('/login', methods=['POST'])
def login_post():
    form = Login_form()
    if form.validate_on_submit():
        # получаем имя пользователя с формы
        name = form.user_login.data
        # проходим по списку существующих пользователей
        for user in users:
            # если имя пользователя с формы нашлось в списке пользователей
            # и хэш пароля с формы равен хэшу из списка пользователей
            if (user.user_name == name 
                    and check_password_hash(user.psw_hash, form.user_psw.data)
                    ):
                # создание сеанса пользователя, сохраняется все время
                # пока пользователь авторизован
                login_user(user)
                print(current_user.get_id())
                # перенаправление на URL защищеннойстраницы обрабатываемый функцией main.profile 
                return redirect(url_for('main.profile'))
        return redirect(url_for('auth.login'))