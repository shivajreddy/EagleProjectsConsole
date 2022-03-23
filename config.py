"""Configuration file, with all the Flask app's configuration"""


# Development Environment
DEBUG = True


# Define the application directory
import os
BASE_DIR =  os.path.abspath(os.path.dirname(__file__))


#! App Config
SECRET_KEY = "d8bfa0ccf1b5e3ab8121a4747a8eeef2ec2f83ba3e4a9966"

#! DB config
SQLALCHEMY_DATABASE_URI = 'postgresql:///feedback'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True



# from app import app
# app.config['MAIL_SERVER']='smtp.mailtrap.io'
# app.config['MAIL_PORT'] = 2525
# app.config['MAIL_USERNAME'] = '76e36181f58151'
# app.config['MAIL_PASSWORD'] = '5d2ad4ef7c2996'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False



