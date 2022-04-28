"""PlatEngineer model"""

from app import db

#* PlatEngineer Model
class PlatEngineer(db.Model):
  """PlatEngineer table"""

  __tablename__ = "platengineers"

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  platengineer_name = db.Column(db.Text, nullable = False)
