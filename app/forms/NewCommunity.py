"""Form for adding new community"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import input_required


class NewCommunity(FlaskForm):
  """form for adding a new community"""

  community_name = StringField("Enter a new Community name to add to Database", validators=[input_required()])
