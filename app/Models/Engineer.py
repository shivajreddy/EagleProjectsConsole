"""Engineer model"""

from app import db

#* Engineer Model
class Engineer(db.Model):
  """Engineer table"""

  __tablename__ = "engineers"

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  engineer_name = db.Column(db.Text, nullable = False)
