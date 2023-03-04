# from sakyum software, your (Schoolsite) project secret.py file
from pathlib import Path

db_origin = Path(__file__).resolve().parent.parent

class Config:
  SECRET_KEY = '8xacCWoGqhhwL7EtDEGwkW'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///'+str(db_origin)+'/default.db'
  # set optional bootswatch theme
  FLASK_ADMIN_SWATCH = 'cerulean'
