from flask import Blueprint, render_template, request, flash, redirect, url_for
# Secure password with hash two-way funcion - only check if password is correct with hash that stored:
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, LoggerTag, Employee, TimeLog, Phone
from .extension import db
from flask_login import login_user, login_required, logout_user#, current_user


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
                timelogger = TimeLog.query.order_by(TimeLog.id).all()
                return render_template('time-logger.html',timelogger = timelogger )
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
        db.session.close()
        return 'New account succefully created'

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


#NFC Tools Pro request catching. Unfortunetly NTP doesn't have json structure so im using list:
@auth.route('/new-tag', methods=['POST'])
def new_tag():
    data = request.get_data()
    data_str = str(data.decode("utf-8")).split(',')
    data_tag = str(data_str[0])

    find_duplicate = LoggerTag.query.filter_by(serial = data_tag).one_or_none()
    if find_duplicate is None:
        #New time logger db commit
        new_log = LoggerTag(id = '', serial = data_tag)
        db.session.add(new_log)
        db.session.commit()
        return 'New tag succefully created'
    else:
        return 'Duplicated Logger tag!'



#Catching NFC Tools Pro request: TIME LOGGER
@auth.route('/timelogger', methods=['POST'])
def new_log():
    data = request.get_data()
    data_str = str(data.decode("utf-8")).split(',')
    data_tag = str(data_str[0])
    data_comp_id = str(data_str[1])



    # Tag existing check

    is_tag_exist = LoggerTag.query.filter_by(serial = data_tag).one_or_none()
    if is_tag_exist:
        employee = Employee.query.filter_by(logger_tag_id = is_tag_exist.id).one_or_none()
        if employee:

            #Current time and date settings

            from datetime import datetime, date, timedelta
            date_today = date.today()
            now = datetime.now()
            dt_string = date_today
            real_time = now + timedelta(hours=1)
            dt_time_string = '{:%H:%M:%S}'.format(real_time)


            phone_id_query = Phone.query.filter_by(comp_id = data_comp_id).one_or_none()
            person_phone_id = Employee.query.filter_by(phone_id = phone_id_query.id).one_or_none()

            #Checking if is any duplicated query down by 5 minutes
            diff_time = '{:%H:%M:%S}'.format(real_time + timedelta(minutes=-5))
            '''is_logger_duplicated = TimeLog.query.filter_by(data_tag = tag, TimeLog.time >= diff_time, TimeLog.time < dt_time_string)
            if is_logger_duplicated is not None:
                new_login = TimeLog(phone = "{} {}".format(person_phone_id.name,person_phone_id.lastname) , tag ="{} {}".format(employee.name, employee.lastname), date = dt_string , time = dt_time_string )
                db.session.add(new_login)
                db.session.commit()
                return 'Add new time log'
            else:
                return 'Duplicated login!'
                '''
        else:
            return 'No employee found'
    else:
        return 'Tag not found'


@auth.route('/new-phone', methods=['POST'])
def add_phone():
    data = request.get_data()
    data_str = str(data.decode("utf-8")).split(',')
    data_tag = str(data_str[0])
    data_mac = str(data_str[1])

    #is_phone_exist = Phone.query.filter_by(n = data_mac).one_or_none()
    #if not is_phone_exist:
    new_phone = Phone(name = data_mac)
    db.session.add(new_phone)
    db.session.commit()
    return 'Add new phone'
    #else:
        #return 'Phone already in!'

'''
    #Datetime section
    from datetime import datetime, date, timedelta
    date_today = date.today()
    now = datetime.now()
    dt_string = date_today
    real_time = now + timedelta(hours=2)
    dt_time_string = '{:%H:%M:%S}'.format(real_time)
    '''