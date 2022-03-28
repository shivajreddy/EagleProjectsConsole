from app import app, db

from flask import jsonify, redirect, render_template, session

from ..Models.Lot import LotsDirectory, serialize_lot
from ..Models.Community import Community
from ..forms.NewLotForm import NewLot


#? GET all lots
@app.route('/api/get-lots', methods=["GET"])
def get_all_lots():

  # query DB for all lots
  all_lots = LotsDirectory.query.all()
  # serialize each lot
  results = [serialize_lot(lot) for lot in all_lots]
  
  return jsonify(results)


#? GET lot of id
@app.route('/api/get-lot/<int:id>', methods=["GET"])
def get_single_lot(id):

  # query for lot of given id
  lot = LotsDirectory.query.filter_by(id=id).first()

  # lot id exists in db
  if lot:
    return jsonify(serialize_lot(lot))
  
  # lot id DOES NOT exists in db
  return render_template('404.html', data={"id":id, "msg":"not in LotsDirectory table"}), 404


#? New Lot form
@app.route('/lot/new', methods=["GET", "POST"])
def new_lot():
  if 'user_email' not in session:
    return redirect('/sign-in')


  new_lot_form_inst = NewLot()

  all_communities = [(c.community_name, c.community_name) for c in Community.query.all()]
  new_lot_form_inst.community.choices = all_communities

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


#? DELETE a lot
@app.route('/api/delete-lot/<int:lot_id>/', methods=["DELETE"])
def delete_lot(lot_id):
  if 'user_email' not in session:
    return redirect('/sign-in')

  # lot = db.session.query(Lot).filter(Lot.id==lot_id)
  lot = db.session.query(LotsDirectory).filter(LotsDirectory.id==lot_id)
  lot.delete()
  db.session.commit()
  return redirect('/')


#? Check USER ROLE
@app.route('/check-editor', methods=["GET"])
def check_editor_rights():
  if "user_email" not in session:
    return jsonify(False)
  if "user_email" in session and 'editor' in session and session['editor'] == True:
    return jsonify(True)
  return jsonify(False)


#? EDIT lot 
@app.route('/lot/edit/<int:lot_id>/', methods=["GET", "POST"])
def edit_lot(lot_id):
  if 'user_email' not in session:
    return redirect('/sign-in')

  lot = LotsDirectory.query.get(lot_id)
  lot_form = NewLot(obj=lot)

  # import pdb
  # pdb.set_trace()

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

  print("FAILL")
  return render_template('edit_lot.html', lot=lot_form)
