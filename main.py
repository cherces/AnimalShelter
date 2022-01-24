from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
import query_db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/profile')
@login_required
def profile():
    animals_list = query_db.select_animals_list()
    type_anymals_list = query_db.select_type_animals()
    return render_template("profile.html",
                           name=current_user.username,
                           animals_list=animals_list,
                           type_animals_list=type_anymals_list)


@main.route('/profile/add', methods=['POST'])
@login_required
def registration():
    if request.form['add'] == 'add_to_animals_list':
        return redirect(url_for("operations_db.registration"))
    if request.form['add'] == 'add_to_types_list':
        return redirect(url_for("operations_db.addType"))

    return profile


@main.route('/profile/edit/animal', methods=['POST'])
@login_required
def edit_animal():
    if request.form['edit_animals_list']:
        return redirect(url_for("operations_db.edit_animal_index", id=int(request.form['edit_animals_list'])))

    return profile


@main.route('/profile/edit/type', methods=['POST'])
@login_required
def edit_type():
    if request.form['edit_type_animal']:
        return redirect(url_for("operations_db.edit_type_index", code=int(request.form['edit_type_animal'])))

    return profile


@main.route('/profile/delete/animal', methods=['POST'])
@login_required
def delete_animal():
    if request.form['delete_from_animals_list']:
        return redirect(url_for("operations_db.delete_animal", id=request.form['delete_from_animals_list']))

    return profile


@main.route('/profile/delete/type', methods=['POST'])
@login_required
def delete_type():
    if request.form['delete_type_animal']:
        return redirect(url_for("operations_db.delete_type", id=request.form['delete_type_animal']))

    return profile
