:tocdepth: 2

Templates / static
##################

Templates and static folder for each blueprint is located within (in side) the base templates/static directory, with thesame name of the bluprint, e.g let say we create an app `exam` in our project called `Schoolsite` within the templates directory it will create (templates/exam) also for the static too (static/exam)

Customise admin page
====================

A default directory in which you can customise admin page is created in the (templates/admin) directory with a default `index.html` file that contains some links. You can style it with different css and js file, but make sure it is extended from **{% extends 'admin/master.html' %}** and anything else wrap it within the body block **{% block body %}  {% endblock body %}**

File system storage
===================

Lorem ipsum dolor sit amet consectetur, adipisicing elit. Sed voluptate dicta ut harum, unde quisquam blanditiis libero, dolorem aut natus, debitis cupiditate accusamus ducimus adipisci accusantium quam dignissimos pariatur. Alias?
