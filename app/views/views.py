""" main views """
import os
from flask import jsonify, render_template, redirect, request, session, send_file, send_from_directory
from werkzeug.utils import secure_filename
from datetime import date

# from my_local_config import DOWNLOADS_DIR, FILES_UPLOADS_PATH
from .compareAlgorithm_V6 import run_algorithm
import shutil


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
    # Frontend makes an api call and renders data
    return render_template('home_page.html')


#! ALL lots
@app.route('/all-lots')
def all_lots_page():
    if 'user_email' not in session:
        return redirect('/sign-in')

    # all_lots = LotsDirectory.query.all()
    # return render_template('all_lots.html', lot_data = all_lots)
    # Frontend makes an api call and renders data
    return render_template('all_lots.html')

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
UPLOADS_DIR = os.getcwd() + "/app/static/uploaded_aqt_files"
GENERATED_REPORTS_DIR = os.getcwd() + "/app/static/generated_reports"
REPORT_TEMPLATE_FILE = GENERATED_REPORTS_DIR + "/ChangeReport_Template_v2.xlsm"
FILES_UPLOADS_PATH = os.getcwd() + "/app/static/uploaded_aqt_files"


@app.route('/tr')
def test_routes():
    return send_file("/Users/smbp/Desktop/EagleProjectsConsole/app/static/generated_reports/Lot-124-01-LA_HEL-30_V03-ComparisonReport-13-09-2022.xlsm", as_attachment=True, )
    print(GENERATED_REPORTS_DIR)
    return GENERATED_REPORTS_DIR

# Form, and client side file verification


# Test route to serve files
@app.route('/compare-reports')
def compare_reports():
    return render_template('./compare_reports.html')


# RUN -> Upload files -> Run the algo -> Start download
@app.route('/upload-run-download', methods=["GET", "POST"])
def upload_run_download():

    if request.files:
        # print("this is the dict", request.files)
        print("the request object is", request)

        # keys for this dict are keys of the form data, sent from client
        file1 = request.files["file1actual"]
        file2 = request.files["file2actual"]
        file1_name_ext = request.values['file1name']
        file2_name_ext = request.values['file2name']

        file_1_path_name_ext = UPLOADS_DIR + "/" + file1_name_ext
        file_2_path_name_ext = UPLOADS_DIR + "/" + file2_name_ext

        print("this are the file names", file1_name_ext, file2_name_ext)
        # /Users/shiva/Desktop/EagleProjectsConsole/app/static/uploaded_aqt_files

        file1.save(file_1_path_name_ext)
        file2.save(file_2_path_name_ext)

        # Main_EST_Lot-003-04-PV_CVX-10_AQT_2022-08-181661174495883.xlsm   find the index of last _
        i = file2_name_ext.rfind('_')
        result_file_name = file2_name_ext[0:i-4] + \
            "-ComparisonReport-" + date.today().strftime("%d-%m-%Y")

        # Create a copy of the report template, with new result_file_name as name
        shutil.copy(
            REPORT_TEMPLATE_FILE,
            f'{GENERATED_REPORTS_DIR}/{result_file_name}.xlsm')

        print('\x1b[0;39;43m' + 'This are the uploaded files' + '\x1b[0m')
        print(file1_name_ext)
        print(file2_name_ext)

        #!Run Report
        # TODO send the report file path
        print('\x1b[0;39;43m' + 'RUNNING ALGO ON' +
              '\x1b[0m', file1_name_ext, file2_name_ext)

        comparison_report_path_name_ext = GENERATED_REPORTS_DIR + \
            "/" + result_file_name + ".xlsm"
        run_algorithm(file_1_path_name_ext, file_2_path_name_ext,
                      comparison_report_path_name_ext)

        # file_1_path = os.path.join(
        #     app.config["FILES_UPLOADS_PATH"], file1_name_ext)
        # file_2_path = os.path.join(
        #     app.config["FILES_UPLOADS_PATH"], file2_name_ext)
        # run_algorithm(file_1_path, file_2_path)

        # return "both file1, file2 are valid"

        # TODO Start downloading the file
        result_file_name_ext = "/" + result_file_name + ".xlsm"
        finalPath = GENERATED_REPORTS_DIR + result_file_name_ext
        print("the final sheet name", finalPath)
        return send_file(finalPath, as_attachment=True)

        # print('START DOWNLOADING RESULT FILE')
        result_file_name_ext = result_file_name + ".xlsm"
        print(GENERATED_REPORTS_DIR, result_file_name_ext)
        result = send_from_directory(
            GENERATED_REPORTS_DIR, result_file_name_ext, as_attachment=True
        )
        print("this is the result", result)
        return result_file_name_ext
        return result
        # return redirect(f'/download-report/{result_file_name_ext}')

    # * Throw error if there are no files in the POST request
    raise Exception("The request object has no files in it")


@app.route("/download-report/<filename>")
def download_report(filename):
    # print('START DOWNLOADING RESULT FILE')
    result_file_name_ext = "/" + filename + ".xlsm"
    print("these are given", GENERATED_REPORTS_DIR, filename)
    finalPath = GENERATED_REPORTS_DIR + result_file_name_ext
    return send_file(finalPath, as_attachment=True)

    result = send_from_directory(
        GENERATED_REPORTS_DIR, filename, as_attachment=True
    )
    print("result is", result)
    return result


#! CompareReport -- END
