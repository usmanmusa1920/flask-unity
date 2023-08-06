# from flask_unity software, your (todo_project) project routes.py file
from flask import (render_template, Blueprint)
from flask_unity.utils import footer_style, template_dir, static_dir
from flask_unity.blueprint import default, errors, auth
from flask import render_template
from todo_app.views import todo_app


base = Blueprint("base", __name__, template_folder=template_dir(), static_folder=static_dir("todo_project"))


"""
  register your app after importing it blueprint from the app views.py file,
  by passing (append) your app blueprint that you import
  into the `reg_blueprints` list below,
  
  warning:
      don't ommit the registered blueprint you see in  the list (default, errors, auth, base) blueprints
"""

reg_blueprints = [
  default,
  errors,
  auth,
  base,
  todo_app,
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
  # the default_base.html below is located in the flask_unity package (templates/default_page) folder
  return render_template("default_base.html", project_name="todo_project", blueprints_list=rem_blueprint(reg_blueprints), footer_style=footer_style)
  
  
""" overwrite error pages here """
