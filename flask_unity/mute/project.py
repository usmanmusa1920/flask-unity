# -*- coding: utf-8 -*-

from flask_unity.utils import Security


secret = Security()
secure_app = secret.passcode_salt
long_comment = "\"\"\""


def pro_init_dummy():
  return f"""import auth
from .routes import base
from .config import app, db
"""


def pro_config_dummy(proj_name, secure_app=secure_app, long_comment=long_comment):
  return f"""from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask import Flask
from pathlib import Path
from flask_login import LoginManager


db_ORIGIN = Path(__file__).resolve().parent.parent
app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '{secure_app}'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+str(db_ORIGIN)+'/default.db'

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
# login_manager.session_protection = "strong"
login_manager.login_view = 'auth.adminLogin'
login_manager.login_message_category = 'info'


{long_comment} You will need to import models themselves before issuing `db.create_all` {long_comment}
from auth.models import User
# from todo_app.models import Todo_appQuestionModel, Todo_appChoiceModel
# from todo_app.admin import QuestionChoiceAdminView
db.create_all() # method to create the tables and database


def admin_runner():
  {long_comment} Model views allow you to add a dedicated set of admin
    pages for managing any model in your database {long_comment}
  admin = Admin(app, name='{proj_name}')


  {long_comment} Register your model, by passing every model that you want
    to manage in admin page in the below list (reg_models) {long_comment}
  reg_models = [
    User,
  ]
  for reg_model in reg_models:
    admin.add_view(ModelView(reg_model, db.session))
    

  {long_comment} If you want to customise how your model is going to be, don't put (pass) it in the
    above `reg_models` list. Instead create a model view class in your app admin.py
    file and import it (in this module) `config.py` above the `db.create_all()` then come
    below this comment and register it just like the way we did for the commented ones

    register your custom admin model view here, like we register `QuestionChoiceAdminView`
    if you are stuck visit:
      https://flask-admin.readthedocs.io/en/latest/introduction/#getting-started {long_comment}

      
  # admin.add_view(QuestionChoiceAdminView(Todo_appQuestionModel, db.session, name="Questions", category="Question-Choice"))
  # admin.add_view(QuestionChoiceAdminView(Todo_appChoiceModel, db.session, name="Choices", category="Question-Choice"))
"""


def pro_routes_dummy(proj):
  return f"""from flask import (render_template, Blueprint)
from flask_unity.utils import footer_style, template_dir, static_dir
from flask_unity.blueprint import default, errors, auth
from flask import render_template
# from <app_name>.views import <app_name>


base = Blueprint("base", __name__, template_folder=template_dir(), static_folder=static_dir("{proj}"))


{long_comment}
  register your app after importing it blueprint from the app views.py file,
  by passing (append) your app blueprint that you import
  into the `reg_blueprints` list below,
  
  warning:
      don\'t ommit the registered blueprint you see in  the list (default, errors, auth, base) blueprints
{long_comment}

reg_blueprints = [
  default,
  errors,
  auth,
  base,
]

def rem_blueprint(lst_blue):
  # these are blueprint that we don't want to show on the
  # default page so we are removing them from the list

  rem_blue = [default, errors, auth, base]
  for blue in rem_blue:
    if blue in lst_blue:
      # finding the index of the `blue` item blueprint in the list
      err_index = lst_blue.index(blue)
      # removing it `blue` item from the list using it index number
      lst_blue.pop(err_index)
  blueprints_list = lst_blue
  return blueprints_list


@default.route('/')
def index():
  # the default_base.html below is located in the flask_unity package (templates/default_page) folder
  return render_template("default_base.html", project_name="{proj}", blueprints_list=rem_blueprint(reg_blueprints), footer_style=footer_style)
  
  
{long_comment} overwrite error pages here {long_comment}
"""
