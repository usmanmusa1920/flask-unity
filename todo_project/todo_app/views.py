# from sakyum software, your app (todo_app) views.py file
from flask import (render_template, Blueprint)
from sakyum.utils import footer_style, template_dir, static_dir
# from .models import <model_name>
# from .forms import <model_form>

todo_app = Blueprint("todo_app", __name__, template_folder=template_dir(), static_folder=static_dir("todo_app"))


@todo_app.route('/todo_app/', methods=["GET", "POST"])
def index():
  head_title = "todo_app"
  """
    the todo_app/index.html pass below is the html file in your project templates/todo_app base dir
    inherited (extended) from `sakyum/templates/default_page/default_index.html`
    you can edit it and give it a different css and js file to your desire
  """

  return render_template("todo_app/index.html", head_title=head_title, footer_style=footer_style)
