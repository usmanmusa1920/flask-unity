# from sakyum software, your (todo_project) project routes.py file
from flask import (render_template, Blueprint)
from sakyum.utils import template_dir, static_dir
from flask import render_template


base = Blueprint("base", __name__, template_folder=template_dir(), static_folder=static_dir("todo_project"))
errors = Blueprint("errors", __name__, template_folder=template_dir(temp_from_pkg=True))


"""
register your app after importing it blueprint from the app views.py file,
by passing (append) your app blueprint that you import
into the `reg_blueprints` list below,
  :warning  -->  don't ommit the base blueprint, and the errors blueprint
"""
from todo_app.views import todo_app
reg_blueprints = [base, errors, todo_app]


@base.route('/')
def index():
  """ removing error pages in app pages list, if it exist """
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
