from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField
from database.psql_db import db
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()


class User(db.Model):
  """users table"""

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  email = db.Column(db.Text, nullable=False, unique=True)
  password = db.Column(db.Text, nullable=False)


  # Registration
  @classmethod
  def register(cls, form_email, form_password):
    hashed_password = bcrypt.generate_password_hash(form_password)
    hashed_password_utf = hashed_password.decode('utf8')
    return cls(email=form_email, password=hashed_password_utf)

  # Authentication
  @classmethod
  def authenticate(cls, form_email, form_password):

    usr = User.query.filter_by(email=form_email).first()

    if usr and bcrypt.check_password_hash(usr.password , form_password):
      return usr
    return False



