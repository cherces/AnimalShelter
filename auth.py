from flask import Blueprint, render_template, request, url_for, redirect
from db import Users
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/login', methods=['POST'])
def login_post():
    user_login = request.form.get('user_login')
    user_pass = request.form.get('user_password')

    user = Users.query.filter_by(username=user_login).first()

    if not user or user.password not in user_pass:
        return redirect('login')

    login_user(user)
    return redirect(url_for('main.profile'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
