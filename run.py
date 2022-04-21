"""Application entry point"""
from app import app

# from flask_apscheduler import APScheduler
# scheduler = APScheduler()

from app.features.autoreport import scheduler, job

# def my_tasks_func():
  # print("this is the task")

if __name__ == "__main__":

  # scheduler.add_job(id='schedule task', func=job, trigger='interval', seconds=30)
  # scheduler.start()

  app.run(host='0.0.0.0', port=8080, debug=True)