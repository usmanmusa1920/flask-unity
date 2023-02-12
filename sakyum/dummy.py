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
long_comment = "\"\"\""


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
          <a href="/admin" class="link_3" target="_blank">Admin</a>
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
            {f1}% if blueprints_list|length > 1 %{l1}
              <div class="blueprint_list">
                <p>List of blueprints</p>
                {f1}% for blueprint in blueprints_list %{l1}
                  {f1}% if blueprint.name == "base" %{l1}
                    <!-- pass -->
                  {f1}% else %{l1}
                    <a href="/{f2}blueprint.name{l2}">{f2}blueprint.name{l2}</a>
                    </br>
                  {f1}% endif %{l1}
                {f1}% endfor %{l1}
              </div>
            {f1}% endif %{l1}
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

.blueprint_list{f1}
  height: 50%;
  width: 200px;
  padding: 5px;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow-y: scroll;
  background: white;
{l1}

@media only screen and (max-width: 700px){f1}
  .blueprint_list{f1}
    height: 30%;
    width: 70%;
    padding: 5px;
    overflow-y: scroll;
    background: white;
  {l1}
{l1}

.blueprint_list a{f1}
  text-decoration: none;
  color: dodgerblue;
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
  font-weight: lighter;
  margin-top: 15px;
  text-align: center;
{l1}

@media only screen and (max-width: 700px){f1}
  .mini_column h3{f1}
    font-size: 12px;
  {l1}
{l1}
"""


def _js(name, f1=f1, l1=l1):
  return f"""function test(){f1}
  alert('I am {__title__} test alert for ({name}) index page')
{l1}
"""


def null(long_comment=long_comment):
  return f"""{long_comment} write awesome code here! {long_comment}
"""


def thunder_dummy(project):
  return f"""from sakyum import Boot
  
boot = Boot()
if __name__ == "__main__":
  boot.run()

from {project} import app
from {project}.routes import reg_blueprints

for reg_blueprint in reg_blueprints:
  app.register_blueprint(reg_blueprint)
app.run(debug=boot.d, port=boot.p, host=boot.h)
"""


def pro_init_dummy():
  return f"""from .routes import base
from .config import app
"""


def pro_config_dummy(proj_name, secure_app=secure_app, long_comment=long_comment):
  return f"""from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask import Flask
from pathlib import Path

db_ORIGIN = Path(__file__).resolve().parent.parent

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '{secure_app}'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+str(db_ORIGIN)+'/default.db'

# set optional bootswatch theme
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
db = SQLAlchemy(app)


{long_comment} You will need to import models themselves before issuing `db.create_all` {long_comment}
# from <app_name>.models import <model_name>
db.create_all() # method to create the tables and database


{long_comment}
Model views allow you to add a dedicated set of admin
pages for managing any model in your database
{long_comment}
admin = Admin(app, name='{proj_name}')


{long_comment}
Register your model, by passing every model that you want
to manage in admin page in the below list (reg_models)
{long_comment}
reg_models = []
for reg_model in reg_models:
  admin.add_view(ModelView(reg_model, db.session))
"""


def pro_routes_dummy(proj):
  return f"""from flask import (render_template, Blueprint)
from sakyum.utils import template_dir, static_dir
from flask import render_template


base = Blueprint("base", __name__, template_folder=template_dir(), static_folder=static_dir("{proj}"))
errors = Blueprint("errors", __name__, template_folder=template_dir(temp_from_pkg=True))


{long_comment}
register your app after importing it blueprint from the app views.py file,
by passing (append) your app blueprint that you import
into the `reg_blueprints` list below,
  :warning  -->  don\'t ommit the base blueprint, and the errors blueprint
{long_comment}
# from <app_name>.views import <app_name>
reg_blueprints = [base, errors]


@base.route('/')
def index():
  {long_comment} removing error pages in app pages list, if it exist {long_comment}
  if errors in reg_blueprints:
    # finding the index of the errors blueprint in the list
    err_index = reg_blueprints.index(errors)
    # removing it from the list using it index number
    reg_blueprints.pop(err_index)
  blueprints_list = reg_blueprints
  return render_template("index.html", blueprints_list=blueprints_list)
  
  
@errors.app_errorhandler(404)
def error_404(error):
  return render_template('404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
  return render_template('403.html'), 403


@errors.app_errorhandler(500)
def error_500(error):
  return render_template('500.html'), 500
"""


def app_views_dummy(app):
  """
  # :app is the application name that you create within your project
  """
  return f"""from flask import (render_template, Blueprint)
from sakyum.utils import template_dir, static_dir
# from .models import <model_name>
# from .forms import <model_form>

{app} = Blueprint("{app}", __name__, template_folder=template_dir(), static_folder=static_dir("{app}"))


@{app}.route('/{app}', methods=["GET", "POST"])
def index():
  return render_template("{app}/index.html")
"""


def app_forms_dummy(app_name):
  return f"""from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class QuestionForm(FlaskForm):
  {long_comment} {app_name.capitalize()} default Question form {long_comment}
  question_text = TextAreaField('Question_Text', validators=[DataRequired()])
  submit = SubmitField('create')


class ChoiceForm(FlaskForm):
  {long_comment} {app_name.capitalize()} default Choice form {long_comment}
  question_id = StringField('Question_Id', validators=[DataRequired()])
  choice_text = StringField('Choice_Text', validators=[DataRequired(), Length(min=2, max=20)])
  submit = SubmitField('create')
"""


def app_models_dummy(your_application, f1=f1, l1=l1, app_name=False, long_comment=long_comment):
  return f"""from datetime import datetime
from {your_application}.config import db


{long_comment}
when ever you create a model, make sure you import it in your
project config.py file in other to see it in admin page
{long_comment}


class QuestionModel(db.Model):
  {long_comment} {app_name.capitalize()} default Question model {long_comment}
  id = db.Column(db.Integer, primary_key=True)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  question_text = db.Column(db.Text, nullable=False)
  choices = db.relationship('ChoiceModel', backref='selector', lazy=True)

  def __str__(self):
    return f"Question {f1}self.id{l1}: {f1}self.question_text{l1}"

  def __repr__(self):
    return f"Question {f1}self.id{l1}: {f1}self.question_text{l1}"
    
  # the `ChoiceModel` is the choice model class below
  # the `selector` is the attribute that we can use to get selector who choose the choice
  # the `lazy` argument just define when sqlalchemy loads the data from the database


class ChoiceModel(db.Model):
  {long_comment} {app_name.capitalize()} default Choice model {long_comment}
  id = db.Column(db.Integer, primary_key=True)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  question_id = db.Column(db.Integer, db.ForeignKey('question_model.id'), nullable=False)
  # you can pass a keyword argument of `unique=True` in the below choice_text field
  # that will make it unique across the entire table of choice
  choice_text = db.Column(db.String(100), nullable=False)

  def __str__(self):
    return f"{f1}self.choice_text{l1} of {f1}self.question_id{l1}"

  def __repr__(self):
    return f"{f1}self.choice_text{l1} of {f1}self.question_id{l1}"


{long_comment}
# *** PLAY WITH API ***

# :move on to terminal and paste the following command,
# :( in python interpreter ) make sure you are within that your virtual environment


from {your_application}.config import db
from todo_app.models import QuestionModel, ChoiceModel


# :method to create the tables and database, if it doesn't create db file,
# :run the below command. But if it create just ignore
db.create_all()


q1 = QuestionModel(question_text="Is sakyum an extension of flask web framework?")
q2 = QuestionModel(question_text="Is flask better with sakyum")

db.session.add(q1)
db.session.add(q2)
db.session.commit()

the_q1 = QuestionModel.query.get_or_404(1)
the_q2 = QuestionModel.query.get_or_404(2)

c1_1 = ChoiceModel(choice_text="Yes, it is", question_id=the_q1.id)
c1_2 = ChoiceModel(choice_text="No, it is not", question_id=the_q1.id)
c1_3 = ChoiceModel(choice_text="I don't no", question_id=the_q1.id)

c2_1 = ChoiceModel(choice_text="Yes for sure", question_id=the_q2.id)
c2_2 = ChoiceModel(choice_text="Always the best", question_id=the_q2.id)
c2_3 = ChoiceModel(choice_text="All the time", question_id=the_q2.id)

db.session.add(c1_1)
db.session.add(c1_2)
db.session.add(c1_3)

db.session.add(c2_1)
db.session.add(c2_2)
db.session.add(c2_3)

db.session.commit()

# to see all our questions
QuestionModel.query.all()
dir(QuestionModel.query) # to see many other method

# to see choices related to our question number 1
QuestionModel.query.get_or_404(1).choices

# to see all our choices
ChoiceModel.query.all()
dir(ChoiceModel.query) # to see many other method

for i in ChoiceModel.query.all():
  i.selector.question_text, i.choice_text


{long_comment}
"""
