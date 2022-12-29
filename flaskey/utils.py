
import os

def static_dir(app):
  return os.getcwd() + "/static/css/" + app

def template_dir():
  return os.getcwd() + "/templates"