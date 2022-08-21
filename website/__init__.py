from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database"

#Initialazing app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fr8D!Dhiweb8TRsj4@dea'
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="szopenkz",
    password="crewintense",
    hostname="szopenkz.mysql.pythonanywhere-services.com",
    databasename="szopenkz${}".format(DB_NAME))
    db.init_app(app)

    #importing blueprints views
    from .views import views
    from .auth import auth

    #Register blueprints, prefix none
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    #Where should flask redirect us when user is not logged in
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    #Use function to load user
    @login_manager.user_loader
    def load_user(id):
        #Query by primary key
        return User.query.get(int(id))

    return app


#If db tables doesn't exist, create new
def create_database(app):
    if not path.exists(app.config['SQLALCHEMY_DATABASE_URI']):
        db.create_all(app=app)
        return 'Created Database!'
    else:
        return 'Database found!'





