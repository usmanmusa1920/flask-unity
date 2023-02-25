
Overview
########

Welcome to Sakyum’s documentation. An extension of flask web framework that erase the complexity of structuring flask project blueprint, packages, and other annoying stuffs.

The main reason behind the development of `sakyum` is to combine `flask <https://flask.palletsprojects.com>`_ and it extensions in one place to make it ease when developing an application without the headache (worrying) of knowing the tricks on how to connect those extensions with flask, or import something from somewhere to avoid some errors such as circular import and other unexpected errors. Also structuring flask application is a problem at some cases, `sakyum` take care of all these so that you only focus on writing your application views the way you want.

Sakyum depends on (come with) the following flask popular and useful extensions, these include: `flask-admin <https://flask-admin.readthedocs.io>`_ where you can manage your models in the admin page, `flask-bcrypt <https://flask-bcrypt.readthedocs.io>`_ that will hash user password and other security issues, `flask-login <https://flask-login.readthedocs.io>`_ for login/logout session and other security tricks to make sure user cookie is safe, `flask-sqlalchemy <https://flask-sqlalchemy.palletsprojects.com>`_ for creating/inserting and other database management command, `flask-wtf <https://flask-wtf.readthedocs.io>`_ representing html page in the form of class. And possibly some other extensions.


Table of content
----------------

.. toctree::
   :maxdepth: 2

   quick_start
   views
   html_forms
   models
   templates_and_static
   error_pages
   databases
   flags
   mod_wsgi
   email
   testing
   deployment
   example/index.rst
   changelog

Support
-------

****

Python 3.8 or higher.

Useful links:
-------------
   
- `Repository <https://github.com/usmanmusa1920/sakyum>`_

- `Documentation <https://sakyum.readthedocs.io>`_

- `PYPI Release <https://pypi.org/project/sakyum>`_

Pull requests are welcome
