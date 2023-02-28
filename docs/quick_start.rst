:tocdepth: 2

Quick start
###########

First we recomend you to create a virtual environment to avoid conflict (upgrade/downgrade of some of your system libraries) when installing sakyum, this is just a recomendation, it still work even if you install it without using virtualenvironment

Install and update the latest release from `pypi <https://pypi.org/project/sakyum>`_. Basically the library was uploaded using **sdist** (Source Distribution) and this software (library) might not be compatible with **windows operating system** but it works on other **OS** such as **linux** and **macOS**, but very soon the version that will be compatible with **windows operating system** will be release, stay tuned.

you will notice we use **--upgrade** in the installation command, this will make sure it install the latest release from pypi (in case you have a version which is not the latest version), you can still ommit the `--upgrade` and use the version you want then wait for the installation to finish.::

  pip install --upgrade sakyum

Create flask project using sakyum
============================================

After the installation paste the following command on your termianl::

  python -c "from sakyum import project; project('Schoolsite')"

or create a file and paste the below codes which is equivalent of the above, and then run the file

.. code-block:: python

    from sakyum import project

    project("Schoolsite")

Both the command you type on terminal or the code you paste in a file (after running the file) will create a project called **Schoolsite** now cd into the **Schoolsite** directory, if you do **ls** within the directory you just enter you will see a module called **thunder.py** and some directories (some in the form of package) **auth**, **static**, **templates** and a directory with the same name of your base directory name, in our case it is **Schoolsite**.

Tree structure of your project look like (using tree package)

.. code-block::

    tree .

.. code-block::

    .
    ├── auth
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── models.py
    │   └── routes.py
    ├── Schoolsite
    │   ├── config.py
    │   ├── __init__.py
    │   ├── routes.py
    │   └── secret.py
    ├── static
    │   └── Schoolsite
    │       ├── index.js
    │       ├── media
    │       └── style.css
    ├── templates
    │   ├── admin
    │   │   └── index.html
    │   └── Schoolsite
    │       └── index.html
    └── thunder.py

    8 directories, 13 files

Boot up the flask server by running the below command::

    python thunder.py boot

Now visit the local url **http://127.0.0.1:5000** this will show you index page of your project

Create flask project app using sakyum
=====================================

For you to start an app within your project (**Schoolsite**) shutdown the flask development server by pressing ( CTRL+C ). If you do **ls** in that same directory you will see it create a **default.db** file (an sqlite file). Now run the following command in other to create your app, by giving the name you want your app to be, in our case we will call our app **exam**::

    python thunder.py create_app -a exam

or

.. code-block::

    python thunder.py create_app --app exam

this will create an app (a new package called **exam**) within your project (**Schoolsite**), the **-a** flag is equivalent to **--app** which is a flag for the app name in this example it is called **exam**

Now the tree structure of your project after creating **exam** app look like (using tree package)

.. code-block::

    tree .

.. code-block::

    .
    ├── auth
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── models.py
    │   └── routes.py
    ├── default.db
    ├── exam
    │   ├── admin.py
    │   ├── forms.py
    │   ├── __init__.py
    │   ├── models.py
    │   └── views.py
    ├── Schoolsite
    │   ├── config.py
    │   ├── __init__.py
    │   ├── routes.py
    │   └── secret.py
    ├── static
    │   ├── exam
    │   │   ├── index.js
    │   │   ├── media
    │   │   └── style.css
    │   └── Schoolsite
    │       ├── index.js
    │       ├── media
    │       └── style.css
    ├── templates
    │   ├── admin
    │   │   └── index.html
    │   ├── exam
    │   │   └── index.html
    │   └── Schoolsite
    │       └── index.html
    └── thunder.py

    12 directories, 22 files

You notice it create a package name with thesame name of your app (**exam**), also a directory named **exam** inside **templates** and **static** folder with default html page together with css and js files (in static folder)

Register an app
===============

Once the app is created open a file **Schoolsite/routes.py** and import your **exam** blueprint which is in (**exam/views.py**), default name given to an app blueprint, is the app name so our **exam** blueprint name is **exam**, after importing it, append (register) the app blueprint in a list called **reg_blueprints** in that same file of **Schoolsite/routes.py**

**warning:** `don't ommit the registered blueprint you see in the list **(default, errors, auth, base)** blueprints` just append your app blueprint

importing blueprint

.. code-block:: python

    from exam.views import exam

after that, append it in the list **reg_blueprints** provided in the **routes.py** file by

registering blueprint

.. code-block:: python

    reg_blueprints = [
      default,
      errors,
      auth,
      base,
      exam,
    ]

once you register the app, boot up the flask webserver again by::

    python thunder.py boot

This will bring the flask development server on port **5000** you can give it a different port by including a flag **-p** or **--port** flag which is for port number::

    python thunder.py boot -p 7000

or

.. code-block::

    python thunder.py boot --port 7000

The above command will bring the serve on port **7000** visit the localhost url with the port number, it will show you your project **index page** (Schoolsite). To get to your app default page (exam), visit the url with your app name in our case:

**http://127.0.0.1:7000/exam**

this will take you to your app **index page** (exam), and you can also vist the admin page with this url **http://127.0.0.1:7000/admin**

Also, you can give your desire ip address/host by using **-H** or **--host** flag, e.g::

    python thunder.py boot -p 7000 -H 0.0.0.0

or

.. code-block::

    python thunder.py boot --port 7000 --host 0.0.0.0

For development server, you can give a debug value to True by specifying **-d** flag or **--debug** e.g::

    python thunder.py boot -p 7000 -d True
        
or

.. code-block::

    python thunder.py boot --port 7000 --debug True

With this, you can do many and many project now!
