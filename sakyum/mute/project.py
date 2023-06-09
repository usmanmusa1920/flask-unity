# -*- coding: utf-8 -*-

from . import f1
from . import l1
from . import secure_app
from . import long_comment


def pro_init_dummy():
  return f"""from .config import create_app


app = create_app()
"""


def pro_secret_dummy():
  return f"""import os
from pathlib import Path


ORIGIN_PATH = Path(__file__).resolve().parent.parent
OS_SEP = os.path.sep # platform-specific path separator (for linux `/`, for windows `\\`)


class Config:
  SECRET_KEY = '{secure_app}'
  # The `SQLALCHEMY_DATABASE_URI` might not be compatible with windows OS,
  # change it to your windows drive like: 'C:\path\to\your\default.db'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///'+str(ORIGIN_PATH)+OS_SEP+'default.db'
  # set optional bootswatch theme
  FLASK_ADMIN_SWATCH = 'cerulean'
  UPLOAD_FOLDER = os.path.join(ORIGIN_PATH, 'media')
  ALLOWED_EXTENSIONS = ('png', 'jpg', 'jpeg')
  MAX_CONTENT_LENGTH = 16 * 1024 * 1024


def load_env():
  os.environ['FLASK_UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
  os.environ['FLASK_ORIGIN_PATH'] = str(ORIGIN_PATH)
  os.environ['FLASK_ALLOWED_EXTENSIONS'] = str(Config.ALLOWED_EXTENSIONS)
"""


def pro_config_dummy(proj_name):
  return f"""from flask_admin import Admin
from flask import Flask
from sakyum.blueprint import adminModelRegister
from sakyum.contrib import ext_lst, db
from .secret import Config


def create_app(reg_blueprints=False, conf=Config):
  app = Flask(__name__)
  app.config.from_object(conf)
  app.app_context().push()
  for ext in ext_lst:
    ext.init_app(app)


  {long_comment} You will need to import models themselves before issuing `db.create_all` {long_comment}
  from sakyum.auth.models import User
  from sakyum.auth.admin import UserAdminView
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
      # User,
      # <app_model>,
    ]
    adminModelRegister(admin, reg_models, db)
    # admin model view be here!
    admin.add_view(UserAdminView(User, db.session, name='User', category='User-section'))

  admin_runner()
  return app
"""


def pro_routes_dummy(proj):
  return f"""from flask import (render_template, Blueprint)
from sakyum import blueprint
from sakyum.utils import footer_style, template_dir, static_dir, rem_blueprint
# from <app_name>.views import <app_name>


base = Blueprint('base', __name__, template_folder=template_dir(), static_folder=static_dir('{proj}'))

rem_blue = [blueprint.default, blueprint.errors, blueprint.auth, base]
reg_blueprints = [
  blueprint.default,
  blueprint.errors,
  blueprint.auth,
  base,
  # <app_name>,
]


@base.route('/', methods=['POST', 'GET'])
def index():
  context = {f1}
    'project_name': '{proj}',
    'footer_style': footer_style,
    'blueprints_list': rem_blueprint(lst_blue=reg_blueprints, rem_blue=rem_blue),
  {l1}
  return render_template('{proj}/index.html', context=context)
  
# overwrite (customise) error pages here
"""
