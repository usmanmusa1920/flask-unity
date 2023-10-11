:tocdepth: 2

Templates / file system
#######################

Templates and static folder for each blueprint is located within (in side) the base templates/static directory, with thesame name of the bluprint, e.g let say we create an app `exam` in our project called `schoolsite` within the templates directory it will create (templates/exam) also for the static too (static/exam)

To access/link css file in html page use `<link rel="stylesheet" type="text/css" href="{{ url_for('exam.static', filename='css/style.css') }}">` for JavaScript is `<script src="{{ url_for('exam.static', filename='js/index.js') }}"></script>`

Customise admin page
====================

A default directory in which you can customise admin page is created in the (templates/admin) directory with a default `index.html` file that contains some links. You can style it with different css and js file, but make sure it is extended from **{% extends 'admin/master.html' %}** and anything else wrap it within the body block **{% block body %}  {% endblock body %}** You can edit the default contents to match your need!

Note, when you remove the default `base` blueprint inside the `reg_blueprints_func` function of your project, the admin index.html customisation won't populate, that mean making the function (reg_blueprints_func) with no param pass in it, will make it not to populate. But as you register any of your app, it will display even if you remove the default passed blueprint.

The default `base` blueprint in your project routes.py file is just to make the admin page to display, but you can still use that blueprint for making some route.

File system storage
===================

The default directory where files will be saved is `media` which is in the project base directory. In the media directory there is a default user profile image called `default_img.png`, and if user change profile image it will be available (saved the new image) in that directory.
