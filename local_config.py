"""Configuration file, with all the Flask app's configuration"""

# Development Environment
DEBUG = True


# Define the application directory
import os
BASE_DIR =  os.path.abspath(os.path.dirname(__file__))


#! App Config
SECRET_KEY = "d8bfa0ccf1b5e3ab8121a4747a8eeef2ec2f83ba3e4a9966"


#! DB config
SQLALCHEMY_DATABASE_URI = 'postgresql://tecofvac_sreddy:Intel1020$$@tecofvac.wwwmi3-ts15.a2hosted.com:5432/tecofvac_eagleconsole'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True


#! Mail Config
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = "shivatecofva@gmail.com"
MAIL_PASSWORD = 'Intel1020$$'
MAIL_USE_TLS = False
MAIL_USE_SSL = True
