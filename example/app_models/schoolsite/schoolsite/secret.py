# from flask_unity software, your (schoolsite) project secret.py file
from pathlib import Path

db_origin = Path(__file__).resolve().parent.parent

class Config:
  SECRET_KEY = '1VkIUrfeZaORdJGXy6wH12uaUh'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///'+str(db_origin)+'/default.db'
  # set optional bootswatch theme
  FLASK_ADMIN_SWATCH = 'cerulean'
