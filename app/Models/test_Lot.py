""" MODEL for a Lot entry"""
from flask import session
from flask_sqlalchemy import SQLAlchemy
from app import db


#* Actual lot model
class Test_LotsDirectory(db.Model):
  """Lot Table"""

  __tablename__ = "test_all_lots_directory"

  #* Lot information category
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  finished = db.Column(db.Boolean, default=False)
  community = db.Column(db.Text)
  section = db.Column(db.Text)
  lot_number = db.Column(db.Text)
  product = db.Column(db.Text)
  elevation = db.Column(db.Text)
  contract_date = db.Column(db.Date)

  #* Drafting
  assigned = db.Column(db.Text)
  draft_deadline = db.Column(db.Date)
  actual = db.Column(db.Date)
  time = db.Column(db.Text)

  #* Engineering
  eng = db.Column(db.Text)
  eng_sent = db.Column(db.Date)
  eng_planned_receipt = db.Column(db.Date)
  eng_actual_receipt = db.Column(db.Date)
  
  #* Plat
  plat_eng = db.Column(db.Text)
  plat_sent = db.Column(db.Date)
  plat_planned_receipt = db.Column(db.Date)
  plat_actual_receipt = db.Column(db.Date)

  #* Permit
  permit_jurisdiction = db.Column(db.Text)
  permit_planned_submit = db.Column(db.Date)
  permit_actual_submit = db.Column(db.Date)
  permit_received = db.Column(db.Date)

  #* BBP
  bbp_planned_posted = db.Column(db.Date)
  bbp_actual_posted = db.Column(db.Date)

  #* Notes
  notes = db.Column(db.Text)

  def __repr__(self):
    lot_info = f"[{self.community} {self.section} {self.lot_number} {self.contract_date}]"
    return lot_info
