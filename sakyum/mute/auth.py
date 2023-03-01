# -*- coding: utf-8 -*-

from . import f1
from . import l1
from . import long_comment


def auth_init_dummy():
  return f"""from . import routes
"""


def auth_forms_dummy():
  return f"""from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from .models import User


class RegistrationForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField("Email", validators=[DataRequired(), Email()])
  password = PasswordField("Password", validators=[DataRequired()])
  confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
  submit = SubmitField("Sign Up")
  
  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError("That username is taken. Please choose a different one.")
      
  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError("That email is taken. Please choose a different one.")
      

class LoginForm(FlaskForm):
  email = StringField("Email", validators=[DataRequired(), Email()])
  password = PasswordField("Password", validators=[DataRequired()])
  remember = BooleanField("Remember Me")
  submit = SubmitField("Login")
  

class UpdateAccountForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField("Email", validators=[DataRequired(), Email()])
  picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png"])])
  submit = SubmitField("Update")

  def validate_username(self, username):
    if username.data != current_user.username:
      user = User.query.filter_by(username=username.data).first()
      if user:
        raise ValidationError("That username is taken. Please choose a different one.")

  def validate_email(self, email):
    if email.data != current_user.email:
      user = User.query.filter_by(email=email.data).first()
      if user:
        raise ValidationError("That email is taken. Please choose a different one.")
        

class RequestResetForm(FlaskForm):
  email = StringField("Email", validators=[DataRequired(), Email()])
  submit = SubmitField("Request Password Reset")

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is None:
      raise ValidationError("There is no account with that email. You must register first.")
      

class ResetPasswordForm(FlaskForm):
  password = PasswordField("Password", validators=[DataRequired()])
  confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
  submit = SubmitField("Reset Password")
"""


def auth_models_dummy(proj_name):
  return f"""from {proj_name}.config import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(255), nullable=False)
  authenticated = db.Column(db.Boolean, default=False)
  is_superuser = db.Column(db.Boolean, default=False)

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
  return f"""from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, fresh_login_required, login_required
from sakyum.utils import footer_style
from sakyum.blueprint import auth
from {proj_name}.config import db, bcrypt
from .models import User


@auth.route("/admin/change/password/", methods=["POST", "GET"])
@fresh_login_required
def adminChangePassword():
  {long_comment}
    the `admin_change_password.html` below is located in the sakyum package (templates/default_page/admin_change_password.html)
  {long_comment}
  if request.method == "POST":
    old_password = request.form["old_password"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    user = User.query.filter_by(username=current_user.username).first()
    if user and bcrypt.check_password_hash(user.password, old_password):
      if password1 == password2:
        hashed_password = bcrypt.generate_password_hash(password2).decode("utf-8")
        user.password = hashed_password
        db.session.commit()
      flash("Your password has changed!", "success")
      return redirect(url_for("auth.adminLogin"))
    else:
      flash("Cross check your login credentials!", "error")
  context = {f1}
    "head_title": "admin change password",
    "footer_style": footer_style,
  {l1}
  return render_template("admin_change_password.html", context=context)


@auth.route("/admin/login/", methods=["POST", "GET"])
def adminLogin():
  {long_comment}
    the `admin_login.html` below is located in the sakyum package (templates/default_page/admin_login.html)
  {long_comment}
  if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
      {long_comment}
          Parameters:
            user (object) - The user object to log in.

            remember (bool) - Whether to remember the user after their session expires. Defaults to False.

            duration (datetime.timedelta) - The amount of time before the remember cookie expires. If None the value set in the settings is used. Defaults to None.

            force (bool) - If the user is inactive, setting this to True will log them in regardless. Defaults to False.

            fresh (bool) - setting this to False will log in the user with a session marked as not “fresh”. Defaults to True.
      {long_comment}
      login_user(user, remember=True)
      # if current_user.is_authenticated:
      #   return redirect(url_for("default.index"))
      flash("You are now logged in!", "success")
      return redirect(url_for("admin.index"))
    else:
      flash("Cross check your login credentials!", "error")
  context = {f1}
    "head_title": "admin login",
    "footer_style": footer_style,
  {l1}
  return render_template("admin_login.html", context=context)


@auth.route("/admin/register/", methods=["POST", "GET"])
def adminRegister():
  {long_comment}
    the `admin_register.html` below is located in the sakyum package (templates/default_page/admin_register.html)
  {long_comment}
  if request.method == "POST":
    username  = request.form["username"]
    email  = request.form["email"]
    raw_password = request.form["password"]
    
    hashed_password = bcrypt.generate_password_hash(raw_password).decode("utf-8")
    user_obj = User(username=username, email=email, password=hashed_password)
    db.session.add(user_obj)
    db.session.commit()
    flash(f"Account for {f1}username{l1} has been created!", "info")
    return redirect(url_for("auth.adminLogin"))
  context = {f1}
    "head_title": "admin register",
    "footer_style": footer_style,
  {l1}
  return render_template("admin_register.html", context=context)


@auth.route("/admin/logout/", methods=["POST", "GET"])
@login_required
def adminLogout():
  logout_user()
  flash("You logged out!", "info")
  return redirect(url_for("auth.adminLogin"))
"""
