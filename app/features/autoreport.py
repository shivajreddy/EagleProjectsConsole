
from app.views import mail
from flask_mail import Message 

msg = Message(
  subject="Daily Report",
  recipients=["sreddy@tecofva.com"],
  sender="",
  html = ""
)


from app.Models.Lot import LotsDirectory
from flask_apscheduler import APScheduler

scheduler = APScheduler()


# msg.html = ""

def job():

  # LotsDirectory.query.filter_by(id=1).first()
  lots = LotsDirectory.query.all()


  mail.send()
  print("this is the jobbb")
