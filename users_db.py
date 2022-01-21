from app import animal_db


class Users(animal_db.Model):
    id = animal_db.Column(animal_db.Integer, primary_key=True)
    username = animal_db.Column(animal_db.String(100), unique=True)
    password = animal_db.Column(animal_db.String(100))
