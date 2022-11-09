from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy import func, desc
from .models import Project, LoggerTag, Employee, TimeLog, Phone
from .extension import db

views = Blueprint('views', __name__)

#URL for routes
@views.route('/', methods = ['POST','GET'])
@views.route('/time-logger', methods = ['POST','GET'])
#Cant access home until login
@login_required
def home():
    timelogger = TimeLog.query.order_by(TimeLog.id).all()
    return render_template("time-logger.html", timelogger = timelogger)


@views.route('/employees', methods = ['GET'])
@login_required
def employees():
    employees = Employee.query.all()
    loggertags = LoggerTag.query.all()
    phones = Phone.query.all()
    projects = Project.query.all()
    return render_template("employees.html", employees = employees, loggertags = loggertags, phones = phones, projects = projects)

@views.route('/employees/new', methods = ['POST'])
@login_required
def employees_new():

    data_list = []
    new_data_list = []

    employee_name = request.form['EmployeeName']
    employee_lastname = request.form['EmployeeLastname']
    employee_loggertag_id = request.form['EmployeeLoggertag']
    employee_phone_id = request.form['EmployeePhone']
    employee_project_id = request.form['EmployeeProject']

    data_list.append(employee_name)
    data_list.append(employee_lastname)
    data_list.append(employee_loggertag_id)
    data_list.append(employee_phone_id)
    data_list.append(employee_project_id)

    for i in data_list:
        if i == '':
            i = None
            new_data_list.append(i)
        else:
            new_data_list.append(i)


    new_employee = Employee(name = employee_name, lastname = employee_lastname, logger_tag_id = new_data_list[2],phone_id = new_data_list[3], project_id = new_data_list[4])
    db.session.add(new_employee)
    db.session.commit()
    db.session.close()
    return redirect(url_for('views.employees'))

@views.route('/projects', methods = ['POST','GET'])
@login_required
def projects():
    projects = Project.query.all()
    return render_template("projects.html", projects = projects)

@views.route('/loggertags', methods = ['GET'])
@login_required
def loggertags():
    loggertag = LoggerTag.query.order_by(LoggerTag.id).all()
    return render_template("loggertags.html", loggertag = loggertag)

@views.route('/phones', methods = ['GET'])
@login_required
def phones():
    phones = Phone.query.order_by(Phone.id).all()
    return render_template("phones.html", phones = phones)


@views.route('/phones/new', methods = ['POST'])
@login_required
def phone_new():
    phone_model = request.form['PhoneModel']
    phone_imei = request.form['PhoneIMEI']
    new_phone = Phone(id = '', name = phone_model, comp_id = phone_imei)
    db.session.add(new_phone)
    db.session.commit()
    db.session.close()
    return redirect(url_for('views.phones'))

'''
@views.route('/time-logger', methods = ['POST','GET'])
@login_required
def time_logger():
        return render_template("time-logger.html")

'''