from crypt import methods
import os
from flask import Flask, flash, render_template, redirect, session
from database.psql_db import db, connect_psqldb
from Models.Lot import Lot, LotsDirectory
from Models.User import User
from forms.NewLotForm import NewLotForm, NewLot
from forms.LoginForm import LoginForm, RegistrationForm
from sqlalchemy import delete
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# Mailing
from flask_mail import Mail, Message



import json
import pandas as pd
import plotly
import plotly.express as px
import ssl

#! App Conifguration
project_root = os.path.dirname(os.path.realpath('__file__'))
template_path = os.path.join(project_root, 'templates')
static_path = os.path.join(project_root, 'static')
app  = Flask(__name__, template_folder=template_path, static_folder=static_path)
app.config["SECRET_KEY"] = "e7543f072c2f7afd5ddfbba37edbc101b0c480c641a9d3be"
import config
mail = Mail(app)

#! PSQL database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///employees'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///eagleconsole'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
connect_psqldb(app)

#! Test route
@app.route('/testmail')
def testmail():
  msg = Message("this is the message", sender='test@tecofva.com', recipients=['shivajreddy@outlook.com'])
  msg.body = "this is the body of the message"
  mail.send(msg)
  return "<h1>mail sent</h1>"


#! Routes
@app.route('/')
def route_homePage():
  # db.create_all()

  if 'user_email' not in session:
    return redirect('/sign-in')

  all_lots = Lot.query.order_by("lot_name")
  all_lots = LotsDirectory.query.all()
  return render_template('home_page.html', lot_data=all_lots)


@app.route('/lot/new', methods=["GET", "POST"])
def new_lot():
  if 'user_email' not in session:
    return redirect('/sign-in')

  new_lot_form_inst = NewLotForm()

  #* Validate the form
  if new_lot_form_inst.validate_on_submit():
    #* get the responses from the form
    name = new_lot_form_inst.lot_name.data
    date = new_lot_form_inst.lot_date.datEagleProjectsConsole_Readmea
    new_lot_entry = Lot(lot_name=name, lot_date=date)
    db.session.add(new_lot_entry)
    db.session.commit()
    return redirect('/')
  else:
    return render_template('new_lot.html', form_data = new_lot_form_inst)

@app.route('/lot/edit/<int:lot_id>/', methods=["GET", "POST"])
def edit_lot(lot_id):
  if 'user_email' not in session:
    return redirect('/sign-in')

  lot = Lot.query.get(lot_id)
  lot_form = NewLotForm(obj=lot)

  #* Validate the edited form
  if lot_form.validate_on_submit():
    #* get the edited responses
    new_name = lot_form.lot_name.data
    new_date = lot_form.lot_date.data
    lot.lot_name = new_name
    lot.lot_date = new_date
    db.session.add(lot)
    db.session.commit()
    return redirect('/')
  else:
    return render_template('edit_lot.html', lot=lot_form)

@app.route('/lot/delete/<int:lot_id>/', methods=["GET", "POST"])
def delete_lot(lot_id):
  if 'user_email' not in session:
    return redirect('/sign-in')

  lot = db.session.query(Lot).filter(Lot.id==lot_id)
  lot.delete()
  db.session.commit()
  return redirect('/')


ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')



#* Using plotly
@app.route('/test/')
def test():
  df = pd.DataFrame({
  'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 
  'Bananas'],
  'Amount': [4, 1, 2, 2, 4, 5],
  'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
  })
  fig = px.bar(df, x='Fruit', y='Amount', color='City', 
    barmode='group')
  graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
  return render_template('notdash.html', graphJSON=graphJSON)


#? User Registration
@app.route('/register', methods=["GET", "POST"])
def sign_in():
  form = RegistrationForm()

  # validate form
  if form.validate_on_submit():
    
    if User.query.filter_by(email=form.email.data).first():
      flash(" already exists", f"{form.email.data}")
      return redirect('/sign-in')

    new_user = User.register(form.email.data, form.password.data)
    flash(f"Your account has been created, with {new_user.email}", "User already exists")
    session['user_email'] = new_user.email
    db.session.add(new_user)
    db.session.commit()

    return redirect('/')

  return render_template('sign_up.html', form_data=form)


#? User Log-In
@app.route('/sign-in/', methods=["GET", "POST"])
def register():
  form = LoginForm()

  if form.validate_on_submit():
    usr = User.query.filter_by(email=form.email.data).first()
    if not usr:
      flash("not found!", f"{form.email.data}")
      return redirect('/sign-in/')
    if usr.authenticate(form.email.data, form.password.data):
      session['user_email'] = usr.email
      # flash(f"Welcome {usr.email}")
      return redirect('/')
    flash(": Password incorrect", f"{form.email.data}")
    return redirect('/sign-in/')
    
  return render_template('login.html', form_data=form)


#? Log out
@app.route('/logout', methods=["POST"])
def logout():
  flash("successfully logged out.", session['user_email'])
  session.pop('user_email')
  return redirect('/sign-in')


@app.errorhandler(404)
def not_found_404(e):
  return render_template('404.html')

