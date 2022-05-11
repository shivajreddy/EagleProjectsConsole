from app import app, db

from flask import jsonify, redirect, render_template, session

from ..Models.Lot import LotsDirectory, serialize_lot
from ..Models.User import User

from ..Models.Community import Community
from ..Models.Product import Product
from ..Models.Elevation import Elevation
from ..Models.Drafter import Drafter
from ..Models.Engineer import Engineer
from ..Models.PlatEngineer import PlatEngineer
from ..Models.PermitJurisdiction import Jurisdiction

from ..forms.NewLotForm import NewLot


#! GET FINISHED lots
@app.route('/api/get-lots', methods=["GET"])
def get_finished_lots():
  all_lots = LotsDirectory.query.filter_by(finished=False).all()
  # serialize each lot
  results = [serialize_lot(lot) for lot in all_lots]
  return jsonify(results)


#! GET All Lots
@app.route('/api/get-all-lots', methods=["GET"])
def get_every_lots():
  all_lots = LotsDirectory.query.all()
  # serialize each lot
  results = [serialize_lot(lot) for lot in all_lots]
  return jsonify(results)


#! Get Current User
@app.route('/api/get-current-user', methods=["GET"])
def get_current_user():
  if 'user_email' not in session:
    return redirect('/')
  usr = User.query.filter_by(email=session['user_email']).first()
  usr_object = {
    "email" : usr.email,
    "token" : usr.token,
    "confirmed" : usr.confirmed_user,
    "editor" : usr.editor,
    "super_editor" : usr.super_editor,
  }
  return usr_object


#! Get User details
@app.route('/api/get-user-details/<user_email>', methods=["GET"])
def get_user_details(user_email):
  usr = User.query.filter_by(email=user_email).first()
  usr_object = {
    "email" : usr.email,
    "token" : usr.token,
    "confirmed" : usr.confirmed_user,
    "editor" : usr.editor,
    "super_editor" : usr.super_editor,
  }
  return usr_object


#! GET lot of id
@app.route('/api/get-lot/<int:id>', methods=["GET"])
def get_single_lot(id):

  # query for lot of given id
  lot = LotsDirectory.query.filter_by(id=id).first()

  # lot id exists in db
  if lot:
    return serialize_lot(lot)
    # return jsonify(serialize_lot(lot))
  
  # lot id DOES NOT exists in db
  return render_template('404.html', data={"id":id, "msg":"not in LotsDirectory table"}), 404


#! New Lot form
@app.route('/lot/new', methods=["GET", "POST"])
def new_lot():
  if 'user_email' not in session:
    return redirect('/sign-in')


  new_lot_form_inst = NewLot()

  all_communities = [(c.community_name, c.community_name) for c in Community.query.all()]
  all_products = [(p.product_name) for p in Product.query.all()]
  all_elevations = [(e.elevation_name) for e in Elevation.query.all()]
  all_drafters = [(i.drafter_name, i.drafter_name) for i in Drafter.query.all()]
  all_engineers = [(c.engineer_name, c.engineer_name) for c in Engineer.query.all()]
  all_platengineers = [(c.platengineer_name, c.platengineer_name) for c in PlatEngineer.query.all()]
  all_jurisdictions = [(c.jurisdiction_name, c.jurisdiction_name) for c in Jurisdiction.query.all()]

  new_lot_form_inst.community.choices = all_communities
  new_lot_form_inst.product.choices = all_products
  new_lot_form_inst.elevation.choices = all_elevations
  new_lot_form_inst.assigned.choices = all_drafters
  new_lot_form_inst.eng.choices = all_engineers
  new_lot_form_inst.plat_eng.choices = all_platengineers
  new_lot_form_inst.permit_jurisdiction.choices = all_jurisdictions

  #* Validate the form
  if new_lot_form_inst.validate_on_submit():
    print("New Lot form is VALIDATED ✅")

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
      permit_actual_submit = new_lot_form_inst.permit_actual_submit.data,
      permit_received = new_lot_form_inst.permit_received.data,

      bbp_planned_posted = new_lot_form_inst.bbp_planned_posted.data,
      bbp_actual_posted = new_lot_form_inst.bbp_actual_posted.data,

      notes = new_lot_form_inst.notes.data 
    )
    # import pdb
    # pdb.set_trace()

    db.session.add(new_lot_entry)
    db.session.commit()
    return redirect('/')
  else:
    # print("Form subbmission failed, giving you the get request")
    # import pdb
    # pdb.set_trace()
    return render_template('new_lot.html', form_data = new_lot_form_inst)


#! DELETE a lot
@app.route('/api/delete-lot/<int:lot_id>', methods=["GET", "DELETE"])
def delete_lot(lot_id):
  if 'user_email' not in session:
    return redirect('/sign-in')

  lot = db.session.query(LotsDirectory).filter(LotsDirectory.id==lot_id)
  lot.delete()
  db.session.commit()
  db.session.close()
  return jsonify(message=f'delete lot with id {lot_id}')
  #if you redirect to url, then axios will send again a request to this url 
  # return redirect('/') 


#? Check USER ROLE
@app.route('/check-editor', methods=["GET"])
def check_editor_rights():
  if "user_email" not in session:
    return jsonify(False)
  if "user_email" in session and 'editor' in session and session['editor'] == True:
    return jsonify(True)
  return jsonify(False)


#! EDIT lot 
@app.route('/lot/edit/<int:lot_id>/', methods=["GET", "POST"])
def edit_lot(lot_id):
  # redirect if there is no lot at this lot number
  lot_exists = bool(LotsDirectory.query.filter_by(id=lot_id).first())
  if not lot_exists:
    return redirect('/')

  if 'user_email' not in session:
    return redirect('/sign-in')

  lot = LotsDirectory.query.get(lot_id)
  lot_form = NewLot(obj=lot)

  all_communities = [(c.community_name, c.community_name) for c in Community.query.all()]
  all_products = [(p.product_name) for p in Product.query.all()]
  all_elevations = [(e.elevation_name) for e in Elevation.query.all()]
  all_drafters = [(i.drafter_name, i.drafter_name) for i in Drafter.query.all()]
  all_engineers = [(c.engineer_name, c.engineer_name) for c in Engineer.query.all()]
  all_platengineers = [(c.platengineer_name, c.platengineer_name) for c in PlatEngineer.query.all()]
  all_jurisdictions = [(c.jurisdiction_name, c.jurisdiction_name) for c in Jurisdiction.query.all()]

  lot_form.community.choices = all_communities
  lot_form.product.choices = all_products
  lot_form.elevation.choices = all_elevations
  lot_form.assigned.choices = all_drafters 
  lot_form.eng.choices = all_engineers 
  lot_form.plat_eng.choices = all_platengineers 
  lot_form.permit_jurisdiction.choices = all_jurisdictions 

  #* Validate the edited form
  if lot_form.validate_on_submit():

    #* get the edited responses
    #* Lot information category
    lot.finished = lot_form.finished.data
    lot.community = lot_form.community.data
    lot.section = lot_form.section.data
    lot.lot_number = lot_form.lot_number.data
    lot.product = lot_form.product.data
    lot.elevation = lot_form.elevation.data
    lot.contract_date = lot_form.contract_date.data

    #* Drafting
    lot.assigned = lot_form.assigned.data
    lot.draft_deadline = lot_form.draft_deadline.data
    lot.actual = lot_form.actual.data
    lot.time = lot_form.time.data

    #* Engineering
    lot.eng = lot_form.eng.data
    lot.eng_sent = lot_form.eng_sent.data
    lot.eng_planned_receipt = lot_form.eng_planned_receipt.data
    lot.eng_actual_receipt = lot_form.eng_actual_receipt.data
    
    #* Plat
    lot.plat_eng = lot_form.plat_eng.data
    lot.plat_sent = lot_form.plat_sent.data
    lot.plat_planned_receipt = lot_form.plat_planned_receipt.data
    lot.plat_actual_receipt = lot_form.plat_actual_receipt.data

    #* Permit
    lot.permit_jurisdiction = lot_form.permit_jurisdiction.data
    lot.permit_planned_submit = lot_form.permit_planned_submit.data
    lot.permit_actual_submit = lot_form.permit_actual_submit.data
    lot.permit_received = lot_form.permit_received.data

    #* BBP
    lot.bbp_planned_posted = lot_form.bbp_planned_posted.data
    lot.bbp_actual_posted = lot_form.bbp_actual_posted.data

    #* Notes
    lot.notes = lot_form.notes.data

    db.session.add(lot)
    db.session.commit()
    return redirect('/')

  return render_template('edit_lot.html', lot=lot_form)

# delete product instance
@app.route('/delete/product/<int:p_id>', methods=["GET", "DELETE"])
def delete_product_instance(p_id):

  if 'user_email' not in session:
    return redirect('/sign-in')

  p = db.session.query(Product).filter(Product.id==p_id)
  p.delete()
  db.session.commit()
  db.session.close()

  return jsonify(message=f'delete product with id {p_id}')

# delete community instance
@app.route('/delete/community/<int:c_id>', methods=["GET", "DELETE"])
def delete_community_instance(c_id):

  if 'user_email' not in session:
    return redirect('/sign-in')

  c = db.session.query(Community).filter(Community.id==c_id)
  c.delete()
  db.session.commit()
  db.session.close()

  return jsonify(message=f'delete community with id {c_id}')

# delete elevation instance
@app.route('/delete/elevation/<int:e_id>', methods=["GET", "DELETE"])
def delete_elevation_instance(e_id):

  if 'user_email' not in session:
    return redirect('/sign-in')

  e = db.session.query(Elevation).filter(Elevation.id==e_id)
  e.delete()
  db.session.commit()
  db.session.close()

  return jsonify(message=f'delete elevation with id {e_id}')

# delete drafter instance
@app.route('/delete/drafter/<int:d_id>', methods=["GET", "DELETE"])
def delete_drafter_instance(d_id):

  if 'user_email' not in session:
    return redirect('/sign-in')

  d = db.session.query(Drafter).filter(Drafter.id==d_id)
  d.delete()
  db.session.commit()
  db.session.close()

  return jsonify(message=f'delete drafter with id {d_id}')

# delete eng instance
@app.route('/delete/eng/<int:e_id>', methods=["GET", "DELETE"])
def delete_eng_instance(e_id):

  if 'user_email' not in session:
    return redirect('/sign-in')

  e = db.session.query(Engineer).filter(Engineer.id==e_id)
  e.delete()
  db.session.commit()
  db.session.close()

  return jsonify(message=f'delete eng with id {e_id}')


# delete plat instance
@app.route('/delete/plat/<int:p_id>', methods=["GET", "DELETE"])
def delete_plat_instance(p_id):

  if 'user_email' not in session:
    return redirect('/sign-in')

  p = db.session.query(PlatEngineer).filter(PlatEngineer.id==p_id)
  p.delete()
  db.session.commit()
  db.session.close()

  return jsonify(message=f'delete plateng with id {p_id}')


# delete jury instance
@app.route('/delete/jury/<int:j_id>', methods=["GET", "DELETE"])
def delete_jury_instance(j_id):

  if 'user_email' not in session:
    return redirect('/sign-in')

  j = db.session.query(Jurisdiction).filter(Jurisdiction.id==j_id)
  j.delete()
  db.session.commit()
  db.session.close()

  return jsonify(message=f'delete plateng with id {j_id}')