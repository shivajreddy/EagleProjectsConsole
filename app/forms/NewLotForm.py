
#! Form -> New Lot Form
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField
from wtforms.validators import input_required, optional

# class NewLotForm(FlaskForm):
#   lot_name = StringField("Lot Identification")
#   lot_date = DateField(" Lot Start Date")



class NewLot(FlaskForm):

  #* Lot information category
  # community = StringField("Community", validators=[input_required()])
  community = SelectField("Community", validators=[input_required()])
  section = StringField("Section", validators=[input_required()])
  lot_number = StringField("Lot Number", validators=[input_required()])
  product = StringField("Product", validators=[input_required()])
  elevation = StringField("Elevation", validators=[input_required()])
  contract_date = DateField("Contract Date", validators=[input_required()])

  #* Drafting Date
  assigned = StringField("Assigned to", validators=[input_required()])
  draft_deadline = DateField("Draft Deadline", validators=[optional()])
  actual = DateField("Actual Date", validators=[optional()])
  time = StringField("Time in Minutes", validators=[optional()])

  #* Engineering
  eng = StringField("Engineer Name", validators=[input_required()])
  eng_sent = DateField("Engineering Sent", validators=[optional()])
  eng_planned_receipt = DateField("Engineering Planned Receipt", validators=[optional()])
  eng_actual_receipt = DateField("Engineering Actual Receipt", validators=[optional()])
  
  #* Plat
  plat_eng = StringField("Plat Eng", validators=[input_required()])
  plat_sent = DateField("Plat Sent", validators=[optional()])
  plat_planned_receipt = DateField("Plat Receipt", validators=[optional()])
  plat_actual_receipt = DateField("Plat Actual Receipt", validators=[optional()])

  #* Permit
  permit_jurisdiction = StringField("Jursidiction", validators=[input_required()])
  permit_planned_submit = DateField("Permit planned submit", validators=[optional()])
  permit_acutual_submit = DateField("Permit Actual submit", validators=[optional()])
  permit_received =DateField("Permit Received", validators=[optional()])

  #* BBP
  bbp_planned_posted = DateField("BBP planned", validators=[optional()])
  bbp_actual_posted = DateField("BBP Actual posted", validators=[optional()])

  #* Notes
  notes = StringField("Lot Notes", validators=[optional()])