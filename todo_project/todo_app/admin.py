# from flask_unity software, your app (todo_app) admin.py file

from flask_login import current_user
from flask import redirect, request, url_for
from flask_admin.contrib.sqla import ModelView


"""
  Customise your app admin page, by going through
  flask-admin documentations at:
    https://flask-admin.readthedocs.io/en/latest/introduction/#getting-started
"""


class QuestionChoiceAdminView(ModelView):
  can_delete = False  # disable model deletion
  can_create = True
  can_edit = True
  page_size = 50  # the number of entries to display on the list view

  # def is_accessible(self):
  #   return current_user.is_authenticated

  # def inaccessible_callback(self, name, **kwargs):
  #   # redirect to login page if user doesn't have access
  #   return redirect(url_for('login', next=request.url))
