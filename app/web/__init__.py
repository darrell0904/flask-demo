from flask import Blueprint
from flask import render_template

web = Blueprint('web', __name__, template_folder='templates')

# 蓝图下面404时，返回相同的页面
@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

from app.web import book
from app.web import auth
from app.web import main
from app.web import gift
from app.web import drift
from app.web import wish