from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField ,PasswordField, ValidationError
from wtforms.validators import input_required, email

#! Log-in Form
class LoginForm(FlaskForm):
  """Log in form using WTForm"""

  # email = StringField("Email address", validators=[input_required()])
  email = EmailField("Email address", validators=[input_required()])
  password = PasswordField("Password", validators=[input_required()])



#! Register-in Form
class RegistrationForm(FlaskForm):
  """Register using Eagle/Tec email"""

  # email = StringField("Email address", validators=[input_required()])
  email = EmailField("Email address", validators=[input_required()])
  password = PasswordField("Password", validators=[input_required()])

  def validate_email(self, email):
    i = (email.data).index('@')
    j = (email.data).index('.com')
    account = email.data[i+1:j]
    if account != "tecofva" and account != "eagleofva":
      flash("is not a Eagle email", email.data)
      raise ValidationError("This is not a Eagle email")
    return email

