
import os

def static_dir(app):
  """relative path to static files"""
  return os.getcwd() + "/static/" + app

def template_dir():
  """relative path to html page"""
  return os.getcwd() + "/templates"
