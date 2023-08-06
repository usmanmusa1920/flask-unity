# -*- coding: utf-8 -*-

f1 = "{"
l1 = "}"
long_comment = "\"\"\""


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
  username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')
  
  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('That username is taken. Please choose a different one.')
      
  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError('That email is taken. Please choose a different one.')
      

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')
  

class UpdateAccountForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
  submit = SubmitField('Update')

  def validate_username(self, username):
    if username.data != current_user.username:
      user = User.query.filter_by(username=username.data).first()
      if user:
        raise ValidationError('That username is taken. Please choose a different one.')

  def validate_email(self, email):
    if email.data != current_user.email:
      user = User.query.filter_by(email=email.data).first()
      if user:
        raise ValidationError('That email is taken. Please choose a different one.')
        

class RequestResetForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  submit = SubmitField('Request Password Reset')

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is None:
      raise ValidationError('There is no account with that email. You must register first.')
      

class ResetPasswordForm(FlaskForm):
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Reset Password')
"""


def auth_models_dummy(proj_name):
  return f"""from flask import current_app
from {proj_name}.config import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)
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
  return f"""from flask import render_template, request, redirect, url_for
from flask_login import login_user, current_user, logout_user
from flask_unity.utils import footer_style
from flask_unity.blueprint import auth
from {proj_name}.config import db
from .models import User
import datetime


@auth.route('/admin/login/', methods=["POST", "GET"])
def adminLogin():
  {long_comment}
    the `admin_login.html` below is located in the flask_unity package (static/default_page/admin_login.html)
  {long_comment}
  if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    user = User.query.filter_by(username=username).first()
    if user and user.username == username and user.password == password:
      login_user(user, remember=True)
      # if current_user.is_authenticated:
      #   return redirect(url_for("default.index"))
      return redirect(url_for("admin.index"))
  return render_template("admin_login.html", footer_style=footer_style)


@auth.route('/admin/register/', methods=["POST", "GET"])
def adminRegister():
  {long_comment}
    the `admin_register.html` below is located in the flask_unity package (static/default_page/admin_register.html)
  {long_comment}
  if request.method == "POST":
    username  = request.form["username"]
    email  = request.form["email"]
    password = request.form["password"]
    user_obj = User(username=username, email=email, password=password)
    db.session.add(user_obj)
    db.session.commit()
    return redirect(url_for("auth.adminLogin"))
  return render_template("admin_register.html", footer_style=footer_style)


@auth.route('/admin/logout/', methods=["POST", "GET"])
def adminLogout():
  logout_user()
  return redirect(url_for("auth.adminLogin"))
"""
