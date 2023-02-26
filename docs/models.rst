:tocdepth: 2

Models
######

There are basically two ways that we can register our model to the admin page, one is registering the model class direct, while the other one is by creating a model view in the app `admin.py` file.

Register a model direct
======================

In other to register your model directly, open your sub project folder and open the **config.py** file you see there. Import your app model that you want to register, above the method that will create the tables and database **db.create_all()** and you will see a commented prototype above it, then append it in the **reg_models = []** list within **admin_runner** function. That will register your model in the admin page and you will see it if you vist the admin page

Register a model view
===================

In other to register your model directly, open your sub project folder and open the **config.py** file you see there. Import your app model that you want to register and also the model view of your model, above the method that will create the tables and database **db.create_all()** and you will see a commented prototype above it, now instead of append it in the **reg_models = []** list within **admin_runner** function, you are to go below for loop in (within admin_runner function) out side the loop and call the admin method called **add_view** and then pass your model view class as an argument, also pass an arguments in the model view class, the first argument is the model class, the second is the **db.session**, and then last give it a category (key word argument) **category="my_models_view". That will register your model in the admin page and you will see it if you vist the admin page.

see more documentationon how to write model view class of group of models get look at flask admin documentation `Flask-Admin <https://flask-admin.readthedocs.io/en/latest/introduction/#customizing-built-in-views>`_

Admin user
==========

You can create an admin user of your application user model, by running the following command::

    python thunder.py create_user

once you run it, a prompt will come up to input your information

Model api
=========

Admin custome model
===================

Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sed voluptate dicta ut harum, unde quisquam blanditiis libero, dolorem aut natus, debitis cupiditate accusamus ducimus adipisci accusantium quam dignissimos pariatur. Alias?
