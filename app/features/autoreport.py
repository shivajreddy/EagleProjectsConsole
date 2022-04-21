from app import app
from flask_mail import Mail, Message
mail = Mail(app)

msg = Message(
  subject="Daily Report",
  recipients=["sreddy@tecofva.com"],
  sender="shivatecofva@gmail.com",
  html = "this is the message text"
)

# Get the lots and categorize them
from app.Models.Lot import LotsDirectory

# Make the subject automatic -> xD-xE-xp


all_lots_list = ['lot10', 'lot52', 'lot21']
  # LotsDirectory.query.filter_by(id=1).first()
  # lots = LotsDirectory.query.all()
  # Drafting - OVERDUE
  # Drafting - Due this week
  # Engineering - OVERDUE
  # Engineering - Due this week
  # Plat - OVERDUE
  # Plat - Due this week


from flask_apscheduler import APScheduler
scheduler = APScheduler()


# msg.html = ""
count = 0
def job():
  # if you don't start with app's context then when ever this function
  # runs, it is going to start on another thread.
  with app.app_context():
    for lot in all_lots_list:
      msg.html += lot

    mail.send(msg)

    global count
    count += 1
    print("job done", count)
