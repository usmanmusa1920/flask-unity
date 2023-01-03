
import os

def static_dir(app):
  """relative path to static files"""
  return os.getcwd() + "/static/" + app

def template_dir():
  """relative path to html page"""
  return os.getcwd() + "/templates"

def readIMG(p):
  """read default alert image, for sure static file work"""
  with open(p, "rb") as i:
    r = i.read()
  return r

def stylePage(name, _is):
  """function for styling project application description default page"""
  desc = "Your " + name + " " + _is + " default pages"
  desc_center = desc.center(len(desc) + 6)
  border = "=" * len(desc_center)
  return [desc_center, border]