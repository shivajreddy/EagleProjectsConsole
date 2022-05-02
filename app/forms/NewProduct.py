"""Form for adding new product"""

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import input_required


class NewProduct(FlaskForm):
  """form for adding a new product"""

  product_name = StringField("Enter a new Prodcut name to add to Database", validators=[input_required()])
