
from flask import Flask

#Initialazing app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fr8D!Dhiweb8TRsj4@dea'

    #importing blueprints views
    from .views import views
    from .auth import auth

    #Register blueprints, prefix none
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')



    return app

