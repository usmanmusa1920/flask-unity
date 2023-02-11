# from sakyum software, your app (todo_app) views.py file
from flask import (render_template, Blueprint)
from sakyum.utils import template_dir, static_dir
# from .models import <model_name>
# from .forms import <model_form>

todo_app = Blueprint("todo_app", __name__, template_folder=template_dir(), static_folder=static_dir("todo_app"))


@todo_app.route('/todo_app', methods=["GET", "POST"])
def index():
  return render_template("todo_app/index.html")
