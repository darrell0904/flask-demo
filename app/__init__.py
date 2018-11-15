'''
  Created By FJW in 20181021  
'''

from flask import Flask
from app.models.base import db

__author = '毛毛'

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    # 注册SQLAlchemy
    db.init_app(app)

    db.create_all(app=app)

    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)