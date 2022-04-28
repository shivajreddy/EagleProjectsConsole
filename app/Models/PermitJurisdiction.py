"""Jurisdiction model"""

from app import db

#* Jurisdiction Model
class Jurisdiction(db.Model):
  """Jurisdiction table"""

  __tablename__ = "jurisdictions"

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  jurisdiction_name = db.Column(db.Text, nullable = False)
