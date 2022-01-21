from app import animal_db


class Animal(animal_db.Model):
    code = animal_db.Column(animal_db.Integer, primary_key=True)
    name = animal_db.Column(animal_db.String(50), unique=True)
    animal_family = animal_db.Column(animal_db.String(50))


class AnimalList(animal_db.Model):
    id = animal_db.Column(animal_db.Integer, primary_key=True)
    type_code = animal_db.Column(animal_db.Integer, animal_db.ForeignKey('animal.code'))
    date = animal_db.Column(animal_db.Date)
    color = animal_db.Column(animal_db.String(25))
    height = animal_db.Column(animal_db.Integer)
