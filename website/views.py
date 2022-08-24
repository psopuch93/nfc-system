from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Project, LoggerTag

views = Blueprint('views', __name__)

#URL for routes
@views.route('/', methods = ['POST','GET'])
@views.route('/time-logger', methods = ['POST','GET'])
#Cant access home until login
@login_required
def home():
    return render_template("time-logger.html")


@views.route('/employees', methods = ['POST','GET'])
@login_required
def employees():
    return render_template("employees.html")

@views.route('/projects', methods = ['POST','GET'])
@login_required
def projects():
    projects = Project.query.all()
    return render_template("projects.html", projects = projects)

@views.route('/loggertags')
@login_required
def loggertags():
    loggertags = LoggerTag.query.all()
    return render_template("loggertags.html", loggertags = loggertags)

'''
@views.route('/time-logger', methods = ['POST','GET'])
@login_required
def time_logger():
        return render_template("time-logger.html")

'''