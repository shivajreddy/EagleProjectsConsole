from Models.Lot import LotsDirectory, Lot
from database.psql_db import db, connect_psqldb
import datetime

db.drop_all()
db.create_all()

LotsDirectory.query.delete()
Lot.query.delete()

test_lot_1 = LotsDirectory(
  #* Lot info
  community="Lauradell",
  section="1",
  lot_number="101",
  product="Savannah",
  elevation="Folk Victorian",
  contract_date= datetime.datetime(2021, 12, 29),

  #* Drafting
  assigned="C.Zobel",
  draft_deadline= datetime.datetime(2021, 12, 31),
  actual= datetime.datetime(2022, 1, 17),
  time=240,

  #* Engineering
  eng = "Struc Tech",
  eng_sent = datetime.datetime(2022, 1, 17),
  eng_planned_receipt = datetime.datetime(2022, 1, 14),
  eng_actual_receipt = datetime.datetime(2022, 1, 24),
  
  #* Plat
  plat_eng = "Bolen",
  plat_sent = datetime.datetime(2022, 1, 17),
  plat_planned_receipt = datetime.datetime(2022, 1, 14),
  plat_actual_receipt = datetime.datetime(2020, 1, 18),

  #* Permit
  permit_jurisdiction = "Hanover",
  permit_planned_submit = datetime.datetime(2022, 1, 19),
  permit_actual_submit = datetime.datetime(2022, 2, 15),
  # permit_received = datetime.datetime(2020, 2, 15),

  #* BBP
  # bbp_planned_posted = datetime.datetime(2020, 5, 17),
  # bbp_actual_posted = datetime.datetime(2020, 5, 17),

  #* Notes
  # notes = "notes1"

)

test_lot_2 = LotsDirectory(
  #* Lot info
  community="Readers Branch",
  section="4",
  lot_number="8",
  product="Fulton Terrace",
  elevation="Folk Victorian",
  contract_date= datetime.datetime(2021, 12, 28),

  #* Drafting
  assigned="C.Zobel",
  draft_deadline= datetime.datetime(2021, 12, 30),
  actual= datetime.datetime(2021, 1, 26),
  time=420,

  #* Engineering
  eng = "HBS",
  eng_sent = datetime.datetime(2022, 1, 27),
  eng_planned_receipt = datetime.datetime(2022, 1, 13),
  eng_actual_receipt = datetime.datetime(2022, 2, 7),
  
  #* Plat
  plat_eng = "Bolen",
  plat_sent = datetime.datetime(2022, 1, 27),
  plat_planned_receipt = datetime.datetime(2022, 1, 13),
  plat_actual_receipt = datetime.datetime(2022, 1, 28),

  #* Permit
  permit_jurisdiction = "Goochland",
  permit_planned_submit = datetime.datetime(2022, 1, 18),
  # permit_actual_submit = datetime.datetime(2022, 5, 27),
  # permit_received = datetime.datetime(2020, 5, 27),

  #* BBP
  # bbp_planned_posted = datetime.datetime(2020, 5, 27),
  # bbp_actual_posted = datetime.datetime(2020, 5, 27),

  #* Notes
  notes = "extend front stoop, extend screened porch, 10' ceiling, diamond window, custom entry door"

)


test_lot_3 = LotsDirectory(
  #* Lot info
  community="Cypress Creek",
  section="0",
  lot_number="229",
  product="Linden III",
  elevation="Tradition",
  contract_date= datetime.datetime(2021, 12, 27),

  #* Drafting
  assigned="C.Zobel",
  draft_deadline= datetime.datetime(2021, 12, 29),
  actual= datetime.datetime(2021, 1, 14),
  time=240,

  #* Engineering
  eng = "DFI",
  eng_sent = datetime.datetime(2022, 1, 17),
  eng_planned_receipt = datetime.datetime(2022, 1, 12),
  eng_actual_receipt = datetime.datetime(2022, 2, 16),
  
  #* Plat
  plat_eng = "Hassel",
  plat_sent = datetime.datetime(2022, 1, 17),
  plat_planned_receipt = datetime.datetime(2022, 1, 12),
  plat_actual_receipt = datetime.datetime(2022, 1, 18),

  #* Permit
  permit_jurisdiction = "Isle of Wight",
  permit_planned_submit = datetime.datetime(2022, 1, 17),
  permit_actual_submit = datetime.datetime(2022, 2, 9),
  # permit_received = datetime.datetime(2020, 5, 3),

  #* BBP
  # bbp_planned_posted = datetime.datetime(2020, 5, 3),
  # bbp_actual_posted = datetime.datetime(2020, 5, 3),

  #* Notes
  notes = "attached shed"

)


# test_lot = Lot(lot_name="testname1",
# lot_date="1")


# db.session.add(test_lot)
db.session.add(test_lot_1)
db.session.add(test_lot_2)
db.session.add(test_lot_3)


db.session.commit()
