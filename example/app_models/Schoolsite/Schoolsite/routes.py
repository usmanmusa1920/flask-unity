# from sakyum software, your (Schoolsite) project routes.py file
from flask import (render_template, Blueprint)
from sakyum.utils import footer_style, template_dir, static_dir, rem_blueprint
from sakyum.blueprint import default, errors, auth
from flask import render_template
from exam.views import exam


base = Blueprint("base", __name__, template_folder=template_dir(), static_folder=static_dir("Schoolsite"))

rem_blue = [default, errors, auth, base]
reg_blueprints = [
  default,
  errors,
  auth,
  base,
  exam,
]


@default.route('/', methods=["POST", "GET"])
def index():
  context = {
    "project_name": "Schoolsite",
    "footer_style": footer_style,
    "blueprints_list": rem_blueprint(lst_blue=reg_blueprints, rem_blue=rem_blue),
  }
  return render_template("Schoolsite/index.html", context=context)
  
  
""" overwrite error pages here """
