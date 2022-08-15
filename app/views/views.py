""" main views """
import os
from flask import jsonify, render_template, redirect, request, session
from werkzeug.utils import secure_filename

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
  # all_lots = LotsDirectory.query.all()
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


#! CompareReport -- Start
# app.config["FILES_UPLOADS_PATH"] = "C:\\Users\\sreddy\\Desktop\\EagleProjectsConsole\\app\static\\reportfiles"
# app.config["ALLOWED_REPORT_FILE_EXT"] = ["XLSM", "XLS", "TXT"]

def allowed_files(filename):
  if not "." in filename:
    return False

  ext = filename.rsplit(".", 1)[1]
  if ext.upper() in app.config["ALLOWED_REPORT_FILE_EXT"]:
    return True
  
  return False


@app.route('/compare-reports')
def compare_reports():
  return render_template('./compare_reports.html')


@app.route('/run-report', methods=["GET", "POST"])
def run_comparision_report():

  #* This runs for POST method
  if request.method == "POST":

    if request.files:
      print("this is the dict", request.files)
      file1 = request.files["file1"]
      file2 = request.files["file2"]

      # redirect to form if both files are not uploaded
      if file1.filename == "" or file2.filename == "":
        return redirect('/compare-reports')

      file1_name = secure_filename(file1.filename)
      file2_name = secure_filename(file2.filename)

      file1.save(os.path.join(app.config["FILES_UPLOADS_PATH"], file1_name))
      file2.save(os.path.join(app.config["FILES_UPLOADS_PATH"], file2_name))

      if not allowed_files(file1.filename) or not allowed_files(file2.filename):
        print("One of the files uploaded file extension is not allowed")
        return redirect('/compare-reports')

      print('\x1b[0;39;43m' + 'This are the uploaded files' + '\x1b[0m')
      print(file1)
      print(file2)

      return "both file1, file2 are valid"

  #* This runs for GET method
  print("hi there report ran succesffuly")
  return "hi there report ran succesffuly"
#! CompareReport -- END