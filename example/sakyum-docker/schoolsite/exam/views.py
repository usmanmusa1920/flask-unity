# from sakyum software, your app (exam) views.py file
from flask import (render_template, Blueprint)
from sakyum.utils import footer_style, template_dir, static_dir
from sakyum.contrib import db
# from .models import <app_models>
# from .forms import <model_form>

exam = Blueprint("exam", __name__, template_folder=template_dir(), static_folder=static_dir("exam"))


@exam.route('/exam/', methods=["GET", "POST"])
def index():
  context = {
    "head_title": "exam",
    "footer_style": footer_style,
  }
  return render_template("exam/index.html", context=context)
