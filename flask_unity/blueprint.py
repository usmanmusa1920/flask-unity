# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from flask_unity.utils import footer_style, template_dir, static_dir


default = Blueprint("default", __name__, template_folder=template_dir(temp_from_pkg="default_page"), static_folder=static_dir("default_style", static_from_pkg=True))
errors = Blueprint("errors", __name__, template_folder=template_dir(temp_from_pkg="default_errors"))
auth = Blueprint("auth", __name__, template_folder=template_dir(temp_from_pkg="default_page"))


"""

  the `default` blueprint above is the blueprint that we will be extending
  our project default pages and also our app default html pages from.
  We also register it in the project routes.py file `reg_blueprints` list

  the `errors` blueprint above is for error pages, you can overite the error
  pages by defining them in your project routes.py file just like the way we
  did in here down below for some of our default error pages (404, 403, 500)
  by giving your desire template file path (correspond to your project templates folder)
  for each error page

  the `auth` blueprint above is for the login and other default authentication
  system of your project, which will let you log into admin page

"""


# @auth.route('/admin/login/')
# def index():
#   """
#     the `admin_login.html` below is located in the flask_unity package (static/default_page/admin_login.html)
#   """
#   return render_template("admin_login.html", footer_style=footer_style)


@errors.app_errorhandler(400)
def error_400(error):
  return render_template('400.html', footer_style=footer_style), 400

@errors.app_errorhandler(401)
def error_401(error):
  return render_template('401.html', footer_style=footer_style), 401

@errors.app_errorhandler(403)
def error_403(error):
  return render_template('403.html', footer_style=footer_style), 403

@errors.app_errorhandler(404)
def error_404(error):
  return render_template('404.html', footer_style=footer_style), 404

@errors.app_errorhandler(406)
def error_406(error):
  return render_template('406.html', footer_style=footer_style), 406

@errors.app_errorhandler(415)
def error_415(error):
  return render_template('415.html', footer_style=footer_style), 415

@errors.app_errorhandler(429)
def error_429(error):
  return render_template('429.html', footer_style=footer_style), 429

@errors.app_errorhandler(500)
def error_500(error):
  return render_template('500.html', footer_style=footer_style), 500

@errors.app_errorhandler(501)
def error_501(error):
  return render_template('501.html', footer_style=footer_style), 501

@errors.app_errorhandler(502)
def error_502(error):
  return render_template('502.html', footer_style=footer_style), 502

@errors.app_errorhandler(503)
def error_503(error):
  return render_template('503.html', footer_style=footer_style), 503

@errors.app_errorhandler(504)
def error_504(error):
  return render_template('504.html', footer_style=footer_style), 504
