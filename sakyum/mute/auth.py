# -*- coding: utf-8 -*-

from . import f1
from . import l1
from . import long_comment


def auth_init_dummy():
  return f"""from . import routes
"""


def auth_forms_dummy():
  return f"""from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User


class RegisterForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired(), Length(min=2, max=30)])
  email = StringField("Email", validators=[DataRequired(), Email()])
  password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
  confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password"), Length(min=6)])
  
  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError("That username is taken. Please choose a different one.")
      
  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError("That email is taken. Please choose a different one.")
      

class LoginForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
  password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
  
  
class ChangePasswordForm(FlaskForm):
  old_password = PasswordField("Old Password", validators=[DataRequired(), Length(min=6)])
  password1 = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
  password2 = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password1"), Length(min=6)])
"""


def auth_models_dummy(proj_name):
  return f"""from datetime import datetime
from {proj_name}.config import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  username = db.Column(db.String(20), unique=True, nullable=False)
  user_img = db.Column(db.String(255), default='default_img.png')
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(255), nullable=False)
  authenticated = db.Column(db.Boolean, default=False)
  is_superuser = db.Column(db.Boolean, default=False)
  is_admin = db.Column(db.Boolean, default=False)

  def is_active(self):
    {long_comment}True, as all users are active.{long_comment}
    return True

  def get_id(self):
    {long_comment}Return the user id to satisfy Flask-Login's requirements.{long_comment}
    return self.id

  def is_authenticated(self):
    {long_comment}Return True if the user is authenticated.{long_comment}
    return self.authenticated

  def is_anonymous(self):
    {long_comment}False, as anonymous users aren't supported.{long_comment}
    return False

  def __repr__(self):
    return f"User('{f1}self.username{l1}', '{f1}self.email{l1}'"
"""


def auth_routes_dummy(proj_name):
  return f"""from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_login import login_user, current_user, logout_user, fresh_login_required, login_required
from sakyum.utils import footer_style, template_dir, static_dir
from sakyum.blueprint import auth
from {proj_name}.config import db, bcrypt
from .models import User
from .forms import LoginForm, ChangePasswordForm, RegisterForm


auth2 = Blueprint("auth2", __name__, template_folder=template_dir(), static_folder=static_dir("auth"))


@auth.route("/admin/register/", methods=["POST", "GET"])
@login_required
def adminRegister():
  form = RegisterForm()
  if form.validate_on_submit():
    username  = form.username.data
    email  = form.email.data
    raw_password2 = form.confirm_password.data
    hashed_password = bcrypt.generate_password_hash(raw_password2).decode("utf-8")
    user = User(username=username, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash("Your created new user, the user is able to log in", "success")
    return redirect(url_for("auth.adminLogin"))
  context = {f1}
    "head_title": "admin register",
    "footer_style": footer_style,
    "form": form,
  {l1}
  return render_template("admin_register.html", context=context)


@auth.route("/admin/login/", methods=["POST", "GET"])
def adminLogin():
  if current_user.is_authenticated:
    return redirect(url_for("base.index"))
  form = LoginForm()
  if form.validate_on_submit():
    username = form.username.data
    password = form.password.data
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
      login_user(user, remember=True)
      flash("You are now logged in!", "success")
      next_page = request.args.get("next")
      return redirect(next_page) if next_page else redirect(url_for("admin.index"))
    else:
      flash("Login Unsuccessful. Please check username and password", "error")
  context = {f1}
    "head_title": "admin login",
    "footer_style": footer_style,
    "form": form,
  {l1}
  return render_template("admin_login.html", context=context)


@auth.route("/admin/change/password/", methods=["POST", "GET"])
@fresh_login_required
def adminChangePassword():
  {long_comment}
    the `admin_change_password.html` below is located in the sakyum package (templates/default_page/admin_change_password.html)
  {long_comment}
  form = ChangePasswordForm()
  if request.method == "POST":
    old_password = form.old_password.data
    password1 = form.password1.data
    password2 = form.password2.data
    user = User.query.filter_by(username=current_user.username).first()
    if user and bcrypt.check_password_hash(user.password, old_password):
      if password1 == password2:
        hashed_password = bcrypt.generate_password_hash(password2).decode("utf-8")
        user.password = hashed_password
        db.session.commit()
        logout_user()
        flash("Your password has changed!", "succes")
        return redirect(url_for("auth.adminLogin"))
      else:
        flash("The two password fields didn't match!", "error")
    else:
      flash("Cross check your login credentials!", "error")
  context = {f1}
    "head_title": "admin change password",
    "footer_style": footer_style,
    "form": form,
  {l1}
  return render_template("admin_change_password.html", context=context)


@auth.route("/admin/logout/", methods=["POST", "GET"])
@login_required
def adminLogout():
  logout_user()
  flash("You logged out!", "info")
  return redirect(url_for("auth.adminLogin"))
"""

def auth_admin_dummy():
  return f"""from flask_login import current_user
from flask import redirect, request, url_for
from flask_admin.contrib.sqla import ModelView


class UserAdminView(ModelView):
  can_delete = True  # enable model deletion
  can_create = True  # enable model deletion
  can_edit = True  # enable model deletion
  page_size = 50  # the number of entries to display on the list view

  # This is used to list the various columns in the order you want them.
  column_list = ('username', 'email', 'password', 'date_created', 'authenticated', 'is_superuser')
  # Columns that you want to be searchable in the model.
  column_searchable_list = ('username', 'email', 'password', 'date_joined', 'authenticated', 'is_superuser')
  # The column that the view should be sorted with by default (when the view is loaded for
  # the first time). The second parameter True tells flask-admin to sort it in descending order.
  column_default_sort = ('username', True)
  # List of columns that can be used to filter.
  column_filters = ('username',)

  def is_accessible(self):
    return current_user.is_authenticated

  def inaccessible_callback(self, name, **kwargs):
    # redirect to login page if user doesn't have access
    return redirect(url_for('auth.adminLogin', next=request.url))
"""
