from flask import jsonify, render_template, redirect, session

from ..Models.Lot import LotsDirectory


from ..forms.NewLotForm import NewLot


import json
import pandas as pd
# import plotly
# import plotly.express as px


from app import app, db


#! Test route
@app.route('/test')
def test_route():
  from ..Models.seed import test_lot_1, test_lot_2, test_lot_3
  db.session.add(test_lot_1)
  db.session.add(test_lot_2)
  db.session.add(test_lot_3)
  db.session.commit()
  # db.create_all()
  return f"test page"


#! Routes
@app.route('/')
def route_homePage():

  if 'user_email' not in session:
    return redirect('/sign-in')

  all_lots = LotsDirectory.query.all()

  return render_template('home_page.html', lot_data=all_lots)


@app.route('/lot/edit/<int:lot_id>/', methods=["GET", "POST"])
def edit_lot(lot_id):
  if 'user_email' not in session:
    return redirect('/sign-in')

  # lot = Lot.query.get(lot_id)
  lot = LotsDirectory.query.get(lot_id)
  # lot_form = NewLotForm(obj=lot)
  lot_form = NewLot(obj=lot)

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



#* Using plotly
# @app.route('/test/')
# def test():
#   df = pd.DataFrame({
#   'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 
#   'Bananas'],
#   'Amount': [4, 1, 2, 2, 4, 5],
#   'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
#   })
#   fig = px.bar(df, x='Fruit', y='Amount', color='City', 
#     barmode='group')
#   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#   return render_template('notdash.html', graphJSON=graphJSON)


#? API
@app.route('/check-editor', methods=["GET"])
def check_editor_rights():
  if "user_email" not in session:
    return jsonify(False)
  if "user_email" in session and 'editor' in session and session['editor'] == True:
    return jsonify(True)
  return jsonify(False)



#! Route to make the current user an editor
# from ..Models.User import User
# @app.route('/change', methods=["GET", "POST"])
# def change_rights():
#   usr = User.query.filter_by(email="shiva@tecofva.com").first()
#   usr.editor = True
#   usr.super_editor = True
#   db.session.add(usr)
#   db.session.commit()
#   print(usr) 
#   return f"{usr}"

