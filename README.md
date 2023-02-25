
# Sakyum

An extension of flask web framework that erase the complexity of structuring flask project blueprint, packages, and other annoying stuffs.

The main reason behind the development of `sakyum` is to combine <a href="https://flask.palletsprojects.com">flask</a> and it extensions in one place to make it ease when developing an application without the headache (worrying) of knowing the tricks on how to connect those extensions with flask, or import something from somewhere to avoid some errors such as circular import and other unexpected errors. Also structuring flask application is a problem at some cases, `sakyum` take care of all these so that you will only focus on writing your application views the way you want.

Sakyum come with the following flask popular and useful extensions, these include: <a href="https://flask-admin.readthedocs.io">flask-admin</a> where you can manage your models in the admin page, <a href="https://flask-bcrypt.readthedocs.io">flask-bcrypt</a> that will hash user password and other security issues, <a href="https://flask-login.readthedocs.io">flask-login</a> for login/logout session and other security tricks to make sure user cookie is safe, <a href="https://flask-sqlalchemy.palletsprojects.com">flask-sqlalchemy</a> for creating/inserting and other database management command, <a href="https://flask-wtf.readthedocs.io">flask-wtf</a> representing html page in the form of class. And possibly some other extensions.

<h3><Installation</h3>

Install and update the latest release from <a href="https://pypi.org/project/sakyum">pypi</a>

```py
pip install --upgrade sakyum
```

Basically the library was uploaded using `sdist` (Source Distribution) and this software (library) might not be compatible with `windows operating system` but it works on other `OS` such as `linux` and `macOS`

<h3>Create your first flask project using sakyum</h3>

After the installation paste the following command on your termianl

```py
python -c "from sakyum import project; project('todo_project')"
```

this will create a project (directory) called `todo_project` now cd into the `todo_project` directory, if you do `ls` within the directory you just enter, you will see a module called `thunder.py` and some directories (some in the form of package) `auth`, `static`, `templates` and a directory with thesame name of your base directory name, in our case it is `todo_project`.

Boot up the flask server by running the below command

```py
python thunder.py boot
```

Now visit the local url `http://127.0.0.1:5000` this will show you index page of your project

<h3>Create flask app within your project (todo_project)</h3>

For you to start an app within your project `todo_project` shutdown the flask development server by pressing ( CTRL+C ) and then run the following command, by giving the name you want your app to be, in our case we will call our app `todo_app`

```py
python thunder.py create_app -a todo_app
```

this will create an app (a new package called `todo_app`) within your project `(todo_project)`

<h3>Register an app</h3>

Once the app is created open a file called `todo_project/routes.py` and import your `todo_app` blueprint which is in (`todo_app/views.py`), default name given to an app blueprint, is the app name so our `todo_app` blueprint name is `todo_app`, after importing it, append (register) the app blueprint in a list called `reg_blueprints` in thatsame file of `todo_project/routes.py`

importing blueprint

```py
from todo_app.views import todo_app
```

registering blueprint

```py
reg_blueprints = [
  default,
  errors,
  auth,
  base,
  todo_app,
]
```

once you register the app, boot up the flask webserver again by

```py
python thunder.py boot
```

visit `http://127.0.0.1:5000` which is your project landing page

visit `http://127.0.0.1:5000/todo_app` this will take you to your app landing page (todo_app)

visit `http://127.0.0.1:5000/todo_app` this will take you to admin page. From there you are ready to go. See more documentations and exmples <a href="https://sakyum.readthedocs.io">sakyum</a>

## Useful links

- Documentation: https://sakyum.readthedocs.io
- Repository: https://github.com/usmanmusa1920/sakyum
- PYPI Release: https://pypi.org/projects/sakyum
- Website: https://readthedocs.org/projects/sakyum

Pull requests are welcome
