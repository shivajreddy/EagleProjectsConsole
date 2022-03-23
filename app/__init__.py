"""App init file"""

from flask import Flask

#* Define the WSGI applicatin object
app = Flask(__name__)

#* Load Configurations
app.config.from_object('config')

#* Connect Databaase
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def connect_db(app):
  db.app = app
  db.init_app(app)
connect_db(app)

#* Import all views
from .views import views
