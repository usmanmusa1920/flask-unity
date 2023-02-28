# from sakyum software, your (Schoolsite) project routes.py file
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, fresh_login_required, login_required
from sakyum.utils import footer_style
from sakyum.blueprint import auth
from Schoolsite.config import db, bcrypt
from .models import User


@auth.route("/admin/change/password/", methods=["POST", "GET"])
@fresh_login_required
def adminLChangePassword():
  """
    the `admin_change_password.html` below is located in the sakyum package (templates/default_page/admin_change_password.html)
  """
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
  context = {
    "head_title": "admin change password",
    "footer_style": footer_style,
  }
  return render_template("admin_change_password.html", context=context)


@auth.route("/admin/login/", methods=["POST", "GET"])
def adminLogin():
  """
    the `admin_login.html` below is located in the sakyum package (templates/default_page/admin_login.html)
  """
  if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
      """
          Parameters:
            user (object) - The user object to log in.

            remember (bool) - Whether to remember the user after their session expires. Defaults to False.

            duration (datetime.timedelta) - The amount of time before the remember cookie expires. If None the value set in the settings is used. Defaults to None.

            force (bool) - If the user is inactive, setting this to True will log them in regardless. Defaults to False.

            fresh (bool) - setting this to False will log in the user with a session marked as not “fresh”. Defaults to True.
      """
      login_user(user, remember=True)
      # if current_user.is_authenticated:
      #   return redirect(url_for("default.index"))
      flash("You are now logged in!", "success")
      return redirect(url_for("admin.index"))
    else:
      flash("Cross check your login credentials!", "error")
  context = {
    "head_title": "admin login",
    "footer_style": footer_style,
  }
  return render_template("admin_login.html", context=context)


@auth.route("/admin/register/", methods=["POST", "GET"])
def adminRegister():
  """
    the `admin_register.html` below is located in the sakyum package (templates/default_page/admin_register.html)
  """
  if request.method == "POST":
    username  = request.form["username"]
    email  = request.form["email"]
    raw_password = request.form["password"]
    
    hashed_password = bcrypt.generate_password_hash(raw_password).decode("utf-8")
    user_obj = User(username=username, email=email, password=hashed_password)
    db.session.add(user_obj)
    db.session.commit()
    flash(f"Account for {username} has been created!", "info")
    return redirect(url_for("auth.adminLogin"))
  context = {
    "head_title": "admin register",
    "footer_style": footer_style,
  }
  return render_template("admin_register.html", context=context)


@auth.route("/admin/logout/", methods=["POST", "GET"])
@login_required
def adminLogout():
  logout_user()
  flash("You logged out!", "info")
  return redirect(url_for("auth.adminLogin"))
