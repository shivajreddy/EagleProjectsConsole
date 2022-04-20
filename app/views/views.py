""" main views """
from crypt import methods
from flask import jsonify, render_template, redirect, request, session

from ..Models.Lot import LotsDirectory
from ..Models.Community import Community
from ..Models.User import User

from ..forms.NewLotForm import NewLot

from app import app, db


#! Test route
# @app.route('/test')
# def test_route():
#   ra = User.query.filter_by(id=15).first()
#   ra.editor = True
#   ra.super_editor = True
#   db.session.add(ra)
#   db.session.commit()
  # return "THIS IS FINISHED"


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
