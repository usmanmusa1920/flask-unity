# from sakyum software, your (sakyum_blog) project config.py file
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask import Flask
from pathlib import Path
from flask_login import LoginManager
from flask_mail import Mail

db_ORIGIN = Path(__file__).resolve().parent.parent

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = 'algU1S1ZWXBqX7RcI2FKH4eAZJCb85JMykBTn9hER'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+str(db_ORIGIN)+'/default.db'

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
mail = Mail(app)


""" You will need to import models themselves before issuing `db.create_all` """
from blog.models import Post
from users.models import User
db.create_all() # method to create the tables and database


"""
Model views allow you to add a dedicated set of admin
pages for managing any model in your database
"""
admin = Admin(app, name='sakyum_blog')


"""
Register your model, by passing every model that you want
to manage in admin page in the below list (reg_models)
"""
reg_models = [Post, User]
for reg_model in reg_models:
  admin.add_view(ModelView(reg_model, db.session))
