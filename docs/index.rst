
Sakyum
######

An extension of flask web framework that erase the complexity of structuring flask project blueprint, packages, and other annoying stuffs.

The main reason behind the development of `sakyum` is to combine `flask <https://flask.palletsprojects.com>`_ and it extensions in one place to make it ease when developing an application without the headache (worrying) of knowing the tricks on how to connect those extensions with flask, or import something from somewhere to avoid some errors such as circular import and other unexpected errors. Also structuring flask application is a problem at some cases to some people, `sakyum` take care of all these so that you only focus on writing your application views the way you want.

Sakyum depends on (come with) the following flask popular and useful extensions, these include: `flask-admin <https://flask-admin.readthedocs.io>`_ for building an admin interface on top of an existing data model (where you can manage your models in the admin page), `flask-bcrypt <https://flask-bcrypt.readthedocs.io>`_ it provides bcrypt hashing utilities for your application, `flask-login <https://flask-login.readthedocs.io>`_ it provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time, `flask-sqlalchemy <https://flask-sqlalchemy.palletsprojects.com>`_ It simplifies using SQLAlchemy with Flask by setting up common objects and patterns for using those objects, such as a session tied to each web request, models, and engines, `flask-wtf <https://flask-wtf.readthedocs.io>`_ Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA. And possibly some other extensions / libraries.

When using sakyum, don't be confuse with the the concept of **project** and **app**.

**Project** is the entire folder that contain your flask application, when you create project with the command::

   python -c "from sakyum import project; project('schoolsite')"

It will create a parent directory with the name `schoolsite` also inside the `schoolsite` directory there is a directory with thesame name of the parent directory `schoolsite` this directory is the one that most of configurations, registering and other thing that are going to be implemented inside it.

Within that parent directory `schoolsite` it also generate a file called `thunder.py` this is the file that you will be running along side with some positional arguments and flags. Also it will generate a directory called `auth` this directory contains admin system utilities. Lastly it will generate `templates` and `static` directory for your site pages and it styles respectively. At a glance, it will create `schoolsite, thunder.py, templates, static, auth` all in `schoolsite`.

**App** (application) is like to say a blueprint which greatly simplify how large applications work and provide a central means for Flask extensions to register operations on applications. Read `blueprint <https://flask.palletsprojects.com/en/2.2.x/blueprints/>`_ about flask.

Don't worry if you didn't get the concept of `project` and `app`, surely you will get it if we dive deep by the help of the `schoolsite <https://sakyum.readthedocs.io/en/latest/quick_start.html>`_ project.


Table of content
----------------

.. toctree::
  :maxdepth: 2

  quick_start
  flags
  error_pages
  example/index
  admin_user
  auth_routes
  page_and_filesystem
  database
  mod_wsgi
  deployment


Useful links:
-------------

- `Repository <https://github.com/usmanmusa1920/sakyum>`_

- `PYPI Release <https://pypi.org/project/sakyum>`_
