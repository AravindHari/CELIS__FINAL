from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO,send
import logging
from flask_mail import Mail

logging.basicConfig(level=logging.DEBUG)
#general configs
app=Flask(__name__)
app.config.from_object(config)
from flask_socketio import SocketIO,send
socketio=SocketIO(app,engineio_logger=True,logger=True)
#DB Configs
db=SQLAlchemy(app)
migrate=Migrate(app,db)
#Login Configs
login=LoginManager(app)
login.login_view='login'
login.message='Please Login To Access The Page'
login.login_message_category='info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = ("celis.students@gmail.com")
app.config['MAIL_PASSWORD'] = ("Celis123@")
mail = Mail(app)

from app import routes,models
