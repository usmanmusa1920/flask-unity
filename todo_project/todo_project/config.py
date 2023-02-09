# from sakyum software, your (todo_project) project config.py file
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask import Flask
from pathlib import Path

db_ORIGIN = Path(__file__).resolve().parent.parent

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'Mj7haL5lNAUuZbVkkOhqRsyBKci0TXHPFpDfrHd3m1c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+str(db_ORIGIN)+'/default.db'

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

db = SQLAlchemy(app)

""" You will need to import models themselves before issuing `db.create_all` """
from todo_app.models import QuestionModel, ChoiceModel
db.create_all() # method to create the tables and database

"""
  Model views allow you to add a dedicated set of admin
  pages for managing any model in your database
"""

admin = Admin(app, name='todo_project')
admin.add_view(ModelView(QuestionModel, db.session))
admin.add_view(ModelView(ChoiceModel, db.session))
