:tocdepth: 2

Flags & CLI
###########

Some useful flags and CLI that you can use along side, when your are running your application (project) along side with `run.py` file are as follows:

**CLI associated with `flask-unity`**:

To initialize a project use `-p` or `--project` as::

    flaskunity -p schoolsite
    .. or
    flaskunity --project schoolsite

To make migrations::

    flaskunity db makemigrations

To apply the migrations::

    flaskunity db migrate

**Flags associated with `create_app` positional argument**:

Use `-a` or `--app` if you are about to create app in your project, that will capture the app name::

    python run.py create_app -a blog

    # or

    python run.py create_app --app blog

**Flags associated with `boot` positional argument**:

Use `-p` or `--port` if you want to give your desire port number instead of the default one which is `5000` It is use only if you are about to bring up the server, after the positional argument of `boot`::

    python run.py boot -p 7000

    # or

    python run.py boot --port 7000

Use `-H` or `--host` if you are to give a different host, in the case of deployment. Also, it is use if you are about to bring up the server, after the positional argument of `boot`::

    python run.py boot -H 0.0.0.0

    # or

    python run.py boot --host 0.0.0.0

Use `-d` or `--debug` if you want your app in debug mode. That mean ifyou make change, you need not to shutdown the server and reload it again, it will do that automatically once you set it to `True` Also, it is use if you are about to bring up the server, after the positional argument of `boot`::

    python run.py boot -d True

    # or

    python run.py boot --debug True

**Flags associated with `create_user` positional argument**:

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
