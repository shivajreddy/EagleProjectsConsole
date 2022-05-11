"""App init file"""

from flask import Flask

#* Define the WSGI applicatin object
app = Flask(__name__)


#* Load Configurations
# app.config.from_object('heroku_config')
app.config.from_object('my_local_config')

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
# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


# from app.plotlydash.dashboard import init_dashboard
# app = init_dashboard(app)
