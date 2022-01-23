from flask import Blueprint, render_template
from flask_login import login_required, current_user
import db, query_db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/profile')
@login_required
def profile():
    animal_list = query_db.select_animals_list()
    return render_template("profile.html", name=current_user.username, animal_list=animal_list)

