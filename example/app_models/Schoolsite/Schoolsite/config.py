# from sakyum software, your (Schoolsite) project config.py file
from flask_sqlalchemy import SQLAlchemy
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


  """ You will need to import models themselves before issuing `db.create_all` """
  from auth.models import User
  from exam.models import ExamQuestionModel, ExamChoiceModel
  from exam.admin import QuestionChoiceAdminView
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
      User,
      # ExamQuestionModel,
      # ExamChoiceModel,
    ]
    adminModelRegister(admin, reg_models, db)
    admin.add_view(QuestionChoiceAdminView(ExamChoiceModel, db.session, name="Questions", category="Question-Choice"))
    admin.add_view(QuestionChoiceAdminView(ExamQuestionModel, db.session, name="Choices", category="Question-Choice"))# admin model view be here!

  admin_runner()
  return app
