# -*- coding: utf-8 -*-

f1 = "{"
l1 = "}"
long_comment = "\"\"\""


def app_views_dummy(app):
  """
  # :app is the application name that you create within your project
  """
  return f"""from flask import (render_template, Blueprint)
from flask_unity.utils import footer_style, template_dir, static_dir
# from .forms import <model_form>
from <project_name>.config import db
from .models import <app_models>

{app} = Blueprint("{app}", __name__, template_folder=template_dir(), static_folder=static_dir("{app}"))


@{app}.route('/{app}/', methods=["GET", "POST"])
def index():
  head_title = "{app}"
  {long_comment}
    the {app}/index.html pass below is the html file in your project templates/{app} base dir
    inherited (extended) from `flask_unity/templates/default_page/default_index.html`
    you can edit it and give it a different css and js file to your desire
  {long_comment}

  return render_template("{app}/index.html", head_title=head_title, footer_style=footer_style)
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
when ever you create a model, make sure you import it in your project config.py
file and register it to the admin page in other to see it in admin page
{long_comment}


class {app_name.capitalize()}QuestionModel(db.Model):
  {long_comment} {app_name.capitalize()} default Question model {long_comment}
  id = db.Column(db.Integer, primary_key=True)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  # the user field is the user who create the question and he is in the `User` models of auth
  user = db.relationship("User", backref="user")
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  question_text = db.Column(db.Text, nullable=False)
  choices = db.relationship('{app_name.capitalize()}ChoiceModel', backref='selector', lazy=True)

  def __str__(self):
    return f"Question {f1}self.id{l1}: {f1}self.question_text{l1}"

  def __repr__(self):
    return f"Question {f1}self.id{l1}: {f1}self.question_text{l1}"
    
  # the `{app_name.capitalize()}ChoiceModel` is the choice model class below
  # the `selector` is the attribute that we can use to get selector who choose the choice
  # the `lazy` argument just define when sqlalchemy loads the data from the database


class {app_name.capitalize()}ChoiceModel(db.Model):
  {long_comment} {app_name.capitalize()} default Choice model {long_comment}
  id = db.Column(db.Integer, primary_key=True)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  question_id = db.Column(db.Integer, db.ForeignKey('{app_name.lower()}_question_model.id'), nullable=False)
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
from {app_name}.models import {app_name.capitalize()}QuestionModel, {app_name.capitalize()}ChoiceModel


# :method to create the tables and database, if it doesn't create db file,
# :run the below command. But if it create just ignore
db.create_all()


q1 = {app_name.capitalize()}QuestionModel(question_text="Is flask_unity an extension of flask web framework?")
q2 = {app_name.capitalize()}QuestionModel(question_text="Is flask better with flask_unity")

db.session.add(q1)
db.session.add(q2)
db.session.commit()

the_q1 = {app_name.capitalize()}QuestionModel.query.get_or_404(1)
the_q2 = {app_name.capitalize()}QuestionModel.query.get_or_404(2)

c1_1 = {app_name.capitalize()}ChoiceModel(choice_text="Yes, it is", question_id=the_q1.id)
c1_2 = {app_name.capitalize()}ChoiceModel(choice_text="No, it is not", question_id=the_q1.id)
c1_3 = {app_name.capitalize()}ChoiceModel(choice_text="I don't no", question_id=the_q1.id)

c2_1 = {app_name.capitalize()}ChoiceModel(choice_text="Yes for sure", question_id=the_q2.id)
c2_2 = {app_name.capitalize()}ChoiceModel(choice_text="Always the best", question_id=the_q2.id)
c2_3 = {app_name.capitalize()}ChoiceModel(choice_text="All the time", question_id=the_q2.id)

db.session.add(c1_1)
db.session.add(c1_2)
db.session.add(c1_3)

db.session.add(c2_1)
db.session.add(c2_2)
db.session.add(c2_3)

db.session.commit()

# to see all our questions
{app_name.capitalize()}QuestionModel.query.all()
dir({app_name.capitalize()}QuestionModel.query) # to see many other method

# to see choices related to our question number 1
{app_name.capitalize()}QuestionModel.query.get_or_404(1).choices

# to see all our choices
{app_name.capitalize()}ChoiceModel.query.all()
dir({app_name.capitalize()}ChoiceModel.query) # to see many other method

for i in {app_name.capitalize()}ChoiceModel.query.all():
  i.selector.question_text, i.choice_text


{long_comment}
"""

def app_admin_dummy(app=None):
  return f"""
from flask_login import current_user
from flask import redirect, request, url_for
from flask_admin.contrib.sqla import ModelView


{long_comment}
  Customise your app admin page, by going through
  flask-admin documentations at:
    https://flask-admin.readthedocs.io/en/latest/introduction/#getting-started
{long_comment}


class QuestionChoiceAdminView(ModelView):
  can_delete = False  # disable model deletion
  can_create = True
  can_edit = True
  page_size = 50  # the number of entries to display on the list view

  # def is_accessible(self):
  #   return current_user.is_authenticated

  # def inaccessible_callback(self, name, **kwargs):
  #   # redirect to login page if user doesn't have access
  #   return redirect(url_for('login', next=request.url))
"""
