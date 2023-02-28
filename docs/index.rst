
Sakyum
######

Welcome to ` **Sakyum’s** ` documentation. An extension of flask web framework that erase the complexity of structuring flask project blueprint, packages, and other annoying stuffs.

The main reason behind the development of `sakyum` is to combine `flask <https://flask.palletsprojects.com>`_ and it extensions in one place to make it ease when developing an application without the headache (worrying) of knowing the tricks on how to connect those extensions with flask, or import something from somewhere to avoid some errors such as circular import and other unexpected errors. Also structuring flask application is a problem at some cases to some people, `sakyum` take care of all these so that you only focus on writing your application views the way you want.

Sakyum depends on (come with) the following flask popular and useful extensions, these include: `flask-admin <https://flask-admin.readthedocs.io>`_ for building an admin interface on top of an existing data model (where you can manage your models in the admin page), `flask-bcrypt <https://flask-bcrypt.readthedocs.io>`_ it provides bcrypt hashing utilities for your application, `flask-login <https://flask-login.readthedocs.io>`_ it provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time, `flask-sqlalchemy <https://flask-sqlalchemy.palletsprojects.com>`_ It simplifies using SQLAlchemy with Flask by setting up common objects and patterns for using those objects, such as a session tied to each web request, models, and engines, `flask-wtf <https://flask-wtf.readthedocs.io>`_ Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA..


Table of content
----------------

.. toctree::
   :maxdepth: 2

   quick_start
   example/index
   advance/index
   views
   admin_user
   templates_and_static
   error_pages
   databases
   flags
   mod_wsgi
   email
   testing
   deployment


Useful links:
-------------

- `Repository <https://github.com/usmanmusa1920/sakyum>`_

- `PYPI Release <https://pypi.org/project/sakyum>`_
