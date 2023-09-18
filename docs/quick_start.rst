:tocdepth: 2

Quick start
###########

First we recomend you to create a virtual environment to avoid conflict (upgrade/downgrade of some of your system libraries) when installing flask_unity, this is just a recomendation, it still work even if you install it without using virtual environment

Install and update the latest release from `pypi <https://pypi.org/project/flask-unity>`_. Basically the library was uploaded using **sdist** (Source Distribution) and **bdist_wheel** (Built Distribution), this software (library) is compatible and also tested with **windows OS**, **linux**, **macOS** and possibly can be compabible with others too!.

You will notice we use **--upgrade** in the installation command, this will make sure it install the latest release from pypi (in case you have a version which is not the latest), you can still ommit the `--upgrade` and use the version you want then wait for the installation to finish.::

    pip install --upgrade flask_unity

This **quick start** will walk you through creating project called **schoolsite** and a basic application called **exam** in the project. User will be able to register, login/logout, create exam questions/choices, and edit or delete their own question/choices. All using `flask_unity`, you will be able to clone it on `github <https://github.com/usmanmusa1920/flask-unity>`_. it is located inside example directory of the base repository.

Create flask project using flask_unity
======================================

Now after the installation, let create a project called **schoolsite** to do so paste either (one) of the following command on your termianl:

.. code-block:: bash
    flask_unity -p schoolsite
    .. or
    flask_unity --project schoolsite

Both (either of) the command you type on terminal will create a project called **schoolsite** now cd into the **schoolsite** directory, if you do **ls** within the directory you just enter you will see a module called **run.py**, **alembic.ini** and some directories (some in the form of package) **media**, **static**, **migrations**, **templates** and a directory with thesame name of your parent directory which is **schoolsite**.

Tree structure of the project using **tree .** command look like:

.. code-block:: bash

    .
    ├── alembic.ini
    ├── media
    │   └── default_img.png
    ├── migrations
    │   ├── env.py
    │   ├── README
    │   ├── script.py.mako
    │   └── versions
    ├── run.py
    ├── schoolsite
    │   ├── config.py
    │   ├── __init__.py
    │   ├── routes.py
    │   └── secret.py
    ├── static
    └── templates
        └── admin
            └── index.html

    7 directories, 11 files

Next make migrations by:

.. code-block:: bash
    flask_unity db makemigrations

If you do **ls** after making the migrations you will see it initiate a **default.db** file (an sqlite file) which is our default database. Apply the migrations:

.. code-block:: bash
    flask_unity db migrate

Now ready to boot up the flask server by running the below command::

    python run.py boot

Visit the local url **http://127.0.0.1:5000** this will take you to the index page of your project with some links in the page.

.. note::
    
    As soon as you create the project make migrations and apply the migrations to avoid errors!

Create flask project app using flask_unity
==========================================

Since we create a project, let create an app within the project. To start an app within the project (**schoolsite**) shutdown the flask development server by pressing `CTRL+C`. Run the following command in other to create an app, by giving the app name, you want your app to be, in our case we will call our app **exam**::

    python run.py create_app -a exam

    # or

    python run.py create_app --app exam

this will create an app (a new package called **exam**) within the project (**schoolsite**), the **-a** flag is equivalent to **--app** which is a flag for the app name in this example it is called **exam**

Now the **tree .** structure of the project after creating **exam** app look like:

.. code-block:: bash

    .
    ├── alembic.ini
    ├── default.db
    ├── exam
    │   ├── admin.py
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── models.py
    │   └── views.py
    ├── media
    │   └── default_img.png
    ├── migrations
    │   ├── env.py
    │   ├── __pycache__
    │   │   └── env.cpython-310.pyc
    │   ├── README
    │   ├── script.py.mako
    │   └── versions
    │       ├── 86121042216e_changes_migrated.py
    │       └── __pycache__
    │           └── 86121042216e_changes_migrated.cpython-310.pyc
    ├── run.py
    ├── schoolsite
    │   ├── config.py
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── config.cpython-310.pyc
    │   │   ├── __init__.cpython-310.pyc
    │   │   ├── routes.cpython-310.pyc
    │   │   └── secret.cpython-310.pyc
    │   ├── routes.py
    │   └── secret.py
    ├── static
    │   └── exam
    │       ├── css
    │       │   └── style.css
    │       ├── js
    │       │   └── index.js
    │       └── media
    └── templates
        ├── admin
        │   └── index.html
        └── exam
            └── index.html

    16 directories, 27 files

You notice it create a package name with thesame name of the app (**exam**) with some files in it, also a directory named **exam** inside **templates** and **static** folder with default html page together with css and js files (in static folder)

Register an app
===============

Once the app is created it is time to register the app, to do so open a file **schoolsite/routes.py** and import your **exam** app blueprint which is in (**exam/views.py**), default name given to an app blueprint, is the app name so our **exam** app blueprint name is **exam**, after importing it, append (register) the app blueprint in a list called **reg_blueprints** in that same file of **schoolsite/routes.py**

importing blueprint

.. code-block:: python

    from exam.views import exam

after importing it, append (register) the app blueprint in a function called `reg_blueprints_func`, which was assigned to `reg_blueprints` in that same file of `schoolsite/routes.py`

.. code-block:: python

    reg_blueprints = reg_blueprints_func(
        exam,
    )

once you register the app, boot up the flask webserver again by::

    python run.py boot

This will bring the flask development server on port **5000** you can give it a different port by including a flag **-p** or **--port** flag which is for port number::

    python run.py boot -p 7000

    # or

    python run.py boot --port 7000

The above command will bring the development serve on port **7000** visit the localhost url with the port number, it will show you your project **index page** (schoolsite). To get to the app `(exam)` default page, visit the url with your app name in our case:

**http://127.0.0.1:7000/exam**

this will take you to the app (exam) **index page**, and you can also vist the admin page with this url **http://127.0.0.1:7000/admin**

Also, you can give your desire ip address/host by using **-H** or **--host** flag, e.g::

    python run.py boot -p 7000 -H 0.0.0.0

    # or

    python run.py boot --port 7000 --host 0.0.0.0

For development server, you can give a debug value to True (for auto reload of changes) by specifying **-d** flag or **--debug** e.g::

    python run.py boot -p 7000 -d True
        
    # or

    python run.py boot --port 7000 --debug True

You can change your default profile picture by moving to http://127.0.0.1:5000/admin/change_profile_image/ and select your new picture from your file system, once logged in.

With this, you can do many and many stuffs now! From here you are ready to keep write more views in the app `views.py` as well as in the project `routes.py` and do many stuffs just like the way you do if you use flask only.

Source code for this `quick start` is available at official `github <https://github.com/usmanmusa1920/flask-unity/tree/master/example/quick_start>`_ repository of the project.
