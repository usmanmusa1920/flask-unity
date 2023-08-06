# from flask_unity software, your (todo_project) project routes.py file
from flask import render_template, request, redirect, url_for
from flask_login import login_user, current_user, logout_user
from flask_unity.utils import footer_style
from flask_unity.blueprint import auth
from todo_project.config import db
from .models import User
import datetime


@auth.route('/admin/login/', methods=["POST", "GET"])
def adminLogin():
  """
    the `admin_login.html` below is located in the flask_unity package (static/default_page/admin_login.html)
  """
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
  """
    the `admin_register.html` below is located in the flask_unity package (static/default_page/admin_register.html)
  """
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
