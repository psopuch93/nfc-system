from flask import Blueprint

views = Blueprint('views', __name__)

#URL for routes
@views.route('/')
def home():
    return "<h1>TEST</h>"
