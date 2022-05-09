from datetime import date, datetime
from app import app
from flask_mail import Mail, Message
mail = Mail(app)
import ssl

msg = Message(
  subject="EPC Report ",
  recipients=["sreddy@tecofva.com"],
  sender="consoleadmin@eagleofva.com",
  # recipients=[os.environ.get('EMAIL_RECIPIENT')],
  # sender=os.environ.get('MAIL_USERNAME'),
  html = "this is the message text from consoleadmin"
)

context = ssl.create_default_context()

@app.route('/test-email')
def email_testing():
  # import pdb
  # pdb.set_trace()
  mail.send(msg)
  return "<h1> you are email </h1>"
