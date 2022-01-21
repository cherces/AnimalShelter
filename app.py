from flask import Flask
from flask_sqlalchemy import SQLAlchemy


animal_db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'rh63nvG7fj9v0?;DAdj1#'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///animals_db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    animal_db.init_app(app)

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)

