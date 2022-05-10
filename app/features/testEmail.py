from datetime import date, datetime
from app import app
from flask_mail import Mail, Message
from flask import render_template


# get the data to send in the email
from app.Models.Lot import LotsDirectory
from app.Models.Lot import serialize_lot


"""
----------------------
Overdue – Drafting
GF 118 (on hold)
GF 115
LC 41-2
MD 10
PY 70
PY 71
PY 72
PY 74
PY 75
----------------------
Overdue – Engineering
HM 18-6
GF 98
CY 325
GG 103-105
GF 94
RB 24-4
CY 324
RB 23-4
----------------------
Overdue – Plat
HM 25-6
HM 23-6
HM 33-6
HM 18-6
GF 98
GG 9-12
LA 113
GG 103-105
GF 94
RB 23-4
----------------------
"""


# drafting_overdue = []   # Drafting - OVERDUE
# drafting_due_this_week = []   # Drafting - Due this week
# eng_overdue = []    # Engineering - OVERDUE
# eng_due_this_week = []    # Engineering - Due this week
# plat_overdue = []   # Plat - OVERDUE
# plat_due_this_week = []   # Plat - Due this week

from datetime import date
start = date(year=2022,month=4,day=1)
end = date(year=2022,month=11,day=30)

def processtest():
  drafting_overdue = []   # Drafting - OVERDUE
  eng_overdue = []    # Engineering - OVERDUE
  plat_overdue = []   # Plat - OVERDUE

  # query for drafting
  for lot in LotsDirectory.query.filter(LotsDirectory.draft_deadline<= end).filter(LotsDirectory.draft_deadline>= start):
    drafting_overdue.append(lot)
  
  # query for engineering 
  for lot in LotsDirectory.query.filter(LotsDirectory.eng_planned_receipt<= end).filter(LotsDirectory.eng_planned_receipt>= start):
    eng_overdue.append(lot)

  # query for plat
  for lot in LotsDirectory.query.filter(LotsDirectory.plat_planned_receipt<= end).filter(LotsDirectory.plat_planned_receipt>= start):
    plat_overdue.append(lot)
  
  """
  'The Meadows 0 10'
  'Readers Branch 4 14'
  'The Meadows 0 14'
  'Givens Farm 12 99'
  'Readers Branch 4 23'
  'Cypress Creek 7B 324'
  'Readers Branch 4 24'
  "Settler's Ridge A 4"
  "Settler's Ridge E 82"
  """

  msg = ""
  msg += f"<div> <h2 style='text-align:center;'>Project Dashboard - {date.today()}</h2></div>"
  msg += "<div>"
  msg += "<h2 style='color: #E06F38;'> Drafting Overdue </h2>"
  for i in drafting_overdue:
    msg += f"<p>{i.community}-{i.section}-{i.lot_number}</p>"
  msg += "-----------------------------------------------------------"
  msg += "<h2 style='color: #E06F38;'> Engineering Overdue </h2>"
  for lot in eng_overdue:
    msg += f"<p>{lot.community}-{lot.section}-{lot.lot_number}</p>"
  msg += "-----------------------------------------------------------"
  msg += "<h2 style='color: #E06F38;'> Plat Overdue </h2>"
  for lot in plat_overdue:
    msg += f"<p>{lot.community}-{lot.section}-{lot.lot_number}</p>"
  msg += "</div>"
  msg += "<div><p style='color:black; text-align:center;'> ⭕️ Eagle Projects Console </p></div>"

  # import pdb
  # pdb.set_trace()

  return msg



mail = Mail(app)

@app.route('/test-email')
def email_testing():
  data = processtest()

  msg = Message(
    subject="EPC Report ",
    recipients=["sreddy@tecofva.com"],
    # recipients=["sreddy@tecofva.com", "lhartmann@tecofva.com"],
    sender="consoleadmin@eagleofva.com",
    # recipients=[os.environ.get('EMAIL_RECIPIENT')],
    # sender=os.environ.get('MAIL_USERNAME'),
    html = "this is the message text from consoleadmin"
  )
  msg.html = data
  # msg.body = render_template(data)

  mail.send(msg)
  return f"<h1> you email was sent with body {msg} </h1>"
