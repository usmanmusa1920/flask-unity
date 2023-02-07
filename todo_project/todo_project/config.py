# from sakyum software, your (todo_project) project config.py file
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask import Flask
from pathlib import Path

db_ORIGIN = Path(__file__).resolve().parent.parent

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'nUxoxfrMvtlFhJIlPc986DkN7PNgTQisaR98enjMXA3zCqVwWm6YXTO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+str(db_ORIGIN)+'/default.db'

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

db = SQLAlchemy(app)

""" You will need to import models themselves before issuing `db.create_all` """
from todo_app.models import TodoListModel
db.create_all() # method to create the tables and database

# Flask and Flask-SQLAlchemy initialization here

admin = Admin(app, name='sakyum', template_mode='bootstrap3')
admin.add_view(ModelView(TodoListModel, db.session))
