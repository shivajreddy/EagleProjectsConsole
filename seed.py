from Models.Lot import LotsDirectory, Lot
from database.psql_db import db, connect_psqldb
import datetime

db.drop_all()
db.create_all()

LotsDirectory.query.delete()
Lot.query.delete()

test_lot_1 = LotsDirectory(
  #* Lot info
  community="c1",
  section="s1",
  lot_number="ln1",
  product="p1",
  elevation="e1",
  contract_date= datetime.datetime(2020, 5, 17),

  #* Drafting
  assigned="a1",
  draft_deadline= datetime.datetime(2020, 5, 17),
  actual= datetime.datetime(2020, 5, 17),
  time=21,

  #* Engineering
  eng = "eng1",
  eng_sent = datetime.datetime(2020, 5, 17),
  eng_planned_receipt = datetime.datetime(2020, 5, 17),
  eng_actual_receipt = datetime.datetime(2020, 5, 17),
  
  #* Plat
  plat_eng = "plateng1",
  plat_sent = datetime.datetime(2020, 5, 17),
  plat_planned_receipt = datetime.datetime(2020, 5, 17),
  plat_actual_receipt = datetime.datetime(2020, 5, 17),

  #* Permit
  permit_jurisdiction = "jury1",
  permit_planned_submit = datetime.datetime(2020, 5, 17),
  permit_actual_submit = datetime.datetime(2020, 5, 17),
  permit_received = datetime.datetime(2020, 5, 17),

  #* BBP
  bbp_planned_posted = datetime.datetime(2020, 5, 17),
  bbp_actual_posted = datetime.datetime(2020, 5, 17),

  #* Notes
  notes = "notes1"

)

test_lot_2 = LotsDirectory(
  #* Lot info
  community="c2",
  section="s2",
  lot_number="ln2",
  product="p2",
  elevation="e2",
  contract_date= datetime.datetime(2020, 5, 27),

  #* Drafting
  assigned="a2",
  draft_deadline= datetime.datetime(2020, 5, 27),
  actual= datetime.datetime(2020, 5, 27),
  time=22,

  #* Engineering
  eng = "eng2",
  eng_sent = datetime.datetime(2020, 5, 27),
  eng_planned_receipt = datetime.datetime(2020, 5, 27),
  eng_actual_receipt = datetime.datetime(2020, 5, 27),
  
  #* Plat
  plat_eng = "plateng2",
  plat_sent = datetime.datetime(2020, 5, 27),
  plat_planned_receipt = datetime.datetime(2020, 5, 27),
  plat_actual_receipt = datetime.datetime(2020, 5, 27),

  #* Permit
  permit_jurisdiction = "jury2",
  permit_planned_submit = datetime.datetime(2020, 5, 27),
  permit_actual_submit = datetime.datetime(2020, 5, 27),
  permit_received = datetime.datetime(2020, 5, 27),

  #* BBP
  bbp_planned_posted = datetime.datetime(2020, 5, 27),
  bbp_actual_posted = datetime.datetime(2020, 5, 27),

  #* Notes
  notes = "notes2"

)


test_lot_3 = LotsDirectory(
  #* Lot info
  community="c3",
  section="s3",
  lot_number="ln3",
  product="p3",
  elevation="e3",
  contract_date= datetime.datetime(2020, 5, 3),

  #* Drafting
  assigned="a3",
  draft_deadline= datetime.datetime(2020, 5, 3),
  actual= datetime.datetime(2020, 5, 3),
  time=33,

  #* Engineering
  eng = "eng3",
  eng_sent = datetime.datetime(2020, 5, 3),
  eng_planned_receipt = datetime.datetime(2020, 5, 3),
  eng_actual_receipt = datetime.datetime(2020, 5, 3),
  
  #* Plat
  plat_eng = "plateng3",
  plat_sent = datetime.datetime(2020, 5, 3),
  plat_planned_receipt = datetime.datetime(2020, 5, 3),
  plat_actual_receipt = datetime.datetime(2020, 5, 3),

  #* Permit
  permit_jurisdiction = "jury3",
  permit_planned_submit = datetime.datetime(2020, 5, 3),
  permit_actual_submit = datetime.datetime(2020, 5, 3),
  permit_received = datetime.datetime(2020, 5, 3),

  #* BBP
  bbp_planned_posted = datetime.datetime(2020, 5, 3),
  bbp_actual_posted = datetime.datetime(2020, 5, 3),

  #* Notes
  notes = "notes3"

)


# test_lot = Lot(lot_name="testname1",
# lot_date="1")


# db.session.add(test_lot)
db.session.add(test_lot_1)
db.session.add(test_lot_2)
db.session.add(test_lot_3)


db.session.commit()
