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


#! Test route
@app.route('/test')
def test_route():
  db.create_all()
  all_lots = Test_LotsDirectory.query.filter_by(id=1)
  # curr_user = User.query.filter_by(id=1).first()
  # curr_user.editor = True
  # curr_user.super_editor = True
  # db.session.add(curr_user)
  # db.session.commit()
  # import pdb
  # pdb.set_trace()
  return "this is finished"


#! Routes
#! Un-Finished lots
@app.route('/')
def route_homePage():
  if 'user_email' not in session:
    return redirect('/sign-in')

  finished_lots = LotsDirectory.query.filter_by(finished=False).all()
  return render_template('home_page.html')
  # return render_template('home_page.html', lot_data=finished_lots)


#! ALL lots
@app.route('/all-lots')
def all_lots_page():
  if 'user_email' not in session:
    return redirect('/sign-in')
  
  # all_lots = LotsDirectory.query.all()
  # return render_template('all_lots.html', lot_data = all_lots)
  return render_template('all_lots.html')


#! Super User Links
@app.route('/super-links')
def route_super_links():
  if 'user_email' not in session:
    return redirect('/sign-in')
  
  if "super_editor" not in session or session['super_editor'] != True:
    return redirect('/')

  return render_template('./super_temp/super_links.html')
