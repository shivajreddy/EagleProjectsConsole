""" main views """
from flask import jsonify, render_template, redirect, request, session

from ..Models.Lot import LotsDirectory
from ..Models.test_Lot import Test_LotsDirectory
from ..Models.Community import Community
from ..Models.Drafter import Drafter
from ..Models.Engineer import Engineer
from ..Models.PlatEngineer import PlatEngineer
from ..Models.PermitJurisdiction import Jurisdiction
from ..Models.Elevation import Elevation
from ..Models.Product import Product
from ..Models.User import User

from ..forms.NewLotForm import NewLot

from app import app, db

import datetime
#! Test route
@app.route('/test')
def test_route():

  # last_lot = all_lots[0]
  # print(last_lot, last_lot.bbp_planned_posted, last_lot.bbp_actual_posted)
  # print('changking')
  # last_lot.bbp_planned_posted = None
  # db.session.add(last_lot)
  # db.session.commit()
  # print('finsihed changing')
  # print(last_lot, last_lot.bbp_planned_posted)

  # print('total are', len(all_lots))
  # curr_user = User.query.filter_by(id=1).first()
  # curr_user.editor = True
  # curr_user.super_editor = True
  # db.session.add(curr_user)
  # db.session.commit()
  # import pdb
  # pdb.set_trace()
  all_lots = LotsDirectory.query.all()
  # test_lot = all_lots[0]
  # for lot in all_lots:
    # lot.released = False
    # db.session.add(lot)
    # db.session.commit()
  return "this is finished"


#! Routes
#! Un-Finished lots
@app.route('/')
def route_homePage():
  if 'user_email' not in session:
    return redirect('/sign-in')

  # finished_lots = LotsDirectory.query.filter_by(finished=False).all()
  # return render_template('home_page.html', lot_data=finished_lots)
  return render_template('home_page.html')  # Frontend makes an api call and renders data


#! ALL lots
@app.route('/all-lots')
def all_lots_page():
  if 'user_email' not in session:
    return redirect('/sign-in')
  
  # all_lots = LotsDirectory.query.all()
  # return render_template('all_lots.html', lot_data = all_lots)
  return render_template('all_lots.html')     # Frontend makes an api call and renders data

#! Released Lots
@app.route('/released-lots')
def released_lots_page():
  if 'user_email' not in session:
    return redirect('/sign-in')
  
  return render_template('released_lots.html')
  # released_lots = LotsDirectory.query.filter_by(finished=False).all()
  # return render_template('released_lots.html', lot_data = released_lots)


#! Super User Links
@app.route('/super-links')
def route_super_links():
  if 'user_email' not in session:
    return redirect('/sign-in')
  
  if "super_editor" not in session or session['super_editor'] != True:
    return redirect('/')

  return render_template('./super_temp/super_links.html')
