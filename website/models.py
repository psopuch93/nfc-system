#Import from packages import db

from . import db
from flask_login import UserMixin
from sqlalchemy.orm import backref

#Backref - back reference to parent
class Employee(db.Model):
    __tablename__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    lastname = db.Column(db.String(128))
    '''
    tag_logger_id = db.Column(db.Integer, db.ForeignKey('project.id'), unique=True)
    tag_logger = db.relationship("Tag_logger", backref=backref("employee", uselist=False))
    tag_tool_id = db.Column(db.Integer, db.ForeignKey('tag_tool.id'), unique=True)
    tag_tool = db.relationship("Tag_tool", backref=backref("employee", uselist=False))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    project = db.relationship("Phone", backref=backref("employee", uselist=False))
    phone_id = db.relationship('Phone')
    '''

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(16))

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.String(16), unique=True)
    type = db.Column(db.String(16))

class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    serial = db.Column(db.String(16), unique=True)

class Tool(db.Model):
    __tablename__ = 'tool'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    serial = db.Column(db.String(128), unique=True)
    tag = db.Column(db.String(16), unique=True)

class Phone(db.Model):
    __tablename__ = 'phone'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    imei = db.Column(db.String(64), unique=True)
    mac = db.Column(db.String(16), unique=True)
