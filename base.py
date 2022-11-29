
import os
import sys
import shlex
import logging
import argparse
import subprocess as sp

from pathlib import Path

from . import _js
from . import _css
from . import _html
from . import pro_default_dummy
from . import app_default_dummy

"""
  NOTSET    ---  0
  DEBUG     ---  10
  INFO      ---  20
  WARNING   ---  30  (default)
  ERROR     ---  40
  CRITICAL  ---  50
"""

formatter = "[+] [%(asctime)s] [%(levelname)s] %(message)s"
logging.basicConfig(format = formatter)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


ORIGIN = Path(__file__).resolve().parent.parent


class BaseStructure:
  """base structure class"""
  
  def __init__(self, flaskey_software=False):
    """base structure class initializer"""
    self.flaskey_software = flaskey_software
    
    
  def append_exs_to_file(self, fls_name):
    """append .py extension for files"""
    return [i+".py" for i in fls_name]
  
  
  def file_content(self, _exs, content=None, file_name="index", dir_togo=None):
    with open(f"{file_name}{_exs}", "w") as pay_fls:
      pay_fls.write(f"{content}")
    os.chdir(dir_togo)
    
    
  def file_opt(self, _dir, tree=True, _here=False, _where=False):
    """make tree dir and get into it"""
    if tree:
      sp.run(["mkdir", "-p", _dir])
    if _here:
      os.chdir(os.path.join(_here, _dir))
    if _where:
      os.chdir(_where)
      
      
  def into_file(self, fls, fls_cmd, file=None):
    """create files within current directory of '''self.file_opt()'''    """
    for _fls in fls:
      if _fls[:-3] == file:
        sp.run(shlex.split(f"{fls_cmd} {_fls}"))
        
        with open(_fls, "w") as pay_fls: # building the run module
          pay_fls.write(f"# Your project {_fls} file\n\n{pro_default_dummy}")
          
          
  def dir_tree(self, proj_name=None):
    """create a directory tree where file will reserved as well as modules too"""
    
    dirs = [proj_name, f"{proj_name}/{proj_name}", "templates", "static"]
    fls_name = ["__init__", "config", "models", "routes", "tunder"]
    fls = self.append_exs_to_file(fls_name)
    _here = os.getcwd() # initial `cwd` where the project was created
    fls_cmd = "touch"
    
    # check if the project already exist
    if os.path.exists(os.path.join(_here, proj_name)):
      print(f"\nProject ({proj_name}) already exist in this directory\n\t" + os.path.realpath(proj_name))
      logger.info(_here)
      print()
    else:
      # making directories trees and their default files in the loop
      for _dir in dirs:
        if _dir == dirs[0]:
          self.file_opt(_dir, _here=_here)
          self.into_file(fls, fls_cmd, file="tunder") # to maker tunder file
          project_folder = os.getcwd() # base dir of project
          _exs = [".html", ".css", ".js"]
          
          # static folders
          for static_dir in dirs[2:]:
            if static_dir == dirs[2:][0]:
              self.file_opt(static_dir, _here=project_folder) # templates
              self.file_content(_exs[0], content=_html, dir_togo=project_folder) # create index.html
              
            if static_dir == dirs[2:][1]:
              self.file_opt(static_dir, _here=project_folder) # static
              inn_static = os.getcwd() # base dir of static dir
              
              self.file_opt(_exs[1][1:], _here=inn_static) # css
              self.file_content(_exs[1], file_name="style", content=_css, dir_togo=inn_static) # create index.css
              
              self.file_opt(_exs[2][1:], _here=inn_static) # js
              self.file_content(_exs[2], content=_js, dir_togo=project_folder) # create index.js
          os.chdir(_here)
          
        if _dir == dirs[0] + "/" + dirs[0]:
          self.file_opt(_dir, _here=_here)
          # create default modules inside project sub dir
          for _fls in fls:
            if _fls[:-3] != "tunder":
              sp.run(shlex.split(f"{fls_cmd} {_fls}"))
              with open(_fls, "w") as pay_fls:
                pay_fls.write(f"# Hello world from {_fls}")
          os.chdir(_here)
      print()
      logger.info(f"Project ({proj_name}) created successfully!")
      print()
      
      
class AppStructure(BaseStructure):
  """base structure class"""
  app_store_name = None
  
  def into_file(self, fls, fls_cmd, file=None, app_default_dummy=app_default_dummy):
    """create files within current directory of '''self.file_opt()'''    """
    for _fls in fls:
      sp.run(shlex.split(f"{fls_cmd} {_fls}"))
      with open(_fls, "w") as pay_fls: # building the run module
        pay_fls.write(f"# Your app {_fls} file\n\n{app_default_dummy}")
        
        
  def app_static_and_template(self, _dir_=False, file=False, app=False, cmd=False, _here_=False):
    # _dir_ = False"template or static"
    # file = ["index.html"]
    # app = app name
    # cmd = "touch"
    # _here_ = # initial `inside project folder` where the project was created
    
    self.file_opt(_dir_, tree=False, _here=_here_) # back to template dir
    self.file_opt(f"{app}", _where=app) # make app dir inside `template`
    self.into_file(file, cmd, app_default_dummy=_html) # making app default file
    
    
  def dir_tree(self, proj_app_name=None):
    """create a directory tree where file will reserved as well as modules too"""
    
    dirs = [proj_app_name]
    app_store_name = proj_app_name # store our app name
    fls_name = ["__init__", "views", "models", "routes"]
    fls = self.append_exs_to_file(fls_name)
    roove_dir = ["templates", "static/css", "static/js"]
    _here_app = os.getcwd()  # initial `inside project folder` where the project was created
    fls_cmd = "touch"
    
    # check if the app already exist
    app_proj_name = _here_app.split("/")[-1]
    if os.path.exists(os.path.join(_here_app, proj_app_name)):
      print(f"\nApp ({proj_app_name}) already exist in this project ({app_proj_name})\n\t" + os.path.realpath(proj_app_name))
      logger.info(_here_app)
      print()
    else:
      # making directories trees and their default files
      for _dir in dirs:
        if _dir == dirs[0]:
          self.file_opt(_dir, _here=_here_app)
          self.into_file(fls, fls_cmd) # to maker app default files
          
      self.app_static_and_template(
        _dir_=roove_dir[0], file=["index.html"], app=proj_app_name, cmd=fls_cmd, _here_=_here_app
        )
      
      self.app_static_and_template(
        _dir_=roove_dir[1], file=["style.css"], app=proj_app_name, cmd=fls_cmd, _here_=_here_app
        )
      
      self.app_static_and_template(
        _dir_=roove_dir[2], file=["index.js"], app=proj_app_name, cmd=fls_cmd, _here_=_here_app
        )
      
      self.file_opt("do_nothing", tree=False, _where=_here_app) # back to project dir
      print()
      logger.info(f"App ({proj_app_name}) created successfully! in {app_proj_name}")
      print()
      
      
def create_app(app):
  """create project app"""
  AppStructure().dir_tree(app)
  
  
def boot(action="create_app"):
  """boot up project operation and app operation"""
  # prog is the name of the program, default=sys.argv[0]
  parser = argparse.ArgumentParser(prog="create_app", description="This create an app in your project")
  # metavar make the -help to look cleaan
  parser.add_argument("--app", "-a", required=True, type=str, metavar="", help="What is the app name")
  parser.add_argument(dest="create_app", default="create_app", type=str, metavar="", help="Put positional argument of `create_app` to create app, app are create inside your project")
  args = parser.parse_args()
  
  if action in sys.argv and sys.argv[1] == action:
    create_app(sys.argv[-1])
    print(args, sys.argv)
  else:
    print("Donn\'t create app", args, sys.argv)

