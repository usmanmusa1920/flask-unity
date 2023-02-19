# from sakyum software, your (todo_project) project config.py file
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask import Flask
from pathlib import Path
from flask_login import LoginManager

db_ORIGIN = Path(__file__).resolve().parent.parent

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'p1RPtQgR6FjdMIW5AMWQJL2ToEwCZucadSkLG8SlNer2qn'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+str(db_ORIGIN)+'/default.db'

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
# login_manager.session_protection = "strong"
login_manager.login_view = 'auth.adminLogin'
login_manager.login_message_category = 'info'


""" You will need to import models themselves before issuing `db.create_all` """
from auth.models import User
from todo_app.models import Todo_appQuestionModel, Todo_appChoiceModel
from todo_app.admin import QuestionChoiceAdminView
db.create_all() # method to create the tables and database


def admin_runner():
  """
  Model views allow you to add a dedicated set of admin
  pages for managing any model in your database
  """
  admin = Admin(app, name='todo_project')


  """
  Register your model, by passing every model that you want
  to manage in admin page in the below list (reg_models)
  """
  reg_models = [
    User,
  ]
  for reg_model in reg_models:
    admin.add_view(ModelView(reg_model, db.session))
    
  """
    register your custom admin here, like we register `QuestionChoiceAdminView`
    if you are stuck visit:
      https://flask-admin.readthedocs.io/en/latest/introduction/#getting-started
  """

  admin.add_view(QuestionChoiceAdminView(Todo_appQuestionModel, db.session, name="Questions", category="Question-Choice"))
  admin.add_view(QuestionChoiceAdminView(Todo_appChoiceModel, db.session, name="Choices", category="Question-Choice"))
