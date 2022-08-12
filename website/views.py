from flask import Blueprint, render_template

views = Blueprint('views', __name__)

#URL for routes
@views.route('/')
def home():
    return render_template("home.html")

@views.route('/login')
def login():
    return render_template("login.html")
