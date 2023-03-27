# from sakyum software, your (schoolsite) project config.py file
from flask_admin import Admin
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


  """ You will need to import models themselves before issuing `db.create_all` """
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
    admin = Admin(app, name='schoolsite')


    # rgister model to admin direct by passing every model that you
    # want to manage in admin page in the below list (reg_models)
    reg_models = [
      # User,
      # <app_model>,
    ]
    adminModelRegister(admin, reg_models, db)
    # admin model view be here!
    admin.add_view(UserAdminView(User, db.session, name="User", category="User-section"))

  admin_runner()
  return app
