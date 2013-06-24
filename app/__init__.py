from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
import os
from flask.ext.login import LoginManager
from config import basedir, UPLOAD_FOLDER
from werkzeug import secure_filename
from flaskext.babel import Babel


UPLOAD_FOLDER = 'app/static/pics'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'login'

babel = Babel(app)

mail = Mail(app)
app.extensions['mail'] = mail

from app import views, models

