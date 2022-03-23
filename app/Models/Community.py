"""Community model"""

from app import db

#* Community Model
class Community(db.Model):
  """Community table"""

  __tablename__ = "communities"

  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  community_name = db.Column(db.Text, nullable = False)
