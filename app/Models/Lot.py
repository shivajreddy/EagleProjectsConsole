""" MODEL for a Lot entry"""
from flask_sqlalchemy import SQLAlchemy
from app import db


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
  time = db.Column(db.Text)

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
    "contract_date" : lot.contract_date,
    },

    "drafting" : {
    "assigned" : lot.assigned,
    "draft_deadline" : lot.draft_deadline,
    "actual" : lot.actual,
    "time" : lot.time,
    },

    "engineering" : {
    "eng" : lot.eng,
    "eng_sent" : lot.eng_sent,
    "eng_planned_receipt" : lot.eng_planned_receipt,
    "eng_actual_receipt" : lot.eng_actual_receipt,
    },
    
    "plat" : {
    "plat_eng" : lot.plat_eng,
    "plat_sent" : lot.plat_sent,
    "plat_planned_receipt" : lot.plat_planned_receipt,
    "plat_actual_receipt" : lot.plat_actual_receipt,
    },

    "permit" : {
    "permit_jurisdiction" : lot.permit_jurisdiction,
    "permit_planned_submit" : lot.permit_planned_submit,
    "permit_actual_submit" : lot.permit_actual_submit,
    "permit_received" : lot.permit_received,
    },

    "bbp" : {
    "bbp_planned_posted" : lot.bbp_planned_posted,
    "bbp_actual_posted" : lot.bbp_actual_posted,
    },

    "notes" : {
    "notes" : lot.notes
    }
  }

