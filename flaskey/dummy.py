
from . import __title__
from . import __version__


def _html(name, static_url=None, is_what=True, f="{{", l="}}"):
  if is_what:
    _is = "application"
    static_url = name
  else:
    _is = "project"
    static_url = "base"
  return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" type="text/css" href="{f} url_for('{static_url}.static', filename='style.css') {l}">
  <script type="text/javascript" src="{f} url_for('{static_url}.static', filename='index.js') {l}"></script>
  <title>{name} - index page</title>
</head>
<body>
  <!-- write awesome code here! -->
  
  <h1>Welcome to flaskey {name} ({_is})</h1>
  <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Numquam quidem in iure architecto, iste eius aperiam, ipsam ducimus commodi soluta ea earum quis eveniet illum fugiat voluptatibus voluptatem aspernatur tenetur?</p>
  <br>
  <p>
    <a href="https://github.com/usmanmusa1920/flaskey" target="_blank">@{__title__} - v{__version__}</a>
  </p>
</body>
</html>
"""


def _css(f="{", l="}"):
  return f"""body {f}
  padding: 0;
  margin: 0;
  height: 100vh;
  width: 100vw;
  background: dodgerblue;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
{l}

p{f}
  text-align: center;
{l}
"""


def _js(name):
  return f"""alert('Welcome alert for {name} page')
"""


null = r"""# write awesome code here!
"""


def thunder_dummy(project):
  return f"""import sys
import argparse
from flaskey import boot

if sys.argv[1] == "boot":
  parser = argparse.ArgumentParser(prog="boot up server", description="This boot up the server")
  parser.add_argument("--port", "-p", default=5000, required=False, type=int, metavar="", help="What is the port number?")
  parser.add_argument(dest="boot", default="boot", type=str, metavar="", help="Put positional argument of `boot` to bring server up running")
  _port_ = parser.parse_args()

if __name__ == "__main__":
  boot()

from {project} import app
from {project}.routes import base
# from <app_name>.views import <app_name>

app.register_blueprint(base)
# app.register_blueprint(<app_name>)

app.run(debug=True, port=_port_.port)
"""


pro_init_dummy = r"""from flask import Flask
app = Flask(__name__)
"""


def pro_routes_dummy(proj):
  return f"""from {proj} import app
from flask import (render_template, Blueprint)
from flaskey.utils import template_dir, static_dir

base = Blueprint("base", __name__, template_folder=template_dir(), static_folder=static_dir("{proj}"))

# @base.route('/')
# def index():
#   return "<h1>base index page</h1>"

@base.route('/')
def index():
  return render_template("index.html")
"""


def app_views_dummy(yourapplication, app):
  return f"""from {yourapplication} import app
from flask import (render_template, Blueprint)
from flaskey.utils import template_dir, static_dir

{app} = Blueprint("{app}", __name__, template_folder=template_dir(), static_folder=static_dir("{app}"))

# @{app}.route('/')
# def index():
#   return "<h1>{app} index page</h1>"

@{app}.route('/{app}')
def index():
  return render_template("{app}/index.html")
"""
