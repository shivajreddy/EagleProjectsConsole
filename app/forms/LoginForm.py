from flask import flash
from flask_wtf import FlaskForm
from wtforms import EmailField ,PasswordField, ValidationError
from wtforms.validators import input_required

#! Log-in Form
class LoginForm(FlaskForm):
  """Log in form using WTForm"""

  email = EmailField("Email address", validators=[input_required()])
  password = PasswordField("Password", validators=[input_required()])



#! Register-in Form
class RegistrationForm(FlaskForm):
  """Register using Eagle/Tec email"""

  email = EmailField("Email address", validators=[input_required()])
  password = PasswordField("Password", validators=[input_required()])

  # this is the name of the function that has to be, for custom email validation
  def validate_email(self, email):
    i = (email.data).index('@')
    j = (email.data).index('.com')
    account = email.data[i+1:j]
    if account != "tecofva" and account != "eagleofva":
      flash("is not a Eagle email", email.data)
      raise ValidationError("This is not a Eagle email")
    return email

