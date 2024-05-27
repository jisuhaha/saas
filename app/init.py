from flask import Flask
import logging
from .models import db
from . import config

def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # SQLALCHEMY_TRACK_MODIFICATIONS는 SQLAlchemy의 이벤트를 처리하는 옵션
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


    flask_app.app_context().push()
    db.init_app(flask_app)
    db.create_all()
    return flask_app