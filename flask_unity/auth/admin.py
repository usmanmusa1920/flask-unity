# -*- coding: utf-8 -*-

from flask_login import current_user
from flask import redirect, request, url_for
from flask_admin.contrib.sqla import ModelView


class UserAdminView(ModelView):
  can_delete = True  # enable model deletion
  can_create = True  # enable model deletion
  can_edit = True  # enable model deletion
  page_size = 50  # the number of entries to display on the list view

  # This is used to list the various columns in the order you want them.
  column_list = ('username', 'email', 'password', 'date_created', 'authenticated', 'is_superuser')
  # Columns that you want to be searchable in the model.
  column_searchable_list = ('username', 'email', 'password', 'date_joined', 'authenticated', 'is_superuser')
  # The column that the view should be sorted with by default (when the view is loaded for
  # the first time). The second parameter True tells flask-admin to sort it in descending order.
  column_default_sort = ('username', True)
  # List of columns that can be used to filter.
  column_filters = ('username',)
  

  def is_accessible(self):
    return current_user.is_authenticated
    
    
  def inaccessible_callback(self, name, **kwargs):
    # redirect to login page if user doesn't have access
    return redirect(url_for('auth.adminLogin', next=request.url))
