from Models.Lot import LotsDirectory, Lot
from database.psql_db import db, connect_psqldb
import datetime

db.drop_all()
db.create_all()

LotsDirectory.query.delete()
Lot.query.delete()

test_lot_1 = LotsDirectory(
  community="c1",
  section="s1",
  lot_number="ln1",
  product="p1",
  elevation="e1",
  contract_date= datetime.datetime(2020, 5, 17),

  assigned="a1",
  draft_deadline="dl1",
  actual="a1",
  time=21,

  #* Engineering
  eng = "eng1",
  eng_sent = x
  eng_planned_receipt = 
  eng_actual_receipt = 
  
  #* Plat
  plat_eng = 
  plat_sent = 
  plat_planned_receipt = 
  plat_actual_receipt = 

  #* Permit
  permit_jurisdiction = 
  permit_planned_submit = 
  permit_acutual_submit = 
  permit_received = 

  #* BBP
  bbp_planned_posted = 
  bbp_actual_posted = 

  #* Notes
  notes = 

)

test_lot = Lot(lot_name="testname1",
lot_date="1")



db.session.add(test_lot)
# db.session.add(test_lot_1)

db.session.commit()