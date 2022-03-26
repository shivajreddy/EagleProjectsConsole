"""mail app module"""
from app import app

from flask_mail import Mail, Message
mail = Mail(app)

def send_confirmation_mail(recipient_email, token):

  # create a link with email and token
  domain = "/127.0.0.1.8000/confirm/"
  link = f"{domain}{recipient_email}/{token}"

  msg = Message(
    subject="Please confirm your registration to Eagle Console",
    recipients= [recipient_email, "shivajreddy@outlook.com"],
    sender= "consoleadmin@tecofva.com",
    body = f"This is the link {link}"
  )
  # import pdb
  # pdb.set_trace()

  mail.send(msg)

  return "sucess"
