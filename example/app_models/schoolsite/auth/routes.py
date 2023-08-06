# from flask_unity software, your (schoolsite) project auth routes.py file
from flask import render_template, request, redirect, url_for, flash, Blueprint
from flask_login import login_user, current_user, logout_user, fresh_login_required, login_required
from flask_unity.utils import footer_style, template_dir, static_dir
from flask_unity.blueprint import auth
from schoolsite.config import db, bcrypt
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
  context = {
    "head_title": "admin register",
    "footer_style": footer_style,
    "form": form,
  }
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
  context = {
    "head_title": "admin login",
    "footer_style": footer_style,
    "form": form,
  }
  return render_template("admin_login.html", context=context)


@auth.route("/admin/change/password/", methods=["POST", "GET"])
@fresh_login_required
def adminChangePassword():
  """
    the `admin_change_password.html` below is located in the flask_unity package (templates/default_page/admin_change_password.html)
  """
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
  context = {
    "head_title": "admin change password",
    "footer_style": footer_style,
    "form": form,
  }
  return render_template("admin_change_password.html", context=context)


@auth.route("/admin/logout/", methods=["POST", "GET"])
@login_required
def adminLogout():
  logout_user()
  flash("You logged out!", "info")
  return redirect(url_for("auth.adminLogin"))
