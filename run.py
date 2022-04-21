"""Application entry point"""
from app import app

from flask_apscheduler import APScheduler
scheduler = APScheduler()

def my_tasks_func():
  print("this is the task")

if __name__ == "__main__":

  scheduler.add_job(id='schedule task', func=my_tasks_func, trigger='interval', seconds=5)
  scheduler.start()

  app.run(host='0.0.0.0', port=8080, debug=True)