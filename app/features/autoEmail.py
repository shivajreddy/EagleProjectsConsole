from datetime import date, datetime
from app import app
from flask_mail import Mail, Message

from app.Models.Lot import LotsDirectory

from datetime import date
start = date(year=2022,month=4,day=1)
end = date(year=2022,month=11,day=30)

def generate_content():
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

  return msg


mail = Mail(app)

@app.route('/test-email')
def email_testing():
  data = generate_content()

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


from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler

# scheduler = APScheduler()
scheduler = BackgroundScheduler()

def auto_email_job():
  with app.app_context():

    msg = Message(
      subject="EPC Report ",
      recipients=["sreddy@tecofva.com", "rarias@tecofva.com", "ksimonsen@tecofva.com"],
      sender="consoleadmin@eagleofva.com",
      html = "default html content of message here"
    )
    data = generate_content()
    msg.html = data

    mail.send(msg)
    print("Auto email job done")
