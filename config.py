"""Configuration file, with all the Flask app's configuration"""


# Development Environment
DEBUG = True


# Define the application directory
import os
BASE_DIR =  os.path.abspath(os.path.dirname(__file__))


#! App Config
SECRET_KEY = "d8bfa0ccf1b5e3ab8121a4747a8eeef2ec2f83ba3e4a9966"

#! DB config
SQLALCHEMY_DATABASE_URI = 'postgresql:///eagleconsole'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

