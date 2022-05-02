"""Elevation model"""

from app import db

#* Elevation Model
class Elevation(db.Model):
  """Elevation table"""

  __tablename__ = "elevations"

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  elevation_name = db.Column(db.Text, nullable = False)