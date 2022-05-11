"""Configuration file, with all the Flask app's configuration"""

# Development Environment
DEBUG = True


# Define the application directory
import os
BASE_DIR =  os.path.abspath(os.path.dirname(__file__))


#! App Config
SECRET_KEY = os.environ.get('SECRET_KEY')


#! DB config
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True


#! Mail Config
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = os.environ.get('MAIL_PORT')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_USE_TLS = True
MAIL_USE_SSL = False 
# MAIL_USE_TLS = False
# MAIL_USE_SSL = True