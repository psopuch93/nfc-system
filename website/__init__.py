from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


from .extension import db


#Initialazing app
def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
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





