# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
# To enable CSRF protection globally for Flask, using secret key to securely sign the token
csrf = CSRFProtect()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.adminLogin'
login_manager.login_message_category = 'info'
login_manager.login_message = u'You must login, in other to get access to that page'
ext_lst = [db, bcrypt, login_manager, csrf]
