

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


