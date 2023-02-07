# -*- coding: utf-8 -*-

from . import __title__
from . import __version__
from .utils import stylePage, Security

secret = Security()
secure_app = secret.passcode_salt

f1 = "{"
l1 = "}"
f2 = "{{"
l2 = "}}"


def _html(name, static_url=None, is_base=True, f1=f1, l1=l1, f2=f2, l2=l2):
  if is_base:
    _is = "application"
    static_url = name
  else:
    _is = "project"
    static_url = "base"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="shortcut icon" href="{f2} url_for('base.static', filename='/media/favicon.ico') {l2}" type="image/x-icon">
  <link rel="stylesheet" type="text/css" href="{f2} url_for('{static_url}.static', filename='style.css') {l2}">
  {f1}% block head %{l1}
    <!-- child css file link -->
  {f1}% endblock head %{l1}
  <script type="text/javascript" src="{f2} url_for('{static_url}.static', filename='index.js') {l2}"></script>
  <script src="main.js"></script>
  <title>Sakyum - {name}</title>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="header_col">
        <div class="head_left">
          <h1 class="logo">
            <a href="/">Sakyum</a>
          </h1>
        </div>

        <div class="head_right">
          <a href="https://github.com/usmanmusa1920/sakyum" class="link_0" target="_blank">Github</a>
          <a class="link_1">|</a>
          <a href="https://github.com/usmanmusa1920/sakyum#readme" class="link_2" target="_blank">Docs</a>
          <a href="https://github.com/usmanmusa1920/sakyum#readme" class="link_3" target="_blank">Install</a>
          <a onclick="test()" class="alert">
            <img src="{f2} url_for('base.static', filename='/media/alert.png') {l2}" alt="">
          </a>
        </div>
      </div>
    </div>
    
    <div class="main">
      <div class="main_column">
        <div class="mini">
        <!--
        {f1}% with messages = get_flashed_messages(with_categories=true) %{l1}
            {f1}% if messages %{l1}
              {f1}% for category, message in messages %{l1}
                <div class="alert alert-{f2} category {l2}">
                  {f2} message {l2}
                </div>
              {f1}% endfor %{l1}
            {f1}% endif %{l1}
          {f1}% endwith %{l1}
        -->
          <div class="mini_column">
            <p><pre>  ...........................
    _
  /_  /|   / / |/ /  / /\  /|
   / /_|  /_/  / /  / /  \/ |
/_/ /  | /  | / /__/ /      |
.............................</pre></p>
            <p>Your project ({name}) default page</p>
            {f1}% block main %{l1}
              <!-- main content -->
            {f1}% endblock main %{l1}
          </div>
        </div>

        <div class="three_col">
          <div>
            <p>An extension of flask web framework of python that erase the complexity of constructing flask project blueprint, packages, and other annoying stuffs</p>
          </div>
        </div>
      </div>
    </div>

    <div class="footer">
      <p><pre>============================
 @ {__title__} software - v{__version__}
============================</pre></p>
    </div>
  </div>
</body>
</html>
"""
  page_desc = stylePage(name, _is)
  return f"""{f1}% extends "index.html" %{l1}

{f1}% block head %{l1}
  <link rel="stylesheet" type="text/css" href="{f2} url_for('{name}.static', filename='style.css') {l2}">
{f1}% endblock head %{l1}

{f1}% block main %{l1}
  <h3><pre>({name})
{page_desc[1]}
{page_desc[0]}
{page_desc[1]}</pre></h3>
{f1}% endblock main %{l1}
"""


def _css(f1=f1, l1=l1, is_base=True):
  if is_base:
    return f"""* {f1}
  margin: 0;
  padding: 0;
  box-sizing: border-box;
{l1}

html, body, div, span, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
abbr, address, cite, code,
del, dfn, em, img, ins, kbd, q, samp,
small, strong, sub, sup, var,
b, i,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section, summary,
time, mark, audio, video {f1}
  outline:0;
  /* font-size:100%; */
  vertical-align:baseline;
  background:transparent;
{l1}

body{f1}
  background: lightgrey;
  overflow-x: hidden;
  overflow-y: auto;
  font-size: 15px;
  font-family: "Roboto","Lucida Grande","DejaVu Sans","Bitstream Vera Sans", Times 'Segoe UI', Tahoma, Verdana, sans-serif, serif,Verdana,Arial,sans-serif;
{l1}

.container{f1}
  width: 100%;
  overflow-x: hidden;
  overflow-y: auto;
{l1}

.header{f1}
  top: 0;
  width: 100%;
  height: 11.5vh;
  position: fixed;
  background: rgb(50, 50, 63);
  border-bottom: solid black 1px;
  display: flex;
  align-items: center;
  justify-content: center;
{l1}

.header_col{f1}
  width: 90%;
  padding: 20px 70px;
  display: flex;
  align-items: center;
  justify-content: space-between;
{l1}

@media only screen and (max-width: 700px){f1}
  .header_col{f1}
    padding: 18px 5px;
  {l1}
{l1}

.head_left{f1}
  width: 45%;
  height: 100%;
{l1}

@media only screen and (max-width: 700px){f1}
  .logo{f1}
    font-size: 20px;
  {l1}
{l1}

.logo a{f1}
  color: white;
  text-decoration: none;
  width: fit-content;
{l1}

.head_right{f1}
  width: 50%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-end;
{l1}

.head_right a{f1}
  color: white;
  margin-left: 15px;
  font-size: 18px;
  text-decoration: none;
{l1}

.head_right a:hover{f1}
  text-decoration: underline solid 3px;
{l1}

@media only screen and (max-width: 700px){f1}
  .link_0, .link_1, .link_2, .link_3{f1}
    display: none;
  {l1}
{l1}

.head_right a img{f1}
  width: 40px;
  height: 40px;
  margin-left: 15px;
{l1}

.alert{f1}
  display: block;
  position: relative;
{l1}

.main{f1}
  width: 100%;
  display: flex;
  justify-content: center;
  margin-top: 12vh;
{l1}

.main_column{f1}
  width: 90%;
  padding: 10px 70px;
{l1}

@media only screen and (max-width: 700px){f1}
  .main_column{f1}
    width: 100%;
    padding: 0;
  {l1}
{l1}

.mini{f1}
  width: 100%;
  min-height: 50vh;
  display: flex;
  justify-content: center;
  align-items: center;
{l1}

.mini_column{f1}
  width: 80%;
  max-width: 1024px;
  height: 45vh;
  border-radius: 7px;
  padding: 50px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
{l1}

@media only screen and (max-width: 700px){f1}
  .mini_column{f1}
    max-width: 100%;
    width: 90%;
    height: 60vh;
    padding: 0;
  {l1}
{l1}

.mini_column p{f1}
  max-width: 80%;
  text-align: center;
  font-weight: lighter;
  font-size: 1rem;
{l1}

.three_col{f1}
  margin: 20px 0;
  width: 100%;
  display: flex;
  justify-content: space-evenly;
{l1}

@media only screen and (max-width: 700px){f1}
  .three_col{f1}
    margin: 10px 0;
    flex-direction: column;
    align-items: space-evenly;
  {l1}
{l1}

.three_col div{f1}
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 100%;
  min-width: 50%;
{l1}

.three_col div p{f1}
  max-width: 80%;
  font-size: 1.1rem;
  line-height: 35px;
  text-align: center;
{l1}

@media only screen and (max-width: 700px){f1}
  .three_col div p{f1}
    max-width: 90%;
    font-size: 1rem;
    line-height: 25px;
    margin-top: 5px;
  {l1}
{l1}

.footer{f1}
  margin: 20px 0;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-top: solid black 1px;
{l1}

@media only screen and (max-width: 700px){f1}
  .footer{f1}
    margin: 10px 0;
    flex-direction: column;
    align-items: center;
    align-items: center;
  {l1}
{l1}

.footer p{f1}
  max-width: 80%;
  font-size: 1.1rem;
  line-height: 35px;
  text-align: center;
{l1}

@media only screen and (max-width: 700px){f1}
  .footer p{f1}
    max-width: 90%;
    font-size: 1rem;
    line-height: 25px;
    margin-top: 5px;
  {l1}
{l1}
  """
  return f"""
.mini_column h3{f1}
  /* font-size: 2.5rem; */
  font-weight: lighter;
  margin-top: 15px;
  text-align: center;
{l1}
"""


def _js(name, f1=f1, l1=l1):
  return f"""function test(){f1}
  alert('I am sakyum test alert for ({name})')
{l1}
"""


null = r"""# write awesome code here!
"""


def thunder_dummy(project):
  return f"""from sakyum import Boot
  
boot = Boot()

if __name__ == "__main__":
  boot.run()

from {project} import app
from {project}.routes import base
# from <app_name>.views import <app_name>

app.register_blueprint(base)
# app.register_blueprint(<app_name>)

app.run(debug=boot.d, port=boot.p, host=boot.h)
"""


def pro_init_dummy():
  return f"""from .routes import base
from .config import app
"""


def pro_config_dummy(secure_app=secure_app, long_comment='"""'):
  return f"""from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from pathlib import Path
from os import path

db_ORIGIN = Path(__file__).resolve().parent.parent

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '{secure_app}'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+str(db_ORIGIN)+'/default.db'

db = SQLAlchemy(app)

if path.exists(str(db_ORIGIN) + '/default.db'):
  pass # if default.db exist just pass
else:
  {long_comment} You will need to import models themselves before issuing `db.create_all` {long_comment}
  # from <app_name>.models import <app_model>
  db.create_all() # create db file
# db.init_app(app)
"""


def pro_routes_dummy(proj, f1=f1, l1=l1):
  return f"""from flask import (render_template, Blueprint)
from sakyum.utils import template_dir, static_dir
# from blogy.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, flash, redirect
from datetime import datetime
from .config import db

base = Blueprint("base", __name__, template_folder=template_dir(), static_folder=static_dir("{proj}"))

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)

#     def __repr__(self):
#         return f"User('{f1}self.username{l1}', '{f1}self.email{l1}', '{f1}self.image_file{l1}')"


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     content = db.Column(db.Text, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __repr__(self):
#         return f"Post('{f1}self.title{l1}', '{f1}self.date_posted{l1}')"


# @base.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {f1}form.username.data{l1}!', 'success')
#         return redirect(url_for('home'))
#     return render_template('register.html', title='Register', form=form)


# @base.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('base.index'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html', title='Login', form=form)


# @base.route('/')
# def index():
#   return "<h1>base index page</h1>"

@base.route('/')
def index():
  return render_template("index.html")
"""


def app_views_dummy(your_application, app, f1=f1, l1=l1):
  return f"""from {your_application} import app
from flask import (render_template, Blueprint, url_for, flash, redirect)
from sakyum.utils import template_dir, static_dir
# from .forms import RegistrationForm, LoginForm

{app} = Blueprint("{app}", __name__, template_folder=template_dir(), static_folder=static_dir("{app}"))

# @{app}.route('/')
# def index():
#   return "<h1>{app} index page</h1>"

@{app}.route('/{app}')
def index():
  return render_template("{app}/index.html")

# @{app}.route('/register', methods=["GET", "POST"])
# def register():
#   form = RegistrationForm()
#   if form.validate_on_submit():
#         flash(f'Account created for {f1}form.username.data{l1}!', 'success')
#         return redirect(url_for('{app}.index'))
#   return render_template("{app}/register.html", form=form)

# @{app}.route('/login', methods=["GET", "POST"])
# def login():
#   form = LoginForm()
#   if form.validate_on_submit():
#         if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#             flash('You have been logged in!', 'success')
#             return redirect(url_for('{app}.index'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#   return render_template("{app}/login.html", form=form)
"""


def app_forms_dummy():
  return f"""from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
"""


def app_models_dummy(your_application, f1=f1, l1=l1):
  return f"""from datetime import datetime
from {your_application}.config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    # the `Post` is the post model class below
    # the `author` is the attribute that we can use to get author who created the post
    # the `lazy` argument just define when sqlalchemy loads the data from the database

    def __repr__(self):
        return f"User('{f1}self.username{l1}', '{f1}self.email{l1}', '{f1}self.image_file{l1}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{f1}self.title{l1}', '{f1}self.date_posted{l1}')"
# db.create_all()


# move on to terminal and paste the following command
# python
# from zaria.config import db
# db.create_all()

# from blogy.models import User, Post
# u = User(username="user_1", email="user_1@email.com", password="1234")
# p = Post(title="post one", content="Lorem lipsum doler", user_id=u.id)

# db.session_add(u)
# db.session_add(p)
# db.commit()

# User.query.all() # show all users
# Post.query.all() # show all post of users

# dir(User.query) # to see many other method
"""
