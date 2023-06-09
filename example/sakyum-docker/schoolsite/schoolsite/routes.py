# from sakyum software, your (schoolsite) project routes.py file
from flask import (render_template, Blueprint)
from sakyum import blueprint
from sakyum.utils import footer_style, template_dir, static_dir, rem_blueprint
from exam.views import exam


base = Blueprint("base", __name__, template_folder=template_dir(), static_folder=static_dir("schoolsite"))

rem_blue = [blueprint.default, blueprint.errors, blueprint.auth, base]
reg_blueprints = [
  blueprint.default,
  blueprint.errors,
  blueprint.auth,
  base,
  exam,
]


@base.route('/', methods=["POST", "GET"])
def index():
  context = {
    "project_name": "schoolsite",
    "footer_style": footer_style,
    "blueprints_list": rem_blueprint(lst_blue=reg_blueprints, rem_blue=rem_blue),
  }
  return render_template("schoolsite/index.html", context=context)
  
# overwrite (customise) error pages here
