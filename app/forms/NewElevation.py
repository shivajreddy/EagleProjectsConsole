"""Form for adding new elevation"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import input_required


class NewElevation(FlaskForm):
  """form for adding a new elevation"""

  elevation_name = StringField("Enter a new Elevation name to add to Database", validators=[input_required()])
