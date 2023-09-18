:tocdepth: 2

Templates / file system
#######################

Templates and static folder for each blueprint is located within (in side) the base templates/static directory, with thesame name of the bluprint, e.g let say we create an app `exam` in our project called `schoolsite` within the templates directory it will create (templates/exam) also for the static too (static/exam)

To access/link css file in html page use `<link rel="stylesheet" type="text/css" href="{{ url_for('exam.static', filename='css/style.css') }}">` for JavaScript is `<script src="{{ url_for('exam.static', filename='js/index.js') }}"></script>`

Customise admin page
====================

A default directory in which you can customise admin page is created in the (templates/admin) directory with a default `index.html` file that contains some links. You can style it with different css and js file, but make sure it is extended from **{% extends 'admin/master.html' %}** and anything else wrap it within the body block **{% block body %}  {% endblock body %}** You can edit the default contents to match your need!

File system storage
===================

The default directory where files will be saved is `media` which is in the project base directory. In the media directory there is a default user profile image called `default_img.png`, and if user change profile image it will be available (saved the new image) in that directory.
