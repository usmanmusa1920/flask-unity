# from sakyum software, your (Schoolsite) project secret.py file
from pathlib import Path

db_origin = Path(__file__).resolve().parent.parent

class Config:
  SECRET_KEY = '1Xl0iT9UywGVeKz25Q26AUDb8SMJKdkNxDIBfNuXE'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///'+str(db_origin)+'/default.db'
  # set optional bootswatch theme
  FLASK_ADMIN_SWATCH = 'cerulean'
