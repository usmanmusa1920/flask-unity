# from sakyum software, your (todo_project) project routes.py file
from flask import (render_template, Blueprint)
from sakyum.utils import template_dir, static_dir
from flask import render_template

base = Blueprint("base", __name__, template_folder=template_dir(), static_folder=static_dir("todo_project"))

from todo_app.views import todo_app
""" register your app, by passing (append) your app blueprint that you import into the `urls` list below,
  :warning  -->  don't ommit the base blueprint """
urls = [base, todo_app]

@base.route('/')
def index():
  urls_list = urls
  return render_template("index.html", urls_list=urls_list)
