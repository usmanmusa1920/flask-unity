# -*- coding: utf-8 -*-

from . import f1
from . import l1
from . import f2
from . import l2
from . import __title__
from . import stylePage


def _html(name, is_landing=False, is_admin=False, project_name=False, is_base_app=False):
  if is_landing:
    return f"""{f1}% extends 'default_base.html' %{l1}

{f1}% block head_js %{l1}
  <script src="{f2} url_for('base.static', filename='index.js') {l2}"></script>
{f1}% endblock head_js %{l1}
"""
  if is_admin:
    return f"""{f1}% extends 'admin/master.html' %{l1}
{f1}% block body %{l1}
  <a href="/">Go to {project_name} home page</a>
  <br>
  {f1}% if current_user.is_authenticated %{l1}
    <a href="{f2} url_for('auth.adminLogout') {l2}">logout</a>
    <br>
    <a href="{f2} url_for('auth.adminRegister') {l2}">register</a>
    <br>
    <a href="{f2} url_for('auth.changeProfileImage') {l2}">change image</a>
    <br>
    <a href="{f2} url_for('auth.adminChangePassword') {l2}">change password</a>
  {f1}% else %{l1}
    <a href="{f2} url_for('auth.adminLogin') {l2}">login</a>
  {f1}% endif %{l1}
{f1}% endblock body %{l1}
"""
  if is_base_app:
    page_desc = stylePage(name)
    return f"""{f1}% extends '{project_name}/index.html' %{l1}

{f1}% block head_css %{l1}
  <!-- <link rel="stylesheet" type="text/css" href="{f2} url_for('{name}.static', filename='style.css') {l2}"> -->
{f1}% endblock head_css %{l1}

{f1}% block head_js %{l1}
  <script src="{f2} url_for('{name}.static', filename='index.js') {l2}"></script>
{f1}% endblock head_js %{l1}


{f1}% block short_info %{l1}
  {f1}% if current_user.is_authenticated %{l1}
      <p>Hi {f2} current_user.username {l2}! from your ({name}) project app</p>
    {f1}% else %{l1}
      <p>Your ({name}) app says, please login</p>
    {f1}% endif %{l1}
{f1}% endblock short_info %{l1}


{f1}% block main %{l1}
  <h3><pre>({name}) app
{page_desc[1]}
{page_desc[0]}
{page_desc[1]}</pre></h3>
{f1}% endblock main %{l1}
"""


def _css():
  return f"""
* {f1}
  margin: 0;
  padding: 0;
  box-sizing: border-box;
{l1}

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
time, mark, audio, video {f1}
  outline:0;
  /* font-size:100%; */
  vertical-align:baseline;
  background:transparent;
{l1}

body {f1}
  overflow-x: hidden;
  overflow-y: auto;
  font-size: 15px;
  font-family: "Roboto","Lucida Grande","DejaVu Sans","Bitstream Vera Sans", Times 'Segoe UI', Tahoma, Verdana, sans-serif, serif,Verdana,Arial,sans-serif;
{l1}
"""


def _js(name):
  return f"""function test(){f1}
  alert('I am {__title__} test alert for ({name}) index page')
{l1}
"""
