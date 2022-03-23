
#! MODEL -> Lot Model
from flask_sqlalchemy import SQLAlchemy
from app import db
# from database.psql_db import db

class Lot(db.Model):
  """Lot Table"""

  __tablename__ = "lots"

  id = db.Column(db.Integer,
  primary_key=True,
  autoincrement=True)

  lot_name = db.Column(db.String(50))
  
  lot_date = db.Column(db.Date)

  def all_columns(self):
    return [self.lot_name, self.lot_date]



#* Actual lot model
class LotsDirectory(db.Model):
  """Lot Table"""

  __tablename__ = "all_lots_directory"

  #* Lot information category
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  community = db.Column(db.Text, nullable=False)
  section = db.Column(db.Text, nullable = False)
  lot_number = db.Column(db.Text, nullable = False)
  product = db.Column(db.Text,nullable=False)
  elevation = db.Column(db.Text, nullable=False)
  contract_date = db.Column(db.Date)

  #* Drafting
  assigned = db.Column(db.Text, nullable=False)
  draft_deadline = db.Column(db.Date)
  actual = db.Column(db.Date)
  time = db.Column(db.Integer)

  #* Engineering
  eng = db.Column(db.Text, nullable=False)
  eng_sent = db.Column(db.Date)
  eng_planned_receipt = db.Column(db.Date)
  eng_actual_receipt = db.Column(db.Date)
  
  #* Plat
  plat_eng = db.Column(db.Text, nullable=False)
  plat_sent = db.Column(db.Date)
  plat_planned_receipt = db.Column(db.Date)
  plat_actual_receipt = db.Column(db.Date)

  #* Permit
  permit_jurisdiction = db.Column(db.Text, nullable=False)
  permit_planned_submit = db.Column(db.Date)
  permit_actual_submit = db.Column(db.Date)
  permit_received = db.Column(db.Date)

  #* BBP
  bbp_planned_posted = db.Column(db.Date)
  bbp_actual_posted = db.Column(db.Date)

  #* Notes
  notes = db.Column(db.Text)

