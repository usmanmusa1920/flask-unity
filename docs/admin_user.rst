:tocdepth: 2

Admin user
==========

There are basically two ways in which you can create admin user. One is by using flags, second one is by prompt, and the other one is by using (combining both the two `prompt or flags`).


**Admin user using flags:**

This can be done by given the `create_user` position argument and flags together with their values e.g::

  python thunder.py create_user -u network-engineer -e network-engineer@datacenter.com -p p@s$w0d

or

.. code-block::

  python thunder.py create_user --username network-engineer --email network-engineer@datacenter.com --password p@s$w0d


**Admin user using prompt:**

This can be done by only given the `create_user` position argument and then hit tab, e.g::

    python thunder.py create_user

once you run it, a prompt will come up to input admin user information, these include `username`, `email`, and `password`


**Admin user using both `flags` and `prompt` :**

Use `-u` or `--username` and then the username beside it, if you do not specify it, you will see a prompt saying `Enter username:`::

  python thunder.py create_user -u network-engineer

or

.. code-block::

  python thunder.py create_user --username network-engineer

Use `-e` or `--email` and then the email beside it, if you do not specify it, you will see a prompt saying `Enter email:`::

  python thunder.py create_user -e network-engineer@datacenter.com

or

.. code-block::

  python thunder.py create_user --email network-engineer@datacenter.com

Use `-p` or `--password` and then the password beside it, if you do not specify it, you will see a prompt saying `Enter password:`::

  python thunder.py create_user -p p@s$w0d

or

.. code-block::

  python thunder.py create_user --password p@s$w0d
