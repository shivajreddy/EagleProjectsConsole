
#! Form -> New Lot Form
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, BooleanField
from wtforms.validators import input_required, optional

# class NewLotForm(FlaskForm):
#   lot_name = StringField("Lot Identification")
#   lot_date = DateField(" Lot Start Date")



class NewLot(FlaskForm):

  #* Lot information category
  # community = StringField("Community", validators=[input_required()])
  finished = BooleanField("Finished", validators=[optional()])
  community = SelectField("Community", validators=[optional()])
  section = StringField("Section", validators=[optional()])
  lot_number = StringField("Lot Number", validators=[optional()])
  product = StringField("Product", validators=[optional()])
  elevation = StringField("Elevation", validators=[optional()])
  contract_date = DateField("Contract Date", validators=[optional()])

  #* Drafting Date
  assigned = SelectField("Assigned to", validators=[optional()])
  draft_deadline = DateField("Draft Deadline", validators=[optional()])
  actual = DateField("Actual Date", validators=[optional()])
  time = StringField("Time in Minutes", validators=[optional()])

  #* Engineering
  eng = SelectField("Engineer Name", validators=[optional()])
  eng_sent = DateField("Engineering Sent", validators=[optional()])
  eng_planned_receipt = DateField("Engineering Planned Receipt", validators=[optional()])
  eng_actual_receipt = DateField("Engineering Actual Receipt", validators=[optional()])
  
  #* Plat
  plat_eng = SelectField("Plat Eng", validators=[optional()])
  plat_sent = DateField("Plat Sent", validators=[optional()])
  plat_planned_receipt = DateField("Plat Receipt", validators=[optional()])
  plat_actual_receipt = DateField("Plat Actual Receipt", validators=[optional()])

  #* Permit
  permit_jurisdiction = SelectField("Jursidiction", validators=[optional()])
  permit_planned_submit = DateField("Permit planned submit", validators=[optional()])
  permit_actual_submit = DateField("Permit Actual submit", validators=[optional()])
  permit_received =DateField("Permit Received", validators=[optional()])

  #* BBP
  bbp_planned_posted = DateField("BBP planned", validators=[optional()])
  bbp_actual_posted = DateField("BBP Actual posted", validators=[optional()])

  #* Notes
  notes = StringField("Lot Notes", validators=[optional()])
