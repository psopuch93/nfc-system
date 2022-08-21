from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

#URL for routes
@views.route('/', methods = ['POST','GET'])
#Cant access home until login
@login_required
def home():
    if request.method == 'POST':
        return render_template("home.html")
    else:
        return redirect(url_for('auth.login'))
