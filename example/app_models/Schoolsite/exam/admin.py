# from sakyum software, your app (exam) admin.py file
from flask_login import current_user
from flask import redirect, request, url_for
from flask_admin.contrib.sqla import ModelView

class QuestionChoiceAdminView(ModelView):
  can_delete = True  # enable model deletion
  can_create = True  # enable model deletion
  can_edit = True  # enable model deletion
  page_size = 50  # the number of entries to display on the list view

  def is_accessible(self):
    return current_user.is_authenticated

  def inaccessible_callback(self, name, **kwargs):
    # redirect to login page if user doesn't have access
    return redirect(url_for('auth.adminLogin', next=request.url))
