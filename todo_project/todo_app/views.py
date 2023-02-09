# from sakyum software, your app (todo_app) views.py file
from flask import (render_template, Blueprint)
from sakyum.utils import template_dir, static_dir
# from .models import <model_name>
# from .forms import <model_form>

todo_app = Blueprint("todo_app", __name__, template_folder=template_dir(), static_folder=static_dir("todo_app"))


@todo_app.route('/todo_app', methods=["GET", "POST"])
def index():
  
  """
    if you want to access your db data in html page, replace `<model_name>` with
    the name of your model and then pass it as a keyword argument in the `render_template`
    in our case we call it `model_list`:e.g

      # :model_list = <model_name>.query.all()
      # :return render_template("todo_app/index.html", model_list=model_list)

  """
  return render_template("todo_app/index.html")
