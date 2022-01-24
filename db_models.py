from app import db
from flask_login import UserMixin


class Animal(db.Model):
    code = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    animal_family = db.Column(db.String(50), default="Не установлено")


class AnimalList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_code = db.Column(db.Integer, db.ForeignKey("animal.code"))
    date = db.Column(db.Date)
    color = db.Column(db.String(25), default="Неизвестно")
    height = db.Column(db.String(5), default="Неизвестно")
    breed = db.Column(db.String(50), default="Не установлено")


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
