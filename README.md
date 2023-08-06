
# Flask-unity

An extension of flask web framework that erase the complexity of structuring flask project blueprint, packages, and other annoying stuffs.

       ____            _                     _____ ______
      /___ /    /|   /_  / /      /  / /|  /   /     /    |/
     /    /    /_|    / /_/      /  / / | /   /     /     /
    /    /___ /  | /_/ /  |     /__/ /  |/ __/__   /     /

## Installation

First create a virtual environment `python3 -m venv venv` and then activate it `source venv/bin/activate`

Once that finish now install the library by

```py
pip install flask_unity
```

wait for the installation basically the library was uploaded using `sdist` (Source Distribution) and this software (library) might not be compatible with `windows operating system` but it works on other `OS` such as `linux` and `macOS`

## Create your first flask project using flask_unity

After the installation paste the following command on your termianl

```py
python3 -c "from flask_unity import project; project('todo_project')"
```

or create a file and paste the below codes which is equivalent of the above, and then run the file

```python
from flask_unity import project

project("todo_project")
```

the command you type on terminal or the code you paste in a file (after running the file) will create a project called `todo_project` now cd into the `todo_project` directory, if you do `ls` you will see a module called `thunder.py`, `static`, `templates` and a directory with the same name of your base directory name, in our case it is `todo_project`.

You can boot up the flask server, after you cd into the project folder (todo_project), and run the below command:

```py
python3 thunder.py boot
```

Now visit the local url `127.0.0.1:5000` this will show you index page of your project. And if you do `ls` in that same dir you will see it create a `default.db` file (an sqlite file)

## Create flask project app using flask_unity

For you to start an app within your project (`todo_project`) run the following command, in that working directory (todo_project) by giving the name you want your app to be, in our case we will call our app `todo_app`

```py
python3 thunder.py create_app -a todo_app
```

or

```py
python3 thunder.py create_app --app todo_app
```

this will create an app within your project (`todo_project`), the `-a` flag is equivalent to `--app` for the app name in this example it is called `todo_app`

## Register an app

Once the app is created open a file called `routes.py` in the folder with the same name of your project in our case it is called `todo_project`, (`todo_project/routes.py`) file of your project and import your app blueprint which is in your app `views.py` file (above `reg_blueprints` list) in the `routes.py` file

```py
from todo_app.views import todo_app
```

after that, append it in the list `reg_blueprints` provided in the `routes.py` file by

```py
reg_blueprints = [base, errors, todo_app]
```

once you register the app, boot up the flask webserver by

```py
python3 thunder.py boot
```

This will bring the flask development server on port `5000` you can give it a different port by including a `-p` or `--port` flag which is for port number:

```py
python3 thunder.py boot -p 7000
```

or

```py
python3 thunder.py boot --port 7000
```

this will bring the serve on port `7000` visit the localhost url with the port number, it will show you your project `index.html page` (todo_project). To get to your app default page (todo_app), visit the url with your app name in our case:

`http://127.0.0.1:7000/todo_app`

this will take you to your app `index.html page` (todo_app). From there you are ready to go.

Also, you can give your desire ip address/host by using `-H` or `--host` flag, e.g

```py
python3 thunder.py boot -p 7000 -H 0.0.0.0
```
or

```py
python3 thunder.py boot --port 7000 --host 0.0.0.0
```

For development server, you can give a debug value to True by specifying `-d` flag or `--debug` e.g

```py
python3 thunder.py boot -p 7000 -d True
```
or

```py
python3 thunder.py boot --port 7000 --debug True
```

## Register model to admin page

To register your model in the admin page, open your sub project folder and open the `config.py` file you see there. Import your app model that you want to register, above the method that will create the tables and database `db.create_all()` and you will see a commented prototype above it, then append it in the `reg_models = []` list within `admin_runner` function. That will register your model in the admin page and you will see it if you vist the admin page

## Admin user

You can create an admin user of your application user model, by running the following command

```py
python3 thunder.py create_user
```

once you run it, a prompt will come up to input your information

## Github repository:

- https://github.com/usmanmusa1920/flask-unity

Pull requests are welcome
