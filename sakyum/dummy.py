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

def _html(name, project_name=False, is_base=True, f1=f1, l1=l1, f2=f2, l2=l2):
  if is_base:
    _is = "application"
    static_url = name
  else:
    _is = "project"
    static_url = "base"
    return f"""{f1}% extends "default_index.html" %{l1}

{f1}% block short_info %{l1}
  <p>Your project ({name}) default page</p>
{f1}% endblock short_info %{l1}

{f1}% block main %{l1}
  {f1}% if blueprints_list|length > 1 %{l1}
    <div class="blueprint_list_wrapper">
      <div class="blueprint_list">
        <p>Routes</p>
        {f1}% for blueprint in blueprints_list %{l1}
          <a href="/{{blueprint.name}}">{{blueprint.name}}</a>
          </br>
        {f1}% endfor %{l1}
        <a href="/login">login</a>
        </br>
      </div>
    </div>
  {f1}% endif %{l1}

  <div class="pkg_desc">
    <div>
      <p>An extension of flask web framework of python that erase the complexity of constructing flask project blueprint, packages, and other annoying stuffs</p>
    </div>
  </div>
{f1}% endblock main %{l1}
"""
  page_desc = stylePage(name, _is)
  return f"""{f1}% extends "{project_name}/index.html" %{l1}

{f1}% block head_css %{l1}
  <!-- <link rel="stylesheet" type="text/css" href="{f2} url_for('{name}.static', filename='style.css') {l2}"> -->
{f1}% endblock head_css %{l1}

{f1}% block head_title %{l1}
  <title>Sakyum - {f2}head_title{l2}</title>
{f1}% endblock head_title %{l1}

{f1}% block main %{l1}
  <h3><pre>({name}) app
{page_desc[1]}
{page_desc[0]}
{page_desc[1]}</pre></h3>
{f1}% endblock main %{l1}
"""


def _css(f1=f1, l1=l1):
  return f"""
* {f1}
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

body {f1}
  overflow-x: hidden;
  overflow-y: auto;
  font-size: 15px;
  font-family: "Roboto","Lucida Grande","DejaVu Sans","Bitstream Vera Sans", Times 'Segoe UI', Tahoma, Verdana, sans-serif, serif,Verdana,Arial,sans-serif;
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
from sakyum import version_style_desc, version_style_border
from sakyum.utils import template_dir, static_dir
from sakyum.blueprint import default, errors, auth
from flask import render_template
# from <app_name>.views import <app_name>


base = Blueprint("base", __name__, template_folder=template_dir(), static_folder=static_dir("{proj}"))


{long_comment}
  register your app after importing it blueprint from the app views.py file,
  by passing (append) your app blueprint that you import
  into the `reg_blueprints` list below,
  
  warning:
      don\'t ommit the registered blueprint you see in  the list (default, errors, auth, base) blueprints
{long_comment}

reg_blueprints = [
  default,
  errors,
  auth,
  base,
]

def rem_blueprint(lst_blue):
  # these are blueprint that we don't want to show on the
  # default page so we are removing them from the list

  rem_blue = [default, errors, auth, base]
  for blue in rem_blue:
    if blue in lst_blue:
      # finding the index of the `blue` item blueprint in the list
      err_index = lst_blue.index(blue)
      # removing it `blue` item from the list using it index number
      lst_blue.pop(err_index)
  blueprints_list = lst_blue
  return blueprints_list


@default.route('/')
def index():
  # the default_base.html below is located in the sakyum package (templates/default_page) folder
  return render_template("default_base.html", project_name="{proj}", blueprints_list=rem_blueprint(reg_blueprints), version_style_desc=version_style_desc, version_style_border=version_style_border)
  
  
{long_comment} overwrite error pages here {long_comment}
"""


def app_views_dummy(app):
  """
  # :app is the application name that you create within your project
  """
  return f"""from flask import (render_template, Blueprint)
from sakyum import version_style_desc, version_style_border
from sakyum.utils import template_dir, static_dir
# from .models import <model_name>
# from .forms import <model_form>

{app} = Blueprint("{app}", __name__, template_folder=template_dir(), static_folder=static_dir("{app}"))


@{app}.route('/{app}/', methods=["GET", "POST"])
def index():
  head_title = "{app}"
  {long_comment}
    the {app}/index.html pass below is the html file in your project templates/{app} base dir
    inherited (extended) from `sakyum/templates/default_page/default_index.html`
    you can edit it and give it a different css and js file to your desire
  {long_comment}

  return render_template("{app}/index.html", head_title=head_title, version_style_desc=version_style_desc, version_style_border=version_style_border)
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
