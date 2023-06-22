:tocdepth: 2

Admin user
==========

There are basically two ways in which you can create admin user. One is by using flags, second one is by prompt, and the other one is by using (combining both the two `prompt or flags`).

Let say you start a project, and an app inside the project by the following command::

  python -c "from sakyum import project; project('schoolsite')" && cd schoolsite && python thunder.py create_app -a exam


**Admin user using flags:**

This can be done by given the `create_user` position argument and flags together with their values e.g::

  python thunder.py create_user -u network-engineer -e network-engineer@datacenter.com -p my-secret-pass

  # or

  python thunder.py create_user --username network-engineer --email network-engineer@datacenter.com --password my-secret-pass


``Warning:`` don't use the `-p` flag to specify user password, do so only if you are testing (not in production) by just giving the user username, and email address, then enter, where as the password will be prompt to enter it, like:

.. code-block:: python

  python thunder.py create_user -u network-engineer -e network-engineer@datacenter.com


**Admin user using prompt:**

This can be done by only given the `create_user` position argument and then hit tab, e.g::

    python thunder.py create_user

once you run it, a prompt will come up to input admin user information, these include `username`, `email`, and `password`


**Admin user using both `flags` and `prompt` :**

Use `-u` or `--username` and then the username beside it, if you do not specify it, you will see a prompt saying `Enter username:`::

  python thunder.py create_user -u network-engineer

  # or

  python thunder.py create_user --username network-engineer

Use `-e` or `--email` and then the email beside it, if you do not specify it, you will see a prompt saying `Enter email:`::

  python thunder.py create_user -e network-engineer@datacenter.com

  # or

  python thunder.py create_user --email network-engineer@datacenter.com

Use `-p` or `--password` and then the password beside it, if you do not specify it, you will see a prompt saying `Enter password:`::

  python thunder.py create_user -p my-secret-pass

  # or

  python thunder.py create_user --password my-secret-pass
