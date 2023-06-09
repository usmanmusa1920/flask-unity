# -*- coding: utf-8 -*-

import os
import secrets
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, flash, send_from_directory, send_file
from flask_login import login_user, current_user, logout_user, fresh_login_required, login_required
from sakyum.utils import footer_style
from sakyum.blueprint import auth
from sakyum.contrib import db, bcrypt
from .models import User
from .forms import LoginForm, ChangePasswordForm, RegisterForm


OS_SEP = os.path.sep # platform-specific path separator (for linux `/`, for windows `\\`)
UPLOAD_FOLDER = os.environ.get('FLASK_UPLOAD_FOLDER')
ORIGIN_PATH = os.environ.get('FLASK_ORIGIN_PATH')
ALLOWED_EXTENSIONS = os.environ.get('FLASK_ALLOWED_EXTENSIONS')


@auth.route('/admin/register/', methods=['POST', 'GET'])
@login_required
def adminRegister():
  form = RegisterForm()
  if form.validate_on_submit():
    username  = form.username.data
    email  = form.email.data
    raw_password2 = form.confirm_password.data
    hashed_password = bcrypt.generate_password_hash(raw_password2).decode('utf-8')
    user = User(username=username, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash('Your created new user, the user is able to log in', 'success')
    return redirect(url_for('auth.adminLogin'))
  context = {
    'head_title': 'admin register',
    'footer_style': footer_style,
    'form': form,
  }
  return render_template('admin_register.html', context=context)
  

@auth.route('/admin/login/', methods=['POST', 'GET'])
def adminLogin():
  if current_user.is_authenticated:
    return redirect(url_for('base.index'))
  form = LoginForm()
  if form.validate_on_submit():
    username = form.username.data
    password = form.password.data
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
      login_user(user, remember=True)
      flash('You are now logged in!', 'success')
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('admin.index'))
    else:
      flash('Login Unsuccessful. Please check username and password', 'error')
  context = {
    'head_title': 'admin login',
    'footer_style': footer_style,
    'form': form,
  }
  return render_template('admin_login.html', context=context)
  

@auth.route('/admin/change/password/', methods=['POST', 'GET'])
@fresh_login_required
def adminChangePassword():
  """
  The `admin_change_password.html` below is located in the sakyum package (templates/default_page/admin_change_password.html)
  """
  form = ChangePasswordForm()
  if request.method == 'POST':
    old_password = form.old_password.data
    password1 = form.password1.data
    password2 = form.password2.data
    user = User.query.filter_by(username=current_user.username).first()
    if user and bcrypt.check_password_hash(user.password, old_password):
      if password1 == password2:
        hashed_password = bcrypt.generate_password_hash(password2).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        logout_user()
        flash('Your password has changed!', 'succes')
        return redirect(url_for('auth.adminLogin'))
      else:
        flash('The two password fields didn`t match!', 'error')
    else:
      flash('Cross check your login credentials!', 'error')
  context = {
    'head_title': 'admin change password',
    'footer_style': footer_style,
    'form': form,
  }
  return render_template('admin_change_password.html', context=context)
  

@auth.route('/admin/logout/', methods=['POST', 'GET'])
@login_required
def adminLogout():
  logout_user()
  flash('You logged out!', 'info')
  return redirect(url_for('auth.adminLogin'))
  

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
  

@auth.route('/profile_image/<path:filename>')
@login_required
def profile_image(filename):
  """
  This function help to show current user profile image, it won't download it
  like the `download_file` function below does
  """
  return send_file(UPLOAD_FOLDER + OS_SEP + filename)
  

@auth.route('/media/<path:filename>')
@login_required
def download_file(filename):
  """
  If we use this to show current user profile image, it won't show instead it will download it,
  so it meant for downloading media file
  """
  return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)
  

def picture_name(pic_name):
  random_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(pic_name)
  picture_fn = random_hex + f_ext
  new_name = _ + '_' + picture_fn
  return new_name
  

@auth.route('/admin/change_profile_image/', methods=['POST', 'GET'])
@login_required
def changeProfileImage():
  if request.method == 'POST':
    # check if the post request has the file part
    if 'file' not in request.files:
      flash('No file part')
      return redirect(request.url)
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
      flash('No selected file')
      return redirect(request.url)
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file_name = picture_name(filename)
      file.save(os.path.join(UPLOAD_FOLDER, file_name))
      user = User.query.filter_by(username=current_user.username).first()
      if user:
        if user.user_img != 'default_img.png':
          r = str(ORIGIN_PATH) + OS_SEP + 'media' + OS_SEP + user.user_img
          if os.path.exists(r):
            os.remove(r)
        user.user_img = file_name
        db.session.commit()
      flash('Your profile image has been changed!', 'success')
      return redirect(url_for('base.index')) # it will redirect to the home page
  context = {
    'head_title': 'admin change profile image',
    'footer_style': footer_style,
  }
  return render_template('admin_change_profile_image.html', context=context)
