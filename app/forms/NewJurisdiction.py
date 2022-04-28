"""Form for adding new drafter"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import input_required


class NewJurisdiction(FlaskForm):
  """form for adding a new jurisdiction"""

  jurisdiction_name = StringField("Enter a new jurisdiction name to add to Database", validators=[input_required()])