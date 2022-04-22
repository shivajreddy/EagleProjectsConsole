from datetime import date, datetime
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

# LotsDirectory.query.filter_by(id=1).first()
lots = LotsDirectory.query.all()
testlot = lots[0]


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

def group_lots():
  # clear the array before adding new lots to this
  drafting_overdue.clear()
  drafting_due_this_week.clear()
  eng_overdue.clear()
  eng_due_this_week.clear()
  plat_overdue.clear()
  plat_due_this_week.clear()

  lots = LotsDirectory.query.all()
  # (Pdb) testlot
  # [Readers Branch None 5 2018-05-31]
  # (Pdb) today = date.today()
  # (Pdb) testlot.actual
  # datetime.date(2018, 9, 17)
  # (Pdb) testlot.actual - today
  # datetime.timedelta(days=-1312)
  # (Pdb) diff = testlot.actual - today
  # (Pdb) diff.days
  # -1312
  today = date.today()
  for lot in lots:
    if (lot.actual - today).days < 0:
      entry = lot.community + lot.section + lot.lot_number
      drafting_overdue.append(entry)


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
