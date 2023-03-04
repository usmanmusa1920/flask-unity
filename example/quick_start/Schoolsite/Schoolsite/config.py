# from sakyum software, your (Schoolsite) project config.py file
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from sakyum.blueprint import adminModelRegister
from .secret import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
# To enable CSRF protection globally for Flask, using secret key to securely sign the token
csrf = CSRFProtect()
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
  csrf.init_app(app)


  """ You will need to import models themselves before issuing `db.create_all` """
  from auth.models import User
  from auth.admin import UserAdminView
  # from <app_name>.models import <app_model>
  # from <app_name>.admin import <admin_model_view>
  db.create_all() # method to create the tables and database
  

  if reg_blueprints:
    for reg_blueprint in reg_blueprints:
      app.register_blueprint(reg_blueprint)


  def admin_runner():
    # Model views allow you to add a dedicated set of admin
    # pages for managing any model in your database
    admin = Admin(app, name='Schoolsite')


    # rgister model to admin direct by passing every model that you
    # want to manage in admin page in the below list (reg_models)
    reg_models = [
      # User,
      # <app_model>,
    ]
    adminModelRegister(admin, reg_models, db)
    # admin model view be here!
    admin.add_view(UserAdminView(User, db.session, name="Auth", category="Auth-section"))

  admin_runner()
  return app
