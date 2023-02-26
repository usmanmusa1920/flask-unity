# -*- coding: utf-8 -*-

f1 = "{"
l1 = "}"
long_comment = "\"\"\""


def app_views_dummy(app):
  """
  # :app is the application name that you create within your project
  """
  return f"""from flask import (render_template, Blueprint)
from sakyum.utils import footer_style, template_dir, static_dir
# from .forms import <model_form>
# from <project_name>.config import db
# from .models import <app_models>

{app} = Blueprint("{app}", __name__, template_folder=template_dir(), static_folder=static_dir("{app}"))


@{app}.route('/{app}/', methods=["GET", "POST"])
def index():
  head_title = "{app}"
  {long_comment}
    the {app}/index.html pass below is the html file in your project templates/{app} base dir
    inherited (extended) from `sakyum/templates/default_page/default_index.html`
    you can edit it and give it a different css and js file to your desire
  {long_comment}

  return render_template("{app}/index.html", head_title=head_title, footer_style=footer_style)
"""


def app_forms_dummy(app_name):
  return f"""from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

# write your app forms here!
"""


def app_models_dummy(your_application, f1=f1, l1=l1, app_name=False, long_comment=long_comment):
  return f"""from datetime import datetime
from {your_application}.config import db


{long_comment}
when ever you create a model, make sure you import it in your project config.py
file and register it to the admin page in other to see it in admin page
{long_comment}

# write your models here!
"""

def app_admin_dummy(app=None):
  return f"""
from flask_login import current_user
from flask import redirect, request, url_for
from flask_admin.contrib.sqla import ModelView

# write your model view here!
"""
