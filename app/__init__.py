"""App init file"""

from flask import Flask

# trying db migration


#* Define the WSGI applicatin object
app = Flask(__name__)


#* Load Configurations
app.config.from_object('my_local_config')
# app.config.from_object('heroku_config')

#* Connect Databaase
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def connect_db(app):
  db.app = app
  db.init_app(app)
connect_db(app)


#* Import all views
from .views import views, auth_views, api, super_user_views

#* Import features
# from .features.autoreport import automail
from .features import autoEmail, autoreport


#* may be need this for ssl problems
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


# from app.plotlydash.dashboard import init_dashboard
# app = init_dashboard(app)
