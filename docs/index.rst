
Flask-Unity
###########

**Flask-Unity** an extension of flask web framework that erase the complexity of structuring flask project blueprint, packages, connecting other flask extensions, database migrations, and other annoying stuffs. For more about visit this `page <https://flask-unity.readthedocs.io/en/latest/know.html>`_

Release v\ |version|


.. image:: https://static.pepy.tech/badge/flask-unity/month
    :target: https://pepy.tech/project/flask-unity
    :alt: Flask-Unity Downloads Per Month Badge
    
.. image:: https://img.shields.io/pypi/l/flask-unity.svg
    :target: https://pypi.org/project/flask-unity/
    :alt: License Badge

.. image:: https://img.shields.io/pypi/wheel/flask-unity.svg
    :target: https://pypi.org/project/flask-unity/
    :alt: Wheel Support Badge

.. image:: https://img.shields.io/pypi/pyversions/flask-unity.svg
    :target: https://pypi.org/project/flask-unity/
    :alt: Python Version Support Badge
    
-------------------

**Simple usage**::

    pip install --upgrade flask_unity # install the library

    flask_unity -p schoolsite # create project

    cd schoolsite # cd into project directory

    flask_unity db makemigrations # make migrations

    flask_unity db migrate # apply migrations

    python run.py boot # run development server

Now visit `http://localhost:5000 <http://localhost:5000>`_

-------------------

Table of content
----------------

.. toctree::
    :maxdepth: 2

    quick_start
    create_models
    app_forms
    admin_user
    custom_auth
    database
    cli
    conn_ext
    error_pages
    page_and_filesystem
    know

Useful links:
-------------

- `Repository <https://github.com/usmanmusa1920/flask-unity>`_

- `PYPI Release <https://pypi.org/project/flask-unity>`_

Flask-unity default page
------------------------

.. image:: https://raw.githubusercontent.com/usmanmusa1920/flask-unity/master/docs/_static/flask_unity_default_page.png
    :align: center
