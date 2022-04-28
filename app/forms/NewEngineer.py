"""Form for adding new drafter"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import input_required


class NewEngineer(FlaskForm):
  """form for adding a new engineer"""

  engineer_name = StringField("Enter a new engineer name to add to Database", validators=[input_required()])
