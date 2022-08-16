from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = "datebase"

#Initialazing app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fr8D!Dhiweb8TRsj4@dea'
    app.config["DEBUG"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="szopenkz",
    password="crewintense",
    hostname="szopenkz.mysql.pythonanywhere-services.com",
    databasename="szopenkz${}".format(DB_NAME))
    db.init_app(app)


    #importing blueprints views
    from .views import views
    from .auth import auth

    import .models

    #Register blueprints, prefix none
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')



    return app

def create_datebase(app):
    if not path.exists():
        db.create_all(app=app)


