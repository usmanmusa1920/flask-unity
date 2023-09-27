:tocdepth: 2

Admin user
==========

There are basically two ways in which you can create admin user. One is by using flags, second one is by prompt, you can combining both the two `prompt or flags`).

Let say you start a project, and an app inside the project by the following command

.. code-block:: bash
    flask_unity -p schoolsite && cd schoolsite && python run.py create_app -a exam
    .. or
    flask_unity --project schoolsite && cd schoolsite && python run.py create_app -a exam

**Admin user using flags:**

To start creating user in your database, you have to makemigrations and migrate the migration, if you haven't do it, like so

.. code-block:: bash
    flask_unity db makemigrations
    flask_unity db migrate

The first command will generate migration filee in the `migrations` directory and the initial database `default.db` file in our project base directory, instead of importing the db object from an interactive Python shell and run the `db.create_all()` or inserting `db.create_all()` below the import of our models in `schoolsite/config.py` file.

The second command will apply the generated migrations in the database `default.db`.

To create user in our databse, this can be done by given the `create_user` position argument and flags together with their values e.g::

    python run.py create_user -u network-engineer -e network-engineer@datacenter.com -p my-secret-pass

    # or

    python run.py create_user --username network-engineer --email network-engineer@datacenter.com --password my-secret-pass
    
.. warning::
    
    Don't use the `-p` flag to specify user password because the password will be visible to who so ever around, do so only if you are testing (not in production) by just giving the user username, and email address, then enter, where as the password will be prompt to enter it, like:

.. code-block:: python

    python run.py create_user -u network-engineer -e network-engineer@datacenter.com


**Admin user using prompt:**

This can be done by only given the `create_user` position argument and then hit tab, e.g::

    python run.py create_user

once you run it, a prompt will come up to input admin user information, these include `username`, `email`, and `password`


**Admin user using both `flags` and `prompt` :**

Use `-u` or `--username` and then the username beside it, if you do not specify it, you will see a prompt saying `Enter username:`::

    python run.py create_user -u network-engineer

    # or

    python run.py create_user --username network-engineer

Use `-e` or `--email` and then the email beside it, if you do not specify it, you will see a prompt saying `Enter email:`::

    python run.py create_user -e network-engineer@datacenter.com

    # or

    python run.py create_user --email network-engineer@datacenter.com

Use `-p` or `--password` and then the password beside it, if you do not specify it, you will see a prompt saying `Enter password:`::

    python run.py create_user -p my-secret-pass

    # or

    python run.py create_user --password my-secret-pass
