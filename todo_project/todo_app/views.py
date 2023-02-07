# from sakyum software, your app (todo_app) views.py file
from todo_project import app
from flask import (render_template, Blueprint, url_for, flash, redirect)
from sakyum.utils import template_dir, static_dir
# from .forms import RegistrationForm, LoginForm

todo_app = Blueprint("todo_app", __name__, template_folder=template_dir(), static_folder=static_dir("todo_app"))

# @todo_app.route('/')
# def index():
#   return "<h1>todo_app index page</h1>"

@todo_app.route('/todo_app')
def index():
  return render_template("todo_app/index.html")

# @todo_app.route('/register', methods=["GET", "POST"])
# def register():
#   form = RegistrationForm()
#   if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('todo_app.index'))
#   return render_template("todo_app/register.html", form=form)

# @todo_app.route('/login', methods=["GET", "POST"])
# def login():
#   form = LoginForm()
#   if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('todo_app.index'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#   return render_template("todo_app/login.html", form=form)
