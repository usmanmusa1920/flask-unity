# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from flask_admin.contrib.sqla import ModelView
from sakyum.utils import footer_style, template_dir, static_dir

# static_folder: the folder where the Blueprint's static files can be found
# static_url_path: the URL to serve static files from
# template_folder: the folder containing the Blueprint's templates
# url_prefix: the path to prepend to all of the Blueprint's URLs
# subdomain: the subdomain that this Blueprint's routes will match on by default
# url_defaults: a dictionary of default values that this Blueprint's views will receive
# root_path: the Blueprint's root dictionary path, whose default values is obtained from the Blueprint's import

default = Blueprint('default', __name__, template_folder=template_dir(temp_from_pkg='default_page'), static_folder=static_dir('default_style', static_from_pkg=True))
errors = Blueprint('errors', __name__, template_folder=template_dir(temp_from_pkg='default_errors'))
auth = Blueprint('auth', __name__, template_folder=template_dir(temp_from_pkg='default_page'))


"""
The `default` blueprint above is the blueprint that is been used by sakyum for linking
it default pages (css, js, and favicon.ico) files and also it can be use for our project
default html pages (landing page route) that is located in your project route.py file
`<project_name>/route.py` like ` @default.route() `, but instead we use ` @base.route() `
for that `<project_name>/routes.py` as default. We also register it in the project routes.py
file `reg_blueprints` list to make it accessible

The `errors` blueprint above is for error pages, you can overite the error pages by
defining them in your project routes.py file `<project_name>/route.py` just like the
way we did in here down below for some of our default error pages (400, 403, 500, etc)
by giving your desire template file path (correspond to your project templates folder)
for each error page

The `auth` blueprint above is for the `login, logout, register, change_password` and
other default authentication system (route) of your project, which will let you log into admin page
"""


def adminModelRegister(admin, reg_models, db):
  """function that will register a direct model (not model view)"""
  for reg_model in reg_models:
    admin.add_view(ModelView(reg_model, db.session))
    

@errors.app_errorhandler(400)
def error_400(error):
  context = {
    'head_title': 'error page',
    'footer_style': footer_style,
  }
  return render_template('400.html', context=context), 400


@errors.app_errorhandler(401)
def error_401(error):
  context = {
    'head_title': 'error page',
    'footer_style': footer_style,
  }
  return render_template('401.html', context=context), 401


@errors.app_errorhandler(403)
def error_403(error):
  context = {
    'head_title': 'error page',
    'footer_style': footer_style,
  }
  return render_template('403.html', context=context), 403


@errors.app_errorhandler(404)
def error_404(error):
  context = {
    'head_title': 'error page',
    'footer_style': footer_style,
  }
  return render_template('404.html', context=context), 404


@errors.app_errorhandler(406)
def error_406(error):
  context = {
    'head_title': 'error page',
    'footer_style': footer_style,
  }
  return render_template('406.html', context=context), 406


@errors.app_errorhandler(415)
def error_415(error):
  context = {
    'head_title': 'error page',
    'footer_style': footer_style,
  }
  return render_template('415.html', context=context), 415


@errors.app_errorhandler(429)
def error_429(error):
  context = {
    'head_title': 'error page',
    'footer_style': footer_style,
  }
  return render_template('429.html', context=context), 429


@errors.app_errorhandler(500)
def error_500(error):
  context = {
    'head_title': 'error page',
    'footer_style': footer_style,
  }
  return render_template('500.html', context=context), 500


@errors.app_errorhandler(501)
def error_501(error):
  context = {
    'head_title': 'error page',
    'footer_style': footer_style,
  }
  return render_template('501.html', context=context), 501


@errors.app_errorhandler(502)
def error_502(error):
  context = {
    'head_title': 'error page',
    'footer_style': footer_style,
  }
  return render_template('502.html', context=context), 502


@errors.app_errorhandler(503)
def error_503(error):
  context = {
    'head_title': 'error page',
    'footer_style': footer_style,
  }
  return render_template('503.html', context=context), 503


@errors.app_errorhandler(504)
def error_504(error):
  context = {
    'head_title': 'error page',
    'footer_style': footer_style,
  }
  return render_template('504.html', context=context), 504
