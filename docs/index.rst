
Overview
########

Welcome to Sakyum’s documentation. An extension of flask web framework that erase the complexity of structuring flask project blueprint, packages, and other annoying stuffs.

The main reason behind the development of `sakyum` is to combine **`flask <https://flask.palletsprojects.com>`_** and it extensions in one place to make it ease when developing an application without the headache (worrying) of knowing the tricks on how to connect those extensions with flask, or import something from somewhere to avoid some errors such as circular import and other unexpected errors. Also structuring flask application is a problem at some cases, `sakyum` take care of all these so that you only focus on writing your application views the way you want.

Sakyum depends on (come with) the following flask popular and useful extensions, these include: **`flask-admin <https://flask-admin.readthedocs.io>`_** where you can manage your models in the admin page, **`flask-bcrypt <https://flask-bcrypt.readthedocs.io>`_** that will hash user password and other security issues, **`flask-login <https://flask-login.readthedocs.io>`_** for login/logout session and other security tricks to make sure user cookie is safe, **`flask-sqlalchemy <https://flask-sqlalchemy.palletsprojects.com>`_** for creating/inserting and other database management command, **`flask-wtf <https://flask-wtf.readthedocs.io>`_** representing html page in the form of class. And possibly some other extensions.

Installation
============

First we recomend you to create a virtual environment to avoid conflict (upgrade/downgrade of some of your system libraries) when installing sakyum, this is just a recomendation, it still work even if you install it without using virtualenvironment

Install and update the latest release from `pypi <https://pypi.org/project/sakyum>`_. Basically the library was uploaded using `sdist` (Source Distribution) and this software (library) might not be compatible with `windows operating system` but it works on other `OS` such as `linux` and `macOS`

you will notice we use `--upgrade` this will make sure it install the latest release from `pypi <https://pypi.org/project/sakyum>`_ (in case you have a version which is not the latest version), you can ommit the `--upgrade` and use the version you want then wait for the installation to finish.::

  pip install --upgrade sakyum

Create your first flask project using sakyum
============================================

After the installation paste the following command on your termianl::

  python -c "from sakyum import project; project('todo_project')"

or create a file and paste the below codes which is equivalent of the above, and then run the file

.. code-block:: python

    from sakyum import project

    project("todo_project")

Both the command you type on terminal or the code you paste in a file (after running the file) will create a project called **todo_project** now cd into the **todo_project** directory, if you do **ls** within the directory you just enter you will see a module called **thunder.py** and some directories (some in the form of package)**auth**, **static**, **templates** and a directory with the same name of your base directory name, in our case it is **todo_project**.

Tree structure of your project look like

.. code-block::

    todo_project
    ├── auth
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── models.py
    │   └── routes.py
    ├── static
    │   └── todo_project
    │       ├── index.js
    │       ├── media
    │       └── style.css
    ├── templates
    │   ├── admin
    │   │   └── index.html
    │   └── todo_project
    │       └── index.html
    ├── thunder.py
    └── todo_project
        ├── config.py
        ├── __init__.py
        └── routes.py

    8 directories, 12 files

Boot up the flask server by running the below command::

    python thunder.py boot

Now visit the local url **http://127.0.0.1:5000** this will show you index page of your project

Create flask project app using sakyum
#####################################

For you to start an app within your project (**todo_project**) shutdown the flask development server by pressing ( CTRL+C ). If you do **ls** in that same directory you will see it create a **default.db** file (an sqlite file). Now run the following command in  other to create your app, by giving the name you want your app to be, in our case we will call our app **todo_app**::

    python thunder.py create_app -a todo_app

        or

    python thunder.py create_app --app todo_app

this will create an app (a new package called **todo_app**) within your project (**todo_project**), the **-a** flag is equivalent to **--app** which is for the app name in this example it is called **todo_app**

Tree structure of your project after creating **todo_app** look like

.. code-block::

    .
    ├── auth
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── models.py
    │   └── routes.py
    ├── default.db
    ├── static
    │   ├── todo_app
    │   │   ├── index.js
    │   │   ├── media
    │   │   └── style.css
    │   └── todo_project
    │       ├── index.js
    │       ├── media
    │       └── style.css
    ├── templates
    │   ├── admin
    │   │   └── index.html
    │   ├── todo_app
    │   │   └── index.html
    │   └── todo_project
    │       └── index.html
    ├── thunder.py
    ├── todo_app
    │   ├── admin.py
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── models.py
    │   └── views.py
    └── todo_project
        ├── config.py
        ├── __init__.py
        └── routes.py

    12 directories, 21 files

You notice it create a package name with thesame name of your app (**todo_app**), also a directory inside **templates** and **static** folder

Register an app
===============

Once the app is created open a file called **todo_project/routes.py** and import your **todo_app** blueprint which is in (**todo_app/views.py**), default name given to an app blueprint, is the app name so our **todo_app** blueprint name is **todo_app**, after importing it, append (register) the app blueprint in a list called **reg_blueprints** in that same file of **todo_project/routes.py**

importing blueprint

.. code-block:: python

    from todo_app.views import todo_app

after that, append it in the list **reg_blueprints** provided in the **routes.py** file by

registering blueprint

.. code-block:: python

    reg_blueprints = [
      default,
      errors,
      auth,
      base,
      todo_app,
    ]

once you register the app, boot up the flask webserver again by::

    python thunder.py boot

This will bring the flask development server on port **5000** you can give it a different port by including a flag **-p** or **--port** flag which is for port number::

    python thunder.py boot -p 7000

or

.. code-block::

    python thunder.py boot --port 7000

The above command will bring the serve on port **7000** visit the localhost url with the port number, it will show you your project **index.html page** (todo_project). To get to your app default page (todo_app), visit the url with your app name in our case:

**http://127.0.0.1:7000/todo_app**

this will take you to your app **index.html page** (todo_app). From there you are ready to go.

Also, you can give your desire ip address/host by using **-H** or **--host** flag, e.g::

    python thunder.py boot -p 7000 -H 0.0.0.0

        or

    python thunder.py boot --port 7000 --host 0.0.0.0

For development server, you can give a debug value to True by specifying **-d** flag or **--debug** e.g::

    - python thunder.py boot -p 7000 -d True
        
        or

    - python thunder.py boot --port 7000 --debug True

Register model to admin page
############################

There are basically two ways that we can register our model to the admin page, one is registering the model class direct, while the other one is by creating a model view in the app `admin.py` file.

Register a model direct
=======================

In other to register your model directly, open your sub project folder and open the **config.py** file you see there. Import your app model that you want to register, above the method that will create the tables and database **db.create_all()** and you will see a commented prototype above it, then append it in the **reg_models = []** list within **admin_runner** function. That will register your model in the admin page and you will see it if you vist the admin page

Register a model view
=====================

In other to register your model directly, open your sub project folder and open the **config.py** file you see there. Import your app model that you want to register and also the model view of your model, above the method that will create the tables and database **db.create_all()** and you will see a commented prototype above it, now instead of append it in the **reg_models = []** list within **admin_runner** function, you are to go below for loop in (within admin_runner function) out side the loop and call the admin method called **add_view** and then pass your model view class as an argument, also pass an arguments in the model view class, the first argument is the model class, the second is the **db.session**, and then last give it a category (key word argument) **category="my_models_view". That will register your model in the admin page and you will see it if you vist the admin page.

see more documentationon how to write model view class of group of models get look at flask admin documentation `Flask-Admin <https://flask-admin.readthedocs.io/en/latest/introduction/#customizing-built-in-views>`_

.. _Admin user

You can create an admin user of your application user model, by running the following command::

    python thunder.py create_user

once you run it, a prompt will come up to input your information

.. toctree::
   :maxdepth: 2

   admin/index
   example
   
- `Repository <https://github.com/usmanmusa1920/sakyum>`_

- `Documentation <https://sakyum.readthedocs.io>`_

Pull requests are welcome
