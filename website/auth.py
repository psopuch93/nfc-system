from flask import Blueprint, render_template, request, flash, redirect, url_for
# Secure password with hash two-way funcion - only check if password is correct with hash that stored:
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login =  request.form.get('login_form')
        password = request.form.get('password_form')
        user = User.query.filter_by(login = login).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category = 'succcess')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                return 'Error'
                #flash('Incorrect account info', category = 'error')
        else:
            return 'No account found'

    return render_template("login.html")

@auth.route('/sign-in', methods=['POST'])
def new_user():
    #Quick json post request data form
    request_data = request.get_json()
    login = request_data['login']
    password = request_data['password']
    user = User.query.filter_by(login = login).first()
    if user:
        flash('Login already exist!')
        return 'Duplicate login'
    else:
        #Generating password by sha256 method
        user = User(login = login, password = generate_password_hash(password, method = 'sha256'))
        db.session.add(user)
        db.session.commit()
        return 'New account succefully created'

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))



