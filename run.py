"""Application entry point"""
from app import app

from app.features.autoEmail import scheduler, auto_email_job


if __name__ == "__main__":

  # scheduler.add_job(id='Auto Email job',
  #                   func=auto_email_job,
  #                   trigger='interval',
  #                   seconds=30)

  scheduler.add_job(auto_email_job, 'cron', day_of_week='1-5', hour=10, minute=50)

  scheduler.start()

  # app.run(debug=True)
  app.run(host='0.0.0.0', port=8080, debug=True)
