# -*- coding: utf-8 -*-

from flask_unity import __title__
from flask_unity.utils import stylePage


f1 = "{"
l1 = "}"
f2 = "{{"
l2 = "}}"


def _html(name, admin=False, project_name=False, is_base=True, f1=f1, l1=l1, f2=f2, l2=l2):
  if admin:
    return f"""{f1}% extends 'admin/master.html' %{l1}
{f1}% block body %{l1}
  <a href="/">Go to {project_name} home page</a>
{f1}% endblock body %{l1}
"""
  if is_base:
    _is = "application"
    static_url = name
  else:
    _is = "project"
    static_url = "base"
    return f"""{f1}% extends "default_index.html" %{l1}

{f1}% block short_info %{l1}
  <p>Your project ({name}) default page</p>
{f1}% endblock short_info %{l1}

{f1}% block main %{l1}
  {f1}% if blueprints_list|length > 1 %{l1}
    <div class="blueprint_list_wrapper">
      <div class="blueprint_list">
        <p>Routes</p>
        {f1}% for blueprint in blueprints_list %{l1}
          <a href="/{{blueprint.name}}">{{blueprint.name}}</a>
          </br>
        {f1}% endfor %{l1}
        <a href="/admin/login">login</a>
        </br>
      </div>
    </div>
  {f1}% endif %{l1}

  <div class="pkg_desc">
    <div>
      <p>An extension of flask web framework of python that erase the complexity of constructing flask project blueprint, packages, and other annoying stuffs</p>
    </div>
  </div>
{f1}% endblock main %{l1}
"""
  page_desc = stylePage(name, _is)
  return f"""{f1}% extends "{project_name}/index.html" %{l1}

{f1}% block head_css %{l1}
  <!-- <link rel="stylesheet" type="text/css" href="{f2} url_for('{name}.static', filename='style.css') {l2}"> -->
{f1}% endblock head_css %{l1}

{f1}% block head_title %{l1}
  <title>Flask-unity - {f2}head_title{l2}</title>
{f1}% endblock head_title %{l1}

{f1}% block main %{l1}
  <h3><pre>({name}) app
{page_desc[1]}
{page_desc[0]}
{page_desc[1]}</pre></h3>
{f1}% endblock main %{l1}
"""


def _css(f1=f1, l1=l1):
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


def _js(name, f1=f1, l1=l1):
  return f"""function test(){f1}
  alert('I am {__title__} test alert for ({name}) index page')
{l1}
"""
