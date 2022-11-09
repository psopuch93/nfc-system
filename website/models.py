#Import from packages import db

from .extension import db
from flask_login import UserMixin
from sqlalchemy.orm import backref

#Backref - back reference to parent

class Employee(db.Model):
    __tablename__ = 'employee'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    lastname = db.Column(db.String(128))
    logger_tag_id = db.Column(db.Integer, db.ForeignKey('loggertag.id'), unique=True)
    logger_tag = db.relationship("LoggerTag", backref=backref("employee", uselist=False))
    tool_tag_id = db.Column(db.Integer, db.ForeignKey('tooltag.id'), unique=True)
    tool_tag = db.relationship("ToolTag", backref=backref("employee", uselist=False))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    project = db.relationship("Project", backref=backref("employee", uselist=False))
    phone_id = db.Column(db.Integer, db.ForeignKey('phone.id'), unique=True)
    phone = db.relationship("Phone", backref=backref("employee", uselist=False))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(16), default = "admin")

class LoggerTag(db.Model):
    __tablename__ = 'loggertag'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serial = db.Column(db.String(16), unique=True)


class ToolTag(db.Model):
    __tablename__ = 'tooltag'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    serial = db.Column(db.String(16), unique=True)


class Project(db.Model):
    __tablename__ = 'project'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), unique=True)
    country = db.Column(db.String(128))
    serial = db.Column(db.String(16), unique=True)

class Tool(db.Model):
    __tablename__ = 'tool'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    serial = db.Column(db.String(128), unique=True)
    tag = db.Column(db.String(16), unique=True)

class Phone(db.Model):
    __tablename__ = 'phone'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))
    comp_id = db.Column(db.Integer)

class TimeLog(db.Model):
    __tablename__ = "timelog"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(64))
    tag = db.Column(db.String(64))
    project = db.Column(db.String(64))
    date = db.Column(db.String(64))
    time = db.Column(db.String(64))

