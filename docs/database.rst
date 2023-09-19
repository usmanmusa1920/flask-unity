:tocdepth: 2

Database migration
##################

Welcome to the chapter that will talk about how to do database migration with `alembic`. By default the database that it (flask_unity) come with is an sqlite database with naming convention of **default.db** located in the parent folder of your project. The main talk here is to show how we can make database migrations and stuffs like that.

**Migrations** are very powerful and let you change your models over time, as you develop your project, without the need to delete your database or tables and make new ones - it specializes in upgrading your database live, without losing data. More will be gist later.

`Alembic` is a very useful library we can use for our database migrations. when we are working with Flask Framework we need a tool which can handle the database migrations. Alembic is widely used for migrations. Alembic version `1.10.2` come with (Mako=1.2.4, MarkupSafe=2.1.2, SQLAlchemy=2.0.7, greenlet=2.0.2, typing-extensions=4.5.0) extensions, let us start how to use alembic.

Alembic is already initialized to our working project directory (parent) directory, you noticed when we create the project (a folder `migrations`, and file `alimbic.ini` are generated in the project dir), and the contents of this folder need to be added to version control along with your other source files. The tree structure of the `migrations` directory looks like::

    migrations
    ├── env.py
    ├── README
    ├── script.py.mako
    └── versions

    1 directory, 3 files

Notice there will be no version files in your versions directory `(migrations/versions)` because we haven’t made any migrations yet. It also already populate the `sqlalchemy.url` in your `alembic.ini` file, and gave it your reletive `default.db` path, ours look like::

    # for the default.db file
    sqlalchemy.url = sqlite:////home/usman/Desktop/schoolsite/default.db

Other RDBMS can be configure as:

.. code-block:: bash

    # for mysql (if you are using mysql database)
    sqlalchemy.url = mysql+mysqldb://root:root@localhost:3306/database_name

    # for postgresql (if you are using postgres database)
    sqlalchemy.url = postgresql://user:user@localhost/test

Also in a file that it generate in the migrations directory **migrations/env.py** it imported the **db** instance of your application, which look like::

    # from <app_name>.models import <app_model>
    from flask_unity.contrib import db
    target_metadata = db.Model.metadata

For Autogenerating Multiple MetaData collections, you can pass a list of models instead of the above, e.g::

    from myapp.mymodel1 import Model1Base
    from myapp.mymodel2 import Model2Base
    target_metadata = [Model1Base.metadata, Model2Base.metadata]

Next is to make the migrations (Create a Migration Script) by runnig the following command::

    flask_unity db makemigrations

Before, in the `migrations/versions` directory there is nothing inside, but now after running the above command, alembic generate our first migration commit file in versions folder `(migrations/versions)`, you can see the version file now in the versions folder, for simplicity the structure look like::

    migrations
    ├── env.py
    ├── __pycache__
    │   └── env.cpython-310.pyc
    ├── README
    ├── script.py.mako
    └── versions
        ├── ac25f12f55b0_added_tables.py
        └── __pycache__
            └── ac25f12f55b0_added_tables.cpython-310.pyc

    3 directories, 6 files

Every commit we did, it will generate the migration file in the `(migrations/versions)` directory. Once this file generates we are ready for database migration. To migrate we are to run::

    flask_unity db migrate

Once you run the above command your tables will be generated in your database. This is how to use alembic for your database, there are many you can do so, hit to the `alembic <https://alembic.sqlalchemy.org>`_ website for more clarification.

Each time the database models change, repeat the `makemigrations` and `migrate` commands.

**Hint**

  - To make migrations (Create a Migration Script)::

    flask_unity db makemigrations

    or

    alembic revision --autogenerate -m "Changes migrated!"

  - To migrate (Running our Migration)::

    flask_unity db migrate

    or

    alembic upgrade head

  - Getting Information more command on `alembic site <https://alembic.sqlalchemy.org/en/latest/tutorial.html#getting-information>`_::

    alembic current

    alembic history --verbose
    
  - Downgrading, We can illustrate a downgrade back to nothing, by calling alembic downgrade back to the beginning, which in Alembic is called base::

    alembic downgrade base
