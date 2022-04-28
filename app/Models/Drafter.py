"""Drafter Model"""

from app import db


#* Drafter Model
class Drafter(db.Model):
  """Drafter Model"""

  __tablename__ = "drafters"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  drafter_name = db.Column(db.Text, nullable=False)