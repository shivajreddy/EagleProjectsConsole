from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_psqldb(app):
  """Connect to PSQL DB"""

  db.app = app
  db.init_app(app)
