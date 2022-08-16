#Import from packages import db

from . import db
from flask_login import UserMixin


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    lastname = db.Column(db.String(128))
    tag_logger_id = db.realtionship('Tag_logger')
    tag_tool_id = db.realtionship('Tag_tool')
    project = db.Column(db.Integer, db.ForeignKey('project.id'))
    phone = db.Column(db.String(128), unique=True)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))

#Split Logger Tag and Tool Tag to increase serial availability range value
class Tag_logger(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   serial = db.Column(db.String(24), unique=True)
   employee_id = db.Column(db.Integer, db.ForeignKey('tag_logger_id'), unique=True)

class Tag_tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial = db.Column(db.String(24), unique=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('tag_tool_id.'), unique=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    serial = db.Column(db.String(128), unique=True)
    tag = db.Column(db.String(24), unique=True)
