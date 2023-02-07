# from sakyum software, your (todo_project) project routes.py file
from flask import (render_template, Blueprint)
from sakyum.utils import template_dir, static_dir
# from <app_name>.forms import <form_name>
from flask import render_template

base = Blueprint("base", __name__, template_folder=template_dir(), static_folder=static_dir("todo_project"))


@base.route('/')
def index():
  return render_template("index.html")
