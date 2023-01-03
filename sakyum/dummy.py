
from . import __title__
from . import __version__
from . utils import stylePage


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
  <link rel="shortcut icon" href="{f} url_for('base.static', filename='/media/favicon.ico') {l}" type="image/x-icon">
  <link rel="stylesheet" type="text/css" href="{f} url_for('{static_url}.static', filename='style.css') {l}">
  <script type="text/javascript" src="{f} url_for('{static_url}.static', filename='index.js') {l}"></script>
  <script src="main.js"></script>
  <title>Sakyum - {name}</title>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="header_col">
        <div class="head_left">
          <h1 class="logo">
            <a href="#">Sakyum</a>
          </h1>
        </div>

        <div class="head_right">
          <a href="https://github.com/usmanmusa1920/sakyum" class="link_0" target="_blank">Github</a>
          <a class="link_1">|</a>
          <a href="#" class="link_2" target="_blank">Docs</a>
          <a href="#" class="link_3" target="_blank">Install</a>
          <a onclick="test()" class="alert">
            <img src="{f} url_for('base.static', filename='/media/alert.png') {l}" alt="">
          </a>
        </div>
      </div>
    </div>
    
    <div class="main">
      <div class="main_column">
        <div class="mini">
          <div class="mini_column">
            <p><pre>  ...........................
    _
  /_  /|   / / |/ /  / /\  /|
   / /_|  /_/  / /  / /  \/ |
/_/ /  | /  | / /__/ /      |
.............................</pre></p>
            <p>Your project ({name}) default page</p>
          </div>
        </div>

        <div class="three_col">
          <div>
            <p>An extension of flask web framework of python that erase the complexity of constructing flask project blueprint, packages, and other annoying stuffs</p>
          </div>
        </div>
      </div>
    </div>

    <div class="footer">
      <p><pre>============================
 @ {__title__} software - v{__version__}
============================</pre></p>
    </div>
  </div>
</body>
</html>
"""
  page_desc = stylePage(name, _is)
  return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="shortcut icon" href="{f} url_for('base.static', filename='/media/favicon.ico') {l}" type="image/x-icon">
  <link rel="stylesheet" type="text/css" href="{f} url_for('{static_url}.static', filename='style.css') {l}">
  <script type="text/javascript" src="{f} url_for('{static_url}.static', filename='index.js') {l}"></script>
  <script src="main.js"></script>
  <title>Sakyum - {name}</title>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="header_col">
        <div class="head_left">
          <h1 class="logo">
            <a href="#">Sakyum</a>
          </h1>
        </div>

        <div class="head_right">
          <a href="https://github.com/usmanmusa1920/sakyum" class="link_0" target="_blank">Github</a>
          <a class="link_1">|</a>
          <a href="#" class="link_2" target="_blank">Docs</a>
          <a href="#" class="link_3" target="_blank">Install</a>
          <a onclick="test()" class="alert">
            <img src="{f} url_for('base.static', filename='/media/alert.png') {l}" alt="">
          </a>
        </div>
      </div>
    </div>
    
    <div class="main">
      <div class="main_column">
        <div class="mini">
          <div class="mini_column">
            <p><pre>{page_desc[1]}
{page_desc[0]}
{page_desc[1]}</pre></p>
          </div>
        </div>

        <div class="three_col">
          <div>
            <p>An extension of flask web framework of python that erase the complexity of constructing flask project blueprint, packages, and other annoying stuffs</p>
          </div>
        </div>
      </div>
    </div>

    <div class="footer">
      <p><pre>============================
 @ {__title__} software - v{__version__}
============================</pre></p>
    </div>
  </div>
</body>
</html>
"""


def _css(f="{", l="}"):
  return f"""* {f}
  margin: 0;
  padding: 0;
  box-sizing: border-box;
{l}

html, body, div, span, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
abbr, address, cite, code,
del, dfn, em, img, ins, kbd, q, samp,
small, strong, sub, sup, var,
b, i,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section, summary,
time, mark, audio, video {f}
  outline:0;
  /* font-size:100%; */
  vertical-align:baseline;
  background:transparent;
{l}

body{f}
  background: lightgrey;
  overflow-x: hidden;
  overflow-y: auto;
  font-size: 15px;
  font-family: "Roboto","Lucida Grande","DejaVu Sans","Bitstream Vera Sans", Times 'Segoe UI', Tahoma, Verdana, sans-serif, serif,Verdana,Arial,sans-serif;
{l}

.container{f}
  width: 100%;
  overflow-x: hidden;
  overflow-y: auto;
{l}

.header{f}
  top: 0;
  width: 100%;
  height: 11.5vh;
  position: fixed;
  background: rgb(50, 50, 63);
  border-bottom: solid black 1px;
  display: flex;
  align-items: center;
  justify-content: center;
{l}

.header_col{f}
  width: 90%;
  padding: 20px 70px;
  display: flex;
  align-items: center;
  justify-content: space-between;
{l}

@media only screen and (max-width: 700px){f}
  .header_col{f}
    padding: 18px 5px;
  {l}
{l}

.head_left{f}
  width: 45%;
  height: 100%;
{l}

@media only screen and (max-width: 700px){f}
  .logo{f}
    font-size: 20px;
  {l}
{l}

.logo a{f}
  color: white;
  text-decoration: none;
  width: fit-content;
{l}

.head_right{f}
  width: 50%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: flex-end;
{l}

.head_right a{f}
  color: white;
  margin-left: 15px;
  font-size: 18px;
  text-decoration: none;
{l}

.head_right a:hover{f}
  text-decoration: underline solid 3px;
{l}

@media only screen and (max-width: 700px){f}
  .link_0, .link_1, .link_2, .link_3{f}
    display: none;
  {l}
{l}

.head_right a img{f}
  width: 40px;
  height: 40px;
  margin-left: 15px;
{l}

.alert{f}
  display: block;
  position: relative;
{l}

.main{f}
  width: 100%;
  display: flex;
  justify-content: center;
  margin-top: 12vh;
{l}

.main_column{f}
  width: 90%;
  padding: 10px 70px;
{l}

@media only screen and (max-width: 700px){f}
  .main_column{f}
    width: 100%;
    padding: 0;
  {l}
{l}

.mini{f}
  width: 100%;
  min-height: 50vh;
  display: flex;
  justify-content: center;
  align-items: center;
{l}

.mini_column{f}
  width: 80%;
  max-width: 1024px;
  height: 45vh;
  border-radius: 7px;
  padding: 50px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
{l}

@media only screen and (max-width: 700px){f}
  .mini_column{f}
    max-width: 100%;
    width: 90%;
    height: 60vh;
    padding: 0;
  {l}
{l}

.mini_column h1{f}
  font-size: 2.5rem;
  font-weight: lighter;
  margin-top: 15px;
  text-align: center;
{l}

.mini_column p{f}
  max-width: 80%;
  text-align: center;
  font-weight: lighter;
  font-size: 1rem;
{l}

.three_col{f}
  margin: 20px 0;
  width: 100%;
  display: flex;
  justify-content: space-evenly;
{l}

@media only screen and (max-width: 700px){f}
  .three_col{f}
    margin: 10px 0;
    flex-direction: column;
    align-items: space-evenly;
  {l}
{l}

.three_col div{f}
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 100%;
  min-width: 50%;
{l}

.three_col div p{f}
  max-width: 80%;
  font-size: 1.1rem;
  line-height: 35px;
  text-align: center;
{l}

@media only screen and (max-width: 700px){f}
  .three_col div p{f}
    max-width: 90%;
    font-size: 1rem;
    line-height: 25px;
    margin-top: 5px;
  {l}
{l}

.footer{f}
  margin: 20px 0;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-top: solid black 1px;
{l}

@media only screen and (max-width: 700px){f}
  .footer{f}
    margin: 10px 0;
    flex-direction: column;
    align-items: center;
    align-items: center;
  {l}
{l}

.footer p{f}
  max-width: 80%;
  font-size: 1.1rem;
  line-height: 35px;
  text-align: center;
{l}

@media only screen and (max-width: 700px){f}
  .footer p{f}
    max-width: 90%;
    font-size: 1rem;
    line-height: 25px;
    margin-top: 5px;
  {l}
{l}
"""


def _js(name, f="{", l="}"):
  return f"""function test(){f}
  alert('I am sakyum test alert for ({name})')
{l}
"""


null = r"""# write awesome code here!
"""


def thunder_dummy(project):
  return f"""from sakyum import Boot
  
boot = Boot()

if __name__ == "__main__":
  boot.run()

from {project} import app
from {project}.routes import base
# from <app_name>.views import <app_name>

app.register_blueprint(base)
# app.register_blueprint(<app_name>)

app.run(debug=boot.d, port=boot.p, host=boot.h)
"""


pro_init_dummy = r"""from flask import Flask
app = Flask(__name__)
"""


def pro_routes_dummy(proj):
  return f"""from {proj} import app
from flask import (render_template, Blueprint)
from sakyum.utils import template_dir, static_dir

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
from sakyum.utils import template_dir, static_dir

{app} = Blueprint("{app}", __name__, template_folder=template_dir(), static_folder=static_dir("{app}"))

# @{app}.route('/')
# def index():
#   return "<h1>{app} index page</h1>"

@{app}.route('/{app}')
def index():
  return render_template("{app}/index.html")
"""
