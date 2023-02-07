
        _
      /_  /|   /   |/ /  / /\  /|
       / /_|  /_/  / /  / /  \/ |
    /_/ /  | /  | / /__/ /      |

An extension of flask web framework of python that erase the complexity of constructing flask project blueprint, packages, and other annoying stuffs

# Installation
First create a virtual environment `python3 -m venv venv` and then activate it `source venv/bin/activate`

Once that finish now install the library by

`pip install sakyum`

wait for the installation basically the library was uploaded using `sdist` (Source Distribution)

## Create your first flask project using sakyum
After the installation paste the following command on your termianl

`python3 -c "from sakyum import project; project('todo_project')"`

or create a file and paste the below codes which is equivalent of the above, and then run the file

```python
from sakyum import project

project("todo_project")
```

the command you type on terminal or the code you paste in a file will create a project called `todo_project` now cd into the `todo_project` directory.

## Create flask project app
For you to start an app within your project (`todo_project`), run the following command by giving the name you want your app to be, in our case we will call our app `todo_app`

`python3 thunder.py create_app -a todo_app`

this will create an app within your project (`todo_project`), the `-a` flag is for the app name in this example it is called `todo_app`

## Run flask server
once the app is created open the `thunder.py` file of your project and import your app `views.py` file

`from todo_app.views import todo_app`

after that, register it to the blueprint template by

`app.register_blueprint(todo_app)`

once you register the app, boot up the flask webser by

`python thunder.py boot`

This will bring the flask development server on port `5000` you can give it a different port by including a `-p` flag which is for port number:

`python thunder.py boot -p 7000`

this will bring the serve on port `7000` visit the localhost url with the port number, it will show you your project `index.html page` (todo_project). To get to your app default page (todo_app), visit the url with your app name in our case:

`http://127.0.0.1:7000/todo_app`

this will take you to your app `index.html page` (todo_app). From there you are ready to go.

Also, you can give your desire ip address/host by using `-H` or `--host` flag, e.g

`python thunder.py boot -p 7000 -H 0.0.0.0` or `python thunder.py boot -p 7000 --host 0.0.0.0`

For development server, you can give a debug value to True by specifying `-d` flag or `--debug` e.g

`python thunder.py boot -p 7000 -d True` or `python thunder.py boot -p 7000 --debug True`

# Recommendation
This software will not be compatible with `windows operating system` use other `OS` such as `linux` or `macOS`

## Github repository:

- https://github.com/usmanmusa1920/sakyum

Pull requests are welcome
