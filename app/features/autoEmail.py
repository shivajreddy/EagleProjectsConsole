from datetime import date, datetime
from app import app
from flask_mail import Mail, Message

from app.Models.Lot import LotsDirectory

from datetime import date, timedelta

def generate_content():
  drafting_overdue = []   # Drafting - OVERDUE
  eng_overdue = []    # Engineering - OVERDUE
  plat_overdue = []   # Plat - OVERDUE

  start = date(year=2022,month=4,day=1)
  end = date(year=2022,month=11,day=30)
  today = date.today()
  yesterday = today - timedelta(days=1)

  # query for drafting
  # for lot in LotsDirectory.query.filter(LotsDirectory.draft_deadline<= end).filter(LotsDirectory.draft_deadline>= start):
  for lot in LotsDirectory.query.filter(LotsDirectory.draft_deadline != None).filter(LotsDirectory.actual == None).filter(LotsDirectory.draft_deadline<= yesterday):
    drafting_overdue.append(lot)
  
  # query for engineering 
  for lot in LotsDirectory.query.filter(LotsDirectory.eng_planned_receipt != None).filter(LotsDirectory.eng_actual_receipt == None).filter(LotsDirectory.eng_planned_receipt<= yesterday):
    eng_overdue.append(lot)

  # query for plat
  for lot in LotsDirectory.query.filter(LotsDirectory.plat_planned_receipt != None).filter(LotsDirectory.plat_actual_receipt == None).filter(LotsDirectory.plat_planned_receipt<= yesterday):
    plat_overdue.append(lot)
  
  # import pdb
  # pdb.set_trace()
  
  html_body = ""
  html_body += f"<div> <h2 style='text-align:center;'>Project Dashboard - {today} </h2> <h3>Projects past {yesterday}</h3></div>"
  html_body += "<div>"
  html_body += f"<h4 style='color: #E06F38;'> Drafting Overdue - {len(drafting_overdue)} </h4>"
  for lot in drafting_overdue:
    html_body += f"<p> <strong>{lot.community}-{lot.lot_number}-{lot.section} </strong>  Drafting Deadline:{lot.draft_deadline}</p>"
  html_body += "-----------------------------------------------------------"
  html_body += f"<h4 style='color: #E06F38;'> Engineering Overdue - {len(eng_overdue)} </h4>"
  for lot in eng_overdue:
    html_body += f"<p> <strong>{lot.community}-{lot.lot_number}-{lot.section} </strong>  Eng.Planned:{lot.eng_planned_receipt}</p>"
  html_body += "-----------------------------------------------------------"
  html_body += f"<h4 style='color: #E06F38;'> Plat Overdue - {len(plat_overdue)} </h4>"
  for lot in plat_overdue:
    html_body += f"<p> <strong>{lot.community}-{lot.lot_number}-{lot.section} </strong>  Plat Planned:{lot.plat_planned_receipt}</p>"
  html_body += "</div>"
  html_body += "<div><p style='color:black; text-align:center;'> ⭕️ Eagle Projects Console </p></div>"

  return html_body


mail = Mail(app)

@app.route('/test-email')
def email_testing():

  msg = Message(
    subject="EPC Report ",
    recipients=["sreddy@tecofva.com"],
    sender = "console@archi-tec-tonic.com",
    # sender="consoleadmin@eagleofva.com",
    html = "this is the message text from consoleadmin"
  )
  data = generate_content()
  msg.html = data
  # mail.send(msg)
  return f"<h1> you email was sent with body {msg} </h1>"


# from flask_apscheduler import APScheduler
# scheduler = APScheduler()

from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()

def auto_email_job():
  print("AUTO EMAIL STARTING -----------------------------------------------------------------")
  with app.app_context():

    msg = Message(
      subject="EPC Daily Report ",
      recipients=["sreddy@tecofva.com"],
      # recipients=["sreddy@tecofva.com", "rarias@tecofva.com", "ksimonsen@tecofva.com"],
      # sender="consoleadmin@eagleofva.com",
      sender = "console@archi-tec-tonic.com",
      html = "default html content of message here"
    )

    data = generate_content()
    msg.html = data

    mail.send(msg)
    print("----------------------EMAIL SENT SECESSFULLY -----------------------------------")

