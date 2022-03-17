
#! Form -> New Lot Form
from flask_wtf import FlaskForm
from wtforms import StringField, DateField

class NewLotForm(FlaskForm):

  lot_name = StringField("Lot Identification")

  lot_date = DateField(" Lot Start Date")

class NewLot(FlaskForm):

  #* Lot information category
  community = StringField("Community")
  section = StringField("Section")
  lot_number = StringField("Lot Number")
  product = StringField("Product")
  elevation = StringField("Elevation")
  contract_date = DateField("Contract Date")

  #* Drafting Date
  assigned = StringField("Assigned to")
  draft_deadline = DateField("Draft Deadline")
  actual = DateField("Actual Date")
  time = DateField("Time in Minutes")

  #* Engineering
  eng = StringField("Engineer Name")
  eng_sent = DateField("Engineering Sent")
  eng_planned_receipt = DateField("Engineering Planned Receipt")
  eng_actual_receipt = DateField("Engineering Actual Receipt")
  
  #* Plat
  plat_eng = StringField("Plat Eng")
  plat_sent = DateField("Plat Sent")
  plat_planned_receipt = DateField("Plat Receipt")
  plat_actual_receipt = DateField("Plat Actual Receipt")

  #* Permit
  permit_jurisdiction = StringField("Jursidiction")
  permit_planned_submit = DateField("Permit planned submit")
  permit_acutual_submit = DateField("Permit Actual submit")
  permit_received =DateField("Permit Received")

  #* BBP
  bbp_planned_posted = DateField("BBP planned")
  bbp_actual_posted = DateField("BBP Actual posted")

  #* Notes
  notes = StringField("Lot Notes")