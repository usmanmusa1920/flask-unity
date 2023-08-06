# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User


class RegisterForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  # picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
  password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password'), Length(min=6)])
  
  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationError('That username is taken. Please choose a different one.')
      
  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user:
      raise ValidationError('That email is taken. Please choose a different one.')
      

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
  
  
class ChangePasswordForm(FlaskForm):
  old_password = PasswordField('Old Password', validators=[DataRequired(), Length(min=6)])
  password1 = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
  password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password1'), Length(min=6)])
