# -*- coding: utf-8 -*-

from . import f1
from . import l1
from . import long_comment


def app_init_dummy():
  return f"""from . import views
"""


def app_views_dummy(app):
  """app is the application name of your project"""
  return f"""from flask import (render_template, Blueprint)
from sakyum.utils import footer_style, template_dir, static_dir
from sakyum.contrib import db
# from .models import <app_models>
# from .forms import <model_form>


{app} = Blueprint('{app}', __name__, template_folder=template_dir(), static_folder=static_dir('{app}'))


@{app}.route('/{app}/', methods=['GET', 'POST'])
def index():
  context = {f1}
    'head_title': '{app}',
    'footer_style': footer_style,
  {l1}
  return render_template('{app}/index.html', context=context)
"""


def app_forms_dummy():
  return f"""from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


# write your app forms here!
"""


def app_models_dummy():
  return f"""from datetime import datetime
from sakyum.contrib import db


{long_comment}
when ever you create a model, make sure you import it in your project config.py
file and register it to the admin page in other to see it in admin page
{long_comment}

# write your app model here!
"""

def app_admin_dummy():
  return f"""from flask_login import current_user
from flask import redirect, request, url_for
from flask_admin.contrib.sqla import ModelView


# write your app admin model view here!
"""
