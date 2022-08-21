from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

#URL for routes
@views.route('/', methods = ['POST','GET'])
#Cant access home until login
@login_required
def home():
        return render_template("home.html")


@views.route('/time-logger', methods = ['POST','GET'])
@login_required
def time_logger():
        return render_template("time-logger.html")

