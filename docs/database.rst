:tocdepth: 2

Database migration
##################

Welcome to the chapter that will talk about how to do database migration. By default the database that it (sakyum) come with is an sqlite database with naming convention of **default.db** located in the parent folder of your project. The main talk here is to show how we can make database migrations and stuffs like that. We are going to use `alembic`.

`Alembic` is a very useful library we can use for our database migrations. when we are working with Flask Framework we need a tool which can handle the database migrations. Alembic is widely used for migrations. Let us start how to use alembic. First install `alembic` by::

  pip install alembic

After installing the alembic we need to initialize the alembic to our working project directory (parent) directory, by running the following command::

  alembic init alembic

After running this command you will see some files and folders are created in your project directory they are `alembic` and `alembic.ini` the tree structure of the `alembic` directory is::

  alembic
  ├── env.py
  ├── README
  ├── script.py.mako
  └── versions

  1 directory, 3 files

Notice there will be no version files in your versions directory because we haven’t made any migrations yet. Now to use alembic we need to do certain changes in these files. First, change the sqlalchemy.url in your alembic.ini file, and give it your reletive `default.db` path, ours look like::

  # for the default.db file
  sqlalchemy.url = sqlite:////home/usman/Desktop/Schoolsite/default.db

  # for mysql (if you are using mysql database)
  sqlalchemy.url = mysql+mysqldb://root:root@localhost:3306/database_name

  # for postgresql (if youare using postgres database)
  sqlalchemy.url = postgresql://user:user@localhost/test

After giving your database url, open a file that it generate in the alembic directory **alembic/env.py** find a variable called `target_metadata = None`, above it import your app models and the **db** instance of your application and replace the value of `None` with `db.Model.metadata` like in the below snippets, ``make sure you don't import your app models in the project config.py file (Schoolsite.config.py) until after you run the make migration``::

  from exam.models import ExamQuestionModel, ExamChoiceModel
  from Schoolsite.config import db
  target_metadata = db.Model.metadata

For Autogenerating Multiple MetaData collections, you can pass a list of models instead e.g::

  from myapp.mymodel1 import Model1Base
  from myapp.mymodel2 import Model2Base
  target_metadata = [Model1Base.metadata, Model2Base.metadata]

Lastly make the migrations (Create a Migration Script) by runnig the following command::

  alembic revision --autogenerate -m "Added table"

Before, in the `alembic/versions` directory there is nothing inside, but now after running the above command, alembic generate our first migration commit file in versions folder `(alembic/versions)`, you can see the version file now in the versions folder, for simplicity the structure look like::

  alembic
  ├── env.py
  ├── __pycache__
  │   └── env.cpython-310.pyc
  ├── README
  ├── script.py.mako
  └── versions
      ├── 83241ca0f125_added_table.py
      └── __pycache__
          └── 83241ca0f125_added_table.cpython-310.pyc

  3 directories, 6 files

Once this file generates we are ready for database migration. To migrate we are to run::

  alembic upgrade head

Once you run the above command your tables will be generated in your database. This is how to use alembic for your database, there are many you can do so, hit to the `alembic <https://alembic.sqlalchemy.org>`_ website for more clarification.


Hint
----

  - To make migrations (Create a Migration Script)::

    alembic revision --autogenerate -m "Added table"

  - To migrate (Running our Migration)::

    alembic upgrade head

  - Getting Information::

    alembic current

    alembic history --verbose
    
  - Downgrading, We can illustrate a downgrade back to nothing, by calling alembic downgrade back to the beginning, which in Alembic is called base::

    alembic downgrade base

Other database management command will be implemented, they are: `update_db` `dump_db` `cleaned_db`
