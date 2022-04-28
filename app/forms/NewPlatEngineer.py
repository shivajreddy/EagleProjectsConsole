"""Form for adding new drafter"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import input_required


class NewPlatEngineer(FlaskForm):
  """form for adding a new plat engineer"""

  plat_engineer_name = StringField("Enter a new plat engineer name to add to Database", validators=[input_required()])