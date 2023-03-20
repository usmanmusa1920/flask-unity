# from sakyum software, your (schoolsite) project routes.py file
from flask import (render_template, Blueprint, url_for)
from flask_login import current_user
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
  if current_user.is_authenticated:
    user_img = url_for("default.static", filename="media/" + current_user.user_img)
  else:
    user_img = None
  context = {
    "project_name": "schoolsite",
    "footer_style": footer_style,
    "user_img": user_img,
    "blueprints_list": rem_blueprint(lst_blue=reg_blueprints, rem_blue=rem_blue),
  }
  return render_template("schoolsite/index.html", context=context)
  
# overwrite (customise) error pages here
