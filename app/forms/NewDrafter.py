"""Form for adding new drafter"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import input_required


class NewDrafter(FlaskForm):
  """form for adding a new drafter"""

  drafter_name = StringField("Enter a new drafter name to add to Database", validators=[input_required()])
