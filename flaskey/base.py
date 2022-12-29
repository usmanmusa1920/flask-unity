
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

from . import null
from . import thunder_dummy

from . import pro_init_dummy
from . import pro_routes_dummy
from . import app_views_dummy

from . import __title__
from . import __version__

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

  def __init__(self, is_software=True):
    """base structure class initializer"""
    self.is_software = is_software
    self.fls_cmd = "touch"
    self._exs_first = ["index", "style"]
    self._exs_last = [".html", ".css", ".js"]
    

  def append_exs_to_file(self, fls_name=False, _exs_=".py", name=None):
    """append .py extension for files if _exs_ value is ".py" or type is str, else if _exs_ type is list, make list of static files `['index.html', 'index.js', 'style.css']` """

    if type(_exs_) == list:
      name, exst = self._exs_first, self._exs_last
      lst = []
      
      for i in exst:
        if i == exst[1]: # css
          idx = name[1]
          lst.append(f"{idx}{i}")
        if i == exst[0] or i == exst[2]: # html & js
          for j in exst:
            if j != exst[1]:
              idx = name[0]
              if f"{idx}{j}" in lst:
                pass
              else:
                lst.append(f"{idx}{j}")
      return lst
    if type(_exs_) == str:
      return [i+f"{_exs_}" for i in fls_name]
      

  def file_content(self, _exs=False, content=None, file_name="index", dir_togo=None, route_go=True):
    """insert content in a file"""
    if _exs:
      with open(f"{file_name}{_exs}", "w") as pay_fls:
        pay_fls.write(f"{content}")
    else:
      with open(f"{file_name}", "w") as pay_fls:
        pay_fls.write(f"{content}")
    if route_go:
      os.chdir(dir_togo)
      

  def file_opt(self, _dir, tree=True, _here=False, _where=False):
    """make tree dir and get into it"""
    if tree:
      sp.run(["mkdir", "-p", _dir])
    if _here:
      os.chdir(os.path.join(_here, _dir))
    if _where:
      os.chdir(_where)
      

  def into_file(self, fls, fls_cmd, file=None, app_default_dummy=null, is_static_file=False, is_app=False, proj_nm=None):
    """create files within current directory of '''self.file_opt()'''
    is_app: if it is True, that mean it will do operation of making app files,
    else it will make for the entire project
    """
    
    if is_app:
      for _fls in fls:
        app_name = os.getcwd().split('/')[-1]
        sp.run(shlex.split(f"{fls_cmd} {_fls}"))
        if is_static_file:
          self.file_content(file_name=_fls, content=f"{app_default_dummy}", route_go=False) # building app default files
        else:
          if _fls == "__init__.py":
            self.file_content(file_name=_fls, content=f"# from {__title__} software, your app ({app_name}) {_fls} file\n\n{null}", route_go=False) # building app `__init__.py` default files
          elif _fls == "forms.py":
            self.file_content(file_name=_fls, content=f"# from {__title__} software, your app ({app_name}) {_fls} file\n\n{null}", route_go=False) # building app `forms.py` default files
          elif _fls == "models.py":
            self.file_content(file_name=_fls, content=f"# from {__title__} software, your app ({app_name}) {_fls} file\n\n{null}", route_go=False) # building app `models.py` default files
          elif _fls == "routes.py":
            self.file_content(file_name=_fls, content=f"# from {__title__} software, your app ({app_name}) {_fls} file\n\n{null}", route_go=False) # building app `routes.py` default files
          elif _fls == "views.py":
            self.file_content(file_name=_fls, content=f"# from {__title__} software, your app ({app_name}) {_fls} file\n\n{app_views_dummy(self.proj_store_name, app_name)}", route_go=False) # building app `views.py` default files
    else:
      for _fls in fls:
        if _fls[:-3] == file:
          sp.run(shlex.split(f"{fls_cmd} {_fls}"))
          self.file_content(
            file_name=_fls,content=f"# Your project {_fls} file\n\n{thunder_dummy(proj_nm)}", route_go=False
            ) # building the run module
            

  def dir_tree(self, proj_name=None):
    """create a directory tree where file will reserved as well as modules too"""
    dirs = [proj_name, f"{proj_name}/{proj_name}", "templates", "static"]
    
    # default files of project sub folder, except `thunder` which is for project base dir
    fls_name = ["__init__", "config", "models", "routes", "thunder"]
    fls = self.append_exs_to_file(fls_name=fls_name) # appending extensions to files
    _here = os.getcwd() # initial `cwd` where the project was e.g `Desktop`
    
    # check if the project already exist
    if os.path.exists(os.path.join(_here, proj_name)):
      print(f"\nProject ({proj_name}) already exist in this directory\n\t" + os.path.realpath(proj_name))
      logger.info(_here)
      print()
    else:
      # making directories trees and their default files in the loop
      for _dir in dirs:
        if _dir == dirs[0] + "/" + dirs[0]:
          self.file_opt(_dir, _here=_here)
          # create default modules inside project sub dir
          for _fls in fls:
            if _fls[:-3] != "thunder":
              sp.run(shlex.split(f"{self.fls_cmd} {_fls}"))
              if _fls == "__init__.py":
                self.file_content(file_name=_fls, content=f"# from {__title__} software, your ({proj_name}) project {_fls} file\n\n{pro_init_dummy}", route_go=False) # building project `__init__.py` default files
              elif _fls == "config.py":
                self.file_content(file_name=_fls, content=f"# from {__title__} software, your ({proj_name}) project {_fls} file\n\n{null}", route_go=False) # building project `config.py` default files
              elif _fls == "models.py":
                self.file_content(file_name=_fls, content=f"# from {__title__} software, your ({proj_name}) project {_fls} file\n\n{null}", route_go=False) # building project `models.py` default files
              elif _fls == "routes.py":
                self.file_content(file_name=_fls, content=f"# from {__title__} software, your ({proj_name}) project {_fls} file\n\n{pro_routes_dummy(proj_name)}", route_go=False) # building project `routes.py` default files
          os.chdir(_here)
          
        if _dir == dirs[0]:
          self.file_opt(_dir, _here=_here)
          self.into_file(fls, self.fls_cmd, file="thunder", proj_nm=proj_name) # to maker thunder file
          project_folder = os.getcwd() # base dir path of 
          
          for static_dir in dirs[2:]: # templates & static
            if static_dir == dirs[2:][0]: # templates
              self.file_opt(static_dir, _here=project_folder) # make templates dir and cd into
              # create index.html and bact to project base dir path
              self.file_content(self._exs_last[0], content=f"<!-- @{__title__}, {proj_name} index.html page -->\n\n"+_html(proj_name, is_what=False), dir_togo=project_folder)
              
            if static_dir == dirs[2:][1]: # static
              self.file_opt(static_dir, _here=project_folder) # make static dir and cd into
              
              # make project static dir and cd into, NB: `os.getcwd()` is base dir of static dir
              self.file_opt(proj_name, _where=os.getcwd()+"/"+proj_name)
              self.file_content(self._exs_last[1], file_name="style", content=_css(), route_go=False) # create index.css
              
              self.file_content(self._exs_last[2], content=_js(proj_name), dir_togo=project_folder) # create index.js and bact to project base dir path
          os.chdir(_here)
      print()
      logger.info(f"Project ({proj_name}) created successfully!")
      print()
      

class AppStructure(BaseStructure):
  """base structure class"""
  app_store_name = None # app name
  proj_store_name = None # project name
  
  def app_static_and_template(self, file_dummy, top_comment=False, _dir_=False, file=False, app=False, cmd=False, _here_=False):
    # _dir_ = "template or static"
    # file = ["index.html"]
    # app = app name
    # cmd = "touch"
    # _here_ = # initial `inside project folder` where the project was created
    
    if top_comment == "html":
      top_comment = f"<!-- @{__title__}, {app} {file[0]} page -->\n\n"
    if top_comment == "css":
      top_comment = f"/* @{__title__}, {app} {file[0]} file */\n\n"
    if top_comment == "js":
      top_comment = f"// @{__title__}, {app} {file[0]} file\n\n"
      
    self.file_opt(_dir_, tree=False, _here=_here_) # back to template dir
    self.file_opt(f"{app}", _where=app) # make app dir inside `template`
    self.into_file(file, cmd, is_static_file=True, app_default_dummy=f"{top_comment}{file_dummy}", is_app=True) # making app default file
    

  def dir_tree(self, proj_app_name=None):
    """create a directory tree where file will reserved as well as modules too"""
    
    dirs = [proj_app_name]
    app_store_name = proj_app_name # store our app name
    fls_name = ["__init__", "views", "models", "routes", "forms"]
    fls = self.append_exs_to_file(fls_name=fls_name)
    roove_dir = ["templates", "static", "static"]
    _here_app = os.getcwd()  # initial `inside project folder` where the project was created
    
    # check if the app already exist
    app_proj_name = _here_app.split("/")[-1]
    self.proj_store_name = app_proj_name

    if os.path.exists(os.path.join(_here_app, proj_app_name)):
      print(f"\nApp ({proj_app_name}) already exist in this project ({app_proj_name})\n\t" + os.path.realpath(proj_app_name))
      logger.info(_here_app)
      print()
    else:
      # making directories trees and their default files
      for _dir in dirs:
        if _dir == dirs[0]:
          self.file_opt(_dir, _here=_here_app)
          self.into_file(fls, self.fls_cmd, is_app=True) # to maker app default files
          
      self.app_static_and_template(
        _html(app_store_name), top_comment="html", _dir_=roove_dir[0], file=[self.append_exs_to_file(_exs_=[])[0]], app=proj_app_name, cmd=self.fls_cmd, _here_=_here_app
        )
      self.app_static_and_template(
        _css(), top_comment="css", _dir_=roove_dir[1], file=[self.append_exs_to_file(_exs_=[])[2]], app=proj_app_name, cmd=self.fls_cmd, _here_=_here_app
        )
      self.app_static_and_template(
        _js(proj_app_name), top_comment="js", _dir_=roove_dir[2], file=[self.append_exs_to_file(_exs_=[])[1]], app=proj_app_name, cmd=self.fls_cmd, _here_=_here_app
        )
      self.file_opt("do_nothing", tree=False, _where=_here_app) # back to project dir
      print()
      logger.info(f"App ({proj_app_name}) created successfully! in {app_proj_name}")
      print()
      

def app_init(app):
  """initialize app in project"""
  AppStructure().dir_tree(app)
  exit()
  

def boot():
  """boot up project operation, app operation, and the server"""
  
  if len(sys.argv) == 1:
    print()
    logger.error(f"\n  please run the module with flag and positional argument\n")
    exit()
  if sys.argv[1] == "create_app":
    # prog is the name of the program, default=sys.argv[0]
    parser = argparse.ArgumentParser(prog="create_app", description="This create an app in your project")
    # metavar make the -help to look cleaan
    parser.add_argument("--app", "-a", required=True, type=str, metavar="", help="What is the app name")
    parser.add_argument(dest="create_app", default="create_app", type=str, metavar="", help="Put positional argument of `create_app` to create app, app are create inside your project")
    args = parser.parse_args()
    
    app_init(args.app)
  elif sys.argv[1] == "boot":
    # prog is the name of the program, default=sys.argv[0]
    parser = argparse.ArgumentParser(prog="boot up server", description="This boot up the server")
    # metavar make the -help to look cleaan
    parser.add_argument("--port", "-p", default=5000, required=False, type=int, metavar="", help="What is the port number?")
    parser.add_argument(dest="boot", default="boot", type=str, metavar="", help="Put positional argument of `boot` to bring server up running")
    args = parser.parse_args()
    
    logger.info(f"@{__title__} v{__version__} | visit: http://localhost:{args.port} (for development)")
  else:
    print()
    logger.error(f"\n  use a valid flag and positional argument\n")
    exit()
