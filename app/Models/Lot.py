""" MODEL for a Lot entry"""
from flask_sqlalchemy import SQLAlchemy
from app import db


#* Actual lot model
class LotsDirectory(db.Model):
  """Lot Table"""

  __tablename__ = "all_lots_directory"

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



#! converting DATE-TIME string into Date
from datetime import datetime
def convert_to_date(datetime_string):
  dt_object = datetime.strptime(datetime_string, '%a, %d %b %Y %H:%M:%S %Z')
  return dt_object.date()

#!Serialization method
def serialize_lot(lot):

  return {
    "lot_info" :{
    "id" : lot.id,
    "community" : lot.community,
    "section" : lot.section,
    "lot_number" : lot.lot_number,
    "product" : lot.product,
    "elevation" : lot.elevation,
    "contract_date" : str(lot.contract_date),
    },

    "drafting" : {
    "assigned" : lot.assigned,
    "draft_deadline" : str(lot.draft_deadline),
    "actual" : str(lot.actual),
    "time" : str(lot.time),
    },

    "engineering" : {
    "eng" : lot.eng,
    "eng_sent" : str(lot.eng_sent),
    "eng_planned_receipt" : str(lot.eng_planned_receipt),
    "eng_actual_receipt" : str(lot.eng_actual_receipt),
    },
    
    "plat" : {
    "plat_eng" : lot.plat_eng,
    "plat_sent" : str(lot.plat_sent),
    "plat_planned_receipt" : str(lot.plat_planned_receipt),
    "plat_actual_receipt" : str(lot.plat_actual_receipt),
    },

    "permit" : {
    "permit_jurisdiction" : lot.permit_jurisdiction,
    "permit_planned_submit" : str(lot.permit_planned_submit),
    "permit_actual_submit" : str(lot.permit_actual_submit),
    "permit_received" : str(lot.permit_received),
    },

    "bbp" : {
    "bbp_planned_posted" : str(lot.bbp_planned_posted),
    "bbp_actual_posted" : str(lot.bbp_actual_posted),
    },

    "notes" : {
    "notes" : lot.notes
    }
  }

