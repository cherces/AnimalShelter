import datetime

from flask import Blueprint, render_template, request, redirect, url_for

import db_models
import query_db
from app import db

operations_db = Blueprint('operations_db', __name__)


@operations_db.route('/registration')
def registration():
    return render_template('registration.html')


@operations_db.route('/registration', methods=['POST'])
def registration_animal():
    new_animal = db_models.AnimalList()
    new_animal.type_code = request.form['type']
    new_animal.color = request.form['color']
    new_animal.height = request.form['height']
    new_animal.breed = request.form['breed']
    new_animal.date = datetime.datetime.today()
    db.session.add(new_animal)
    db.session.commit()
    return redirect(url_for('main.profile'))


@operations_db.route('/addType')
def addType():
    return render_template('addType.html')


@operations_db.route('/addType', methods=['POST'])
def add_type():
    new_type = db_models.Animal()
    new_type.code = request.form['type']
    new_type.name = request.form['name']
    new_type.animal_family = request.form['family']
    db.session.add(new_type)
    db.session.commit()
    return redirect(url_for('main.profile'))


@operations_db.route('/editAnimal')
def edit_animal_index():
    id = request.args.get('id')
    item = query_db.select_animals_list_from_id(id)

    return render_template('editAnimal.html', item=item[0], id=id)


@operations_db.route('/editAnimal', methods=['POST'])
def edit_animal():
    edit_id = request.form['id']
    edit_animal = db_models.AnimalList.query.get(edit_id)
    edit_animal.type_code = request.form['type']
    edit_animal.color = request.form['color']
    edit_animal.height = request.form['height']
    edit_animal.breed = request.form['breed']

    db.session.commit()

    return redirect(url_for('main.profile'))


@operations_db.route('/editType')
def edit_type_index():
    code = request.args.get('code')
    item = query_db.select_type_from_code(code)

    return render_template('editType.html', item=item[0], code=code)


@operations_db.route('/editType', methods=['POST'])
def edit_type():
    edit_code = request.form['code']
    edit_type = db_models.Animal.query.get(edit_code)
    edit_type.name = request.form['name']
    edit_type.animal_family = request.form['family']

    db.session.commit()

    return redirect(url_for('main.profile'))


@operations_db.route('/deleteAnimal')
def delete_animal():
    del_user = db_models.AnimalList.query.filter_by(id=request.args.get('id')).first()

    if del_user is not None:
        db.session.delete(del_user)
        db.session.commit()

    return redirect(url_for('main.profile'))


@operations_db.route('/deleteType')
def delete_type():
    del_animal = db_models.Animal.query.filter_by(code=request.args.get('id')).first()

    if del_animal is not None:
        db.session.delete(del_animal)
        db.session.commit()

    return redirect(url_for('main.profile'))
