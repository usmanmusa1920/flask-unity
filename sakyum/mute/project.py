# -*- coding: utf-8 -*-

from sakyum.utils import Security


secret = Security()
secure_app = secret.passcode_salt
f1 = "{"
l1 = "}"
long_comment = "\"\"\""


def pro_init_dummy():
  return f"""from .config import create_app
from .config import db

app = create_app()
"""


def pro_secret_dummy():
  return f"""from pathlib import Path

db_origin = Path(__file__).resolve().parent.parent

class Config:
  SECRET_KEY = '{secure_app}'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///'+str(db_origin)+'/default.db'
  # set optional bootswatch theme
  FLASK_ADMIN_SWATCH = 'cerulean'
"""


def pro_config_dummy(proj_name):
  return f"""from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from sakyum.blueprint import adminModelRegister
from .secret import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = 'auth.adminLogin'
login_manager.login_message_category = 'info'
login_manager.login_message = u"You must login, in other to get access to that page"


def create_app(reg_blueprints=False, conf=Config):
  app = Flask(__name__)
  app.config.from_object(conf)
  app.app_context().push()
  db.init_app(app)
  bcrypt.init_app(app)
  login_manager.init_app(app)


  {long_comment} You will need to import models themselves before issuing `db.create_all` {long_comment}
  from auth.models import User
  # from <app_name>.models import <app_model>
  # from <app_name>.admin import <admin_model_view>
  db.create_all() # method to create the tables and database
  

  if reg_blueprints:
    for reg_blueprint in reg_blueprints:
      app.register_blueprint(reg_blueprint)


  def admin_runner():
    # Model views allow you to add a dedicated set of admin
    # pages for managing any model in your database
    admin = Admin(app, name='{proj_name}')


    # rgister model to admin direct by passing every model that you
    # want to manage in admin page in the below list (reg_models)
    reg_models = [
      User,
      # <app_model>,
    ]
    adminModelRegister(admin, reg_models, db)
    # admin model view be here!

  admin_runner()
  return app
"""


def pro_routes_dummy(proj):
  return f"""from flask import (render_template, Blueprint)
from sakyum.utils import footer_style, template_dir, static_dir, rem_blueprint
from sakyum.blueprint import default, errors, auth
from flask import render_template
# from <app_name>.views import <app_name>


base = Blueprint("base", __name__, template_folder=template_dir(), static_folder=static_dir("{proj}"))

rem_blue = [default, errors, auth, base]
reg_blueprints = [
  default,
  errors,
  auth,
  base,
  # <app_name>,
]


@default.route('/', methods=["POST", "GET"])
def index():
  context = {f1}
    "project_name": "{proj}",
    "footer_style": footer_style,
    "blueprints_list": rem_blueprint(lst_blue=reg_blueprints, rem_blue=rem_blue),
  {l1}
  return render_template("{proj}/index.html", context=context)
  
  
{long_comment} overwrite error pages here {long_comment}
"""
