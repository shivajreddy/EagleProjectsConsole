"""Application entry point"""
from app import app

from app.features.autoEmail import scheduler, auto_email_job

def printjob():
  print('this is a job')

if __name__ == "__main__":

  print("going to start the schedulers")
  scheduler.add_job(id='Auto Email job',
                    func=printjob,
                    trigger='interval',
                    seconds=5)

  # scheduler.add_job(auto_email_job, 'cron', day_of_week='1-5', hour=8, minute=15)

  scheduler.start()

  print("going to start the app now")
  # app.run(debug=True)
  app.run(host='0.0.0.0', port=8080, debug=True)
