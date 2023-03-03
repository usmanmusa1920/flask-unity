# from sakyum software, your (Schoolsite) project secret.py file
from pathlib import Path

db_origin = Path(__file__).resolve().parent.parent

class Config:
  SECRET_KEY = 'tNOU5Xdn7gzeVHIEYj33'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///'+str(db_origin)+'/default.db'
  # set optional bootswatch theme
  FLASK_ADMIN_SWATCH = 'cerulean'
