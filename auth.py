from flask import Blueprint, render_template, request, url_for, redirect

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html")


@auth.route('/login', methods=['POST'])
def login_post():
    user_login = request.form.get('user_login')
    user_pass = request.form.get('user_password')

    if user_login in "" or user_pass in "":
        return redirect('login')

    return redirect(url_for('main.profile'))


@auth.route('/logout')
def logout():
    return 'Logout'
