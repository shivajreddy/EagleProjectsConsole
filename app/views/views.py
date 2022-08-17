""" main views """
import os
from flask import jsonify, render_template, redirect, request, session, send_file, send_from_directory
from werkzeug.utils import secure_filename

# from ...my_local_config import REPORT_DOWNLOADS_PATH
#! Use these following imports when modifying models
# from ..Models.Lot import LotsDirectory
# from ..Models.test_Lot import Test_LotsDirectory
# from ..Models.Community import Community
# from ..Models.Drafter import Drafter
# from ..Models.Engineer import Engineer
# from ..Models.PlatEngineer import PlatEngineer
# from ..Models.PermitJurisdiction import Jurisdiction
# from ..Models.Elevation import Elevation
# from ..Models.Product import Product
# from ..Models.User import User

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

@app.route('/compare-reports')
def compare_reports():
  return render_template('./compare_reports.html')


# send the names of the uploaded files to run the report on, this should run the algo and return the result report file
@app.route('/run-report', methods=["GET", "POST"])
def run_comparison_report():
  print("running the run_comparison_report function on views.py")

  #* This runs for POST method
  if request.method == "POST":

    if request.files:
      # print("this is the dict", request.files)
      print("the request object is", request)

      # keys for this dict are keys of the form data, sent from client
      file1 = request.files["file1actual"]
      file2 = request.files["file2actual"]
      file1name = request.values['file1name']
      file2name = request.values['file2name']

      file1.save(os.path.join(app.config["FILES_UPLOADS_PATH"], file1name))
      file2.save(os.path.join(app.config["FILES_UPLOADS_PATH"], file2name))

      print('\x1b[0;39;43m' + 'This are the uploaded files' + '\x1b[0m')
      print(file1name)
      print(file2name)

      # return "both file1, file2 are valid"
      print('Going to redirect')
      return redirect('/compare-sheets-algorithm')

    #* Throw error if there are no files in the POST request
    raise Exception("The request object has no files in it")

  #* This runs for GET method
  print("hi there report ran successfully")
  return "hi there report ran successfully"

@app.route('/compare-sheets-algorithm', methods=["GET", "POST"])
def run_compare_sheets_algorithm():
  print('you are here')
  return redirect('/download-report/testdown')


@app.route("/download-report/<filename>")
def download_report(filename):
  try:
    # print("printing at", app.config["REPORT_DOWNLOADS_PATH"], filename )
    file_with_path = app.config["DOWNLOADS_DIR"] +filename + ".xlsm"
    print(file_with_path)
    return send_file(file_with_path, as_attachment=True)
    return send_from_directory(
      app.config["DOWNLOADS_DIR"],
      filename,
      as_attachment=True)
  except Exception as e:
    print("got exception")
    print(str(e))
    return str(e)

#! CompareReport -- END