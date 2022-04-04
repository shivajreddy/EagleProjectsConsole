""" main views """
from crypt import methods
from flask import jsonify, render_template, redirect, request, session

from ..Models.Lot import LotsDirectory
# from ..Models.User import User

from ..forms.NewLotForm import NewLot

from app import app, db


#! Test route
# @app.route('/test')
# def test_route():
  # import pdb
  # pdb.set_trace()
  # return "THIS IS FINISHED"
  # db.create_all()
  # return "create db"


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


@app.route('/new', methods=["GET"])
def new_test_home():
  all_lots = LotsDirectory.query.all()

  return render_template('newdir.html', all_lots = all_lots)


#! Route to make the current user an editor
# from ..Models.User import User
# @app.route('/change', methods=["GET", "POST"])
# def change_rights():
#   usr = User.query.filter_by(email="sreddy@tecofva.com").first()
#   usr.editor = True
#   usr.super_editor = True
#   db.session.add(usr)
#   db.session.commit()
#   print(usr) 
#   return f"{usr}"
