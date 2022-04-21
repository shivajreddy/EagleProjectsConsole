from datetime import datetime
from app import app
from flask_mail import Mail, Message
mail = Mail(app)

msg = Message(
  subject="EPC Report ",
  recipients=["sreddy@tecofva.com"],
  sender="shivatecofva@gmail.com",
  html = "this is the message text"
)

# Get the lots and categorize them
from app.Models.Lot import LotsDirectory

# Make the subject automatic -> xD-xE-xp


all_lots_list = ['lot10', 'lot52', 'lot21']
# LotsDirectory.query.filter_by(id=1).first()
lots = LotsDirectory.query.all()


# Drafting - OVERDUE
drafting_overdue = []
# Drafting - Due this week
drafting_due_this_week = []
# Engineering - OVERDUE
eng_overdue = []
# Engineering - Due this week
eng_due_this_week = []
# Plat - OVERDUE
plat_overdue = []
# Plat - Due this week
plat_due_this_week = []


@app.route('/email')
def email_test():
  import pdb
  pdb.set_trace()

  return "<h1> you are email </h1>"


from flask_apscheduler import APScheduler
scheduler = APScheduler()


# msg.html = ""
count = 0
def job():

  # set the subject field
  today = datetime.now()
  format = "%d/%m/%Y %H:%M:%S"
  time = today.strftime(format)
  msg.subject += time

  #TODO traverse the lots and seggregate 
  #TODO create the msg body using the lists 

  # if you don't start with app's context then when ever this function
  # runs, it is going to start on another thread.
  with app.app_context():
    for lot in all_lots_list:
      msg.html += lot

    mail.send(msg)

    global count
    count += 1
    print("job done", count)
