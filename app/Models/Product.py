"""Product model"""

from app import db

#* Model
class Product(db.Model):
  """Product table"""

  __tablename__ = "products"

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  product_name = db.Column(db.Text, nullable = False)
