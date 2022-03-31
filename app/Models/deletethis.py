from datetime import date, time, datetime


resp = "Thu, 14 Feb 2019 00:00:00 GMT"



dt_object = datetime.strptime(
  resp, '%a, %d %b %Y %H:%M:%S %Z')


my_date = dt_object.date()

print(type(my_date))