from crypt import methods
import os
from flask import Flask, flash, jsonify, render_template, redirect, session
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
  # import pdb
  # pdb.set_trace()

  if 'user_email' not in session:
    return redirect('/sign-in')

  all_lots = Lot.query.order_by("lot_name")
  all_lots = LotsDirectory.query.all()
  return render_template('home_page.html', lot_data=all_lots)


#? New Lot form
@app.route('/lot/new', methods=["GET", "POST"])
def new_lot():
  if 'user_email' not in session:
    return redirect('/sign-in')

  # new_lot_form_inst = NewLotForm()
  new_lot_form_inst = NewLot()

  #* Validate the form
  if new_lot_form_inst.validate_on_submit():
    print("PASSSSSSS")

    #* get the responses from the form
    new_lot_entry = LotsDirectory(
      community=new_lot_form_inst.community.data,
      section = new_lot_form_inst.section.data,
      lot_number = new_lot_form_inst.lot_number.data,
      product = new_lot_form_inst.product.data,
      elevation = new_lot_form_inst.elevation.data,
      contract_date = new_lot_form_inst.contract_date.data,

      assigned = new_lot_form_inst.assigned.data,
      draft_deadline = new_lot_form_inst.draft_deadline.data,
      actual = new_lot_form_inst.actual.data,
      time = new_lot_form_inst.time.data,

      eng = new_lot_form_inst.eng.data,
      eng_sent = new_lot_form_inst.eng_sent.data,
      eng_planned_receipt = new_lot_form_inst.eng_planned_receipt.data,
      eng_actual_receipt = new_lot_form_inst.eng_actual_receipt.data,

      plat_eng = new_lot_form_inst.plat_eng.data,
      plat_sent = new_lot_form_inst.plat_sent.data,
      plat_planned_receipt = new_lot_form_inst.plat_planned_receipt.data,
      plat_actual_receipt = new_lot_form_inst.plat_actual_receipt.data,

      permit_jurisdiction = new_lot_form_inst.permit_jurisdiction.data,
      permit_planned_submit = new_lot_form_inst.permit_planned_submit.data,
      permit_actual_submit = new_lot_form_inst.permit_acutual_submit.data,
      permit_received = new_lot_form_inst.permit_received.data,

      bbp_planned_posted = new_lot_form_inst.bbp_planned_posted.data,
      bbp_actual_posted = new_lot_form_inst.bbp_actual_posted.data,

      notes = new_lot_form_inst.notes.data 
    )
    db.session.add(new_lot_entry)
    db.session.commit()
    return redirect('/')
  else:
    print("FAILLLLL")
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
@app.route('/sign-in', methods=["GET", "POST"])
def register():
  form = LoginForm()

  if form.validate_on_submit():
    usr = User.query.filter_by(email=form.email.data).first()
    if not usr:
      flash("not found!", f"{form.email.data}")
      return redirect('/sign-in/')
    if usr.authenticate(form.email.data, form.password.data):

      session['user_email'] = usr.email
      session['editor'] = usr.editor

      # import pdb
      # pdb.set_trace()

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
  session.pop('editor')
  return redirect('/sign-in')


@app.errorhandler(404)
def not_found_404(e):
  return render_template('404.html')


#? API
@app.route('/check-editor', methods=["GET"])
def check_editor_rights():
  if "user_email" not in session:
    return json(False)
  if "user_email" in session and 'editor' in session and session['editor'] == True:
    return jsonify(True)
  return jsonify(False)


# #! Route to make the current user an editor
# @app.route('/change', methods=["GET", "POST"])
# def change_rights():
#   usr = User.query.filter_by(email="admin@tecofva.com").first()
#   usr.editor = True
#   db.session.add(usr)
#   db.session.commit()
#   print(usr) 
#   return f"{usr}"

