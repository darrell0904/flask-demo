from flask import Blueprint

web = Blueprint('web', __name__, template_folder='templates')

from app.web import book
from app.web import auth
from app.web import main
from app.web import gift
from app.web import drift
from app.web import wish