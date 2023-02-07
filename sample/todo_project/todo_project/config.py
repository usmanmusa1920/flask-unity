# from sakyum software, your (todo_project) project config.py file
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from pathlib import Path
from os import path

db_ORIGIN = Path(__file__).resolve().parent.parent

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'V4y3LIBY4AiPzO2GlRjv0fbcKJN1i7EB9aKo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+str(db_ORIGIN)+'/default.db'

db = SQLAlchemy(app)

if path.exists(str(db_ORIGIN) + '/default.db'):
  pass # if default.db exist just pass
else:
  """ You will need to import models themselves before issuing `db.create_all` """
  # from <app_name>.models import <app_model>
  db.create_all() # create db file
# db.init_app(app)
