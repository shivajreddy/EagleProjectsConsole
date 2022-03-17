from Models.Lot import LotsDirectory, Lot
from database.psql_db import db, connect_psqldb

db.drop_all()
db.create_all()

LotsDirectory.query.delete()
Lot.query.delete()

test_lot_1 = LotsDirectory(community="c1",
section="s1",
lot_number="ln1",
product="p1",
elevation="e1",
contract_date="cd1",

assigned="a1",
draft_deadline="dl1",
actual="a1",
time=21,

)

test_lot = Lot(lot_name="testname1",
lot_date="1")



db.session.add(test_lot)
# db.session.add(test_lot_1)

db.session.commit()