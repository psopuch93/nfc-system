from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login =  request.form.get('login_form')
        password = request.form.get('password_form')



    return render_template("login.html")

@auth.route('/logout')
def logout():
    return 'ok'



