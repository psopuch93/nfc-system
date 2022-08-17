from flask import Blueprint, render_template
from . import db

views = Blueprint('views', __name__)

#URL for routes
@views.route('/')
def home():
    return render_template("login.html")

@views.route('/')
def login():
    return render_template("home.html")
