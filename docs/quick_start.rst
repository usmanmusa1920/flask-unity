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

Now after the installation, let create a project called **schoolsite** to do so paste the following command on your termianl::

  python -c "from flask_unity import project; project('schoolsite')"

or create a file and paste the below codes which is equivalent of the above, and then run the file

.. code-block:: python

  from flask_unity import project

  project("schoolsite")

Both the command you type on terminal or the code you paste in a file (after running the file) will create a project called **schoolsite** now cd into the **schoolsite** directory, if you do **ls** within the directory you just enter you will see a module called **thunder.py** and some directories (some in the form of package) **media**, **static**, **templates** and a directory with thesame name of your parent directory which is **schoolsite**.

Tree structure of the project using **tree .** command look like:

.. code-block::

  .
  ├── media
  │   └── default_img.png
  ├── schoolsite
  │   ├── config.py
  │   ├── __init__.py
  │   ├── routes.py
  │   └── secret.py
  ├── static
  │   └── schoolsite
  │       ├── index.js
  │       ├── media
  │       └── style.css
  ├── templates
  │   ├── admin
  │   │   └── index.html
  │   └── schoolsite
  │       └── index.html
  └── thunder.py

  8 directories, 10 files

Boot up the flask server by running the below command::

  python thunder.py boot

Now visit the local url **http://127.0.0.1:5000** this will take you to the index page of your project with some links in the page.

Create flask project app using flask_unity
==========================================

Since we create a project, let create an app within the project. To start an app within the project (**schoolsite**) shutdown the flask development server by pressing ( CTRL+C ). If you do **ls** in that same directory you will see it create a **default.db** file (an sqlite file) which is our default database. Now run the following command in other to create your app, by giving the name you want your app to be, in our case we will call our app **exam**::

  python thunder.py create_app -a exam

  # or

  python thunder.py create_app --app exam

this will create an app (a new package called **exam**) within the project (**schoolsite**), the **-a** flag is equivalent to **--app** which is a flag for the app name in this example it is called **exam**

Now the **tree .** structure of the project after creating **exam** app look like:

.. code-block::

  .
  ├── default.db
  ├── exam
  │   ├── admin.py
  │   ├── forms.py
  │   ├── __init__.py
  │   ├── models.py
  │   └── views.py
  ├── media
  │   └── default_img.png
  ├── schoolsite
  │   ├── config.py
  │   ├── __init__.py
  │   ├── routes.py
  │   └── secret.py
  ├── static
  │   ├── exam
  │   │   ├── index.js
  │   │   ├── media
  │   │   └── style.css
  │   └── schoolsite
  │       ├── index.js
  │       ├── media
  │       └── style.css
  ├── templates
  │   ├── admin
  │   │   └── index.html
  │   ├── exam
  │   │   └── index.html
  │   └── schoolsite
  │       └── index.html
  └── thunder.py

  12 directories, 19 files

You notice it create a package name with thesame name of the app (**exam**) with some files in it, also a directory named **exam** inside **templates** and **static** folder with default html page together with css and js files (in static folder)

Register an app
===============

Once the app is created it is time to register the app, to do so open a file **schoolsite/routes.py** and import your **exam** app blueprint which is in (**exam/views.py**), default name given to an app blueprint, is the app name so our **exam** app blueprint name is **exam**, after importing it, append (register) the app blueprint in a list called **reg_blueprints** in that same file of **schoolsite/routes.py**

``**WARNING** don't ommit the registered blueprint you see in the `reg_blueprints` list **(blueprint.default, blueprint.errors, blueprint.auth, base)** blueprints just append your app blueprint``

importing blueprint

.. code-block:: python

  from exam.views import exam

after that, append it in the list **reg_blueprints** provided in the **routes.py** file by

registering blueprint

.. code-block:: python

  reg_blueprints = [
    blueprint.default,
    blueprint.errors,
    blueprint.auth,
    base,
    exam,
  ]

once you register the app, boot up the flask webserver again by::

  python thunder.py boot

This will bring the flask development server on port **5000** you can give it a different port by including a flag **-p** or **--port** flag which is for port number::

  python thunder.py boot -p 7000

  # or

  python thunder.py boot --port 7000

The above command will bring the development serve on port **7000** visit the localhost url with the port number, it will show you your project **index page** (schoolsite). To get to the app `(exam)` default page, visit the url with your app name in our case:

**http://127.0.0.1:7000/exam**

this will take you to the app (exam) **index page**, and you can also vist the admin page with this url **http://127.0.0.1:7000/admin**

Also, you can give your desire ip address/host by using **-H** or **--host** flag, e.g::

  python thunder.py boot -p 7000 -H 0.0.0.0

  # or

  python thunder.py boot --port 7000 --host 0.0.0.0

For development server, you can give a debug value to True by specifying **-d** flag or **--debug** e.g::

  python thunder.py boot -p 7000 -d True
      
  # or

  python thunder.py boot --port 7000 --debug True

You can change your default profile picture by moving to http://127.0.0.1:5000/admin/change_profile_image/ and select your new picture from your file system.

With this, you can do many and many stuffs now! From here you are ready to keep write more views in the app `views.py` as well as in the project `routes.py` and do many stuffs just like the way you do if you use flask only.

Source code for this `quick start` is available at official `github <https://github.com/usmanmusa1920/flask-unity/tree/master/example/quick_start>`_ repository of the project.
