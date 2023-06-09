# -*- coding: utf-8 -*-

from datetime import datetime
from sakyum.contrib import db, login_manager
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
    """True, as all users are active."""
    return True

  def get_id(self):
    """Return the user id to satisfy Flask-Login`s requirements."""
    return self.id

  def is_authenticated(self):
    """Return True if the user is authenticated."""
    return self.authenticated

  def is_anonymous(self):
    """False, as anonymous users aren`t supported."""
    return False

  def __repr__(self):
    return f'User(\'{self.username}\', \'{self.email}\')'
