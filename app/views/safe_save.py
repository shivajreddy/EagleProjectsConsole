

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