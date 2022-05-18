

# Filtering out Unique community Names from all lots
@app.route('/test')
def test_route():

  all_lots = LotsDirectory.query.all()

  comms = []

  # querying the LotsDirectory Model for distinict community names
  for com in LotsDirectory.query.distinct(LotsDirectory.community):
    community = com.community
    if community != None:
      comms.append(community)
  
  # Adding the names to the database
  for comm in comms:
    new_community = Community(community_name=comm)
    db.session.add(new_community)

  return "DONE"

# How to add editor, super_editor roles to user by id
ra = User.query.filter_by(id=12).first()
ra.editor = True
ra.super_editor = True
db.session.add(ra)
db.session.commit()

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

#! New Model
from ..Models.Drafter import Drafter
@app.route('/add-new-models')
def test_route():
  db.create_all()

#! Start the Drafter Category, with existing unique names
@app.route('/test')
def test_route():
  all_drafters = LotsDirectory.query.all()
  drafters = []
  # querying the LotsDirectory Model for distinct Drafter names
  for lot in LotsDirectory.query.distinct(LotsDirectory.assigned):
    drafter_name = lot.assigned
    if drafter_name != None and drafter_name != '':
      drafters.append(drafter_name)

  # use pdb_settrace to check the array, before adding to the db
  # add the entries to database
  for name in drafters:
    new_drafter = Drafter(drafter_name=name)
    db.session.add(new_drafter)
  db.session.commit()

  return 'done'


#* Removing a field from multiple instances
  # target_date = datetime.datetime(2000, 1, 2)
  # print('target date is ', target_date)
  # all_lots = LotsDirectory.query.filter_by(finished=False).filter_by(bbp_planned_posted=target_date).all()
  # for count, lot in enumerate(all_lots):
  #   print(count, lot, lot.bbp_planned_posted)
  #   lot.bbp_planned_posted = None
  #   db.session.add(lot)
  # db.session.commit()