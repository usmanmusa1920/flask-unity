# from sakyum software, your app (todo_app) views.py file
from flask import (render_template, Blueprint, redirect, url_for, flash)
from flask_login import current_user, login_required
from sakyum.utils import footer_style, template_dir, static_dir
from .forms import QuestionForm
from todo_project.config import db
from .models import Todo_appQuestionModel

todo_app = Blueprint("todo_app", __name__, template_folder=template_dir(), static_folder=static_dir("todo_app"))


@todo_app.route('/todo_app/', methods=["GET", "POST"])
@login_required
def index():
  head_title = "todo_app"
  """
    the todo_app/index.html pass below is the html file in your project templates/todo_app base dir
    inherited (extended) from `sakyum/templates/default_page/default_index.html`
    you can edit it and give it a different css and js file to your desire
  """

  return render_template("todo_app/index.html", head_title=head_title, footer_style=footer_style)


@todo_app.route('/todo_app/new', methods=["GET", "POST"])
@login_required
def new():
  head_title = "todo_app"
  form = QuestionForm()
  if form.validate_on_submit():
    post = Todo_appQuestionModel(question_text=form.question_text.data, user=current_user)
    db.session.add(post)
    db.session.commit()
    flash('Your post has been created!', 'success')
    return redirect(url_for('todo_app.index'))
  
  return render_template("todo_app/new.html", head_title=head_title, footer_style=footer_style, form=form)
