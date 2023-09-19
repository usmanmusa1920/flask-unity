
Flask-Unity
###########

**Flask-Unity** an extension of flask web framework that erase the complexity of structuring flask project blueprint, packages, connecting other flask extensions, database migrations, and other annoying stuffs.

The main reason behind the development of `flask_unity` is to combine (`unite`) `flask <https://flask.palletsprojects.com>`_ and it extensions in one place to make it ease when developing an application without the headache (worrying) of knowing the tricks on how to connect those extensions with flask, or import something from somewhere to avoid some errors such as circular import and other unexpected errors. Also structuring flask application is a problem at some cases to some people, `flask_unity` take care of all these so that you only focus on writing your application views the way you want.

Flask-unity depends on (come with) the following flask popular and useful extensions, these include: `flask-admin <https://flask-admin.readthedocs.io>`_ for building an admin interface on top of an existing data model (where you can manage your models in the admin page), `flask-bcrypt <https://flask-bcrypt.readthedocs.io>`_ it provides bcrypt hashing utilities for your application, `flask-login <https://flask-login.readthedocs.io>`_ it provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time, `flask-sqlalchemy <https://flask-sqlalchemy.palletsprojects.com>`_ It simplifies using SQLAlchemy with Flask by setting up common objects and patterns for using those objects, such as a session tied to each web request, models, and engines, `flask-wtf <https://flask-wtf.readthedocs.io>`_ Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA. And possibly some other extensions / libraries.

It also include `alembic <https://alembic.sqlalchemy.org>`_ that handles SQLAlchemy database migrations. The database operations are made available through the flask-unity command-line interface or the alembic. It configures Alembic in the proper way to work with your Flask and Flask-SQLAlchemy application. In terms of the actual database migrations, everything is handled by Alembic so you get exactly the same functionality.

Table of content
----------------

.. toctree::
    :maxdepth: 2

    quick_start
    create_models
    app_forms
    admin_user
    custom_auth
    database
    cli
    error_pages
    page_and_filesystem
    know

Useful links:
-------------

- `Repository <https://github.com/usmanmusa1920/flask-unity>`_

- `PYPI Release <https://pypi.org/project/flask-unity>`_

Flask-unity default page
------------------------

.. image:: https://raw.githubusercontent.com/usmanmusa1920/flask-unity/master/docs/_static/flask_unity_default_page.png
    :align: center
