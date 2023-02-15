# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from sakyum import version_style_desc, version_style_border
from sakyum.utils import template_dir, static_dir


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


@auth.route('/login/')
def index():
  """
    the `admin_login.html` below is located in the sakyum package (static/default_page/admin_login.html)
  """
  return render_template("admin_login.html", version_style_desc=version_style_desc, version_style_border=version_style_border)
  

@errors.app_errorhandler(404)
def error_404(error):
  return render_template('404.html', version_style_desc=version_style_desc, version_style_border=version_style_border), 404
  

@errors.app_errorhandler(403)
def error_403(error):
  return render_template('403.html', version_style_desc=version_style_desc, version_style_border=version_style_border), 403
  

@errors.app_errorhandler(500)
def error_500(error):
  return render_template('500.html', version_style_desc=version_style_desc, version_style_border=version_style_border), 500
