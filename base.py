
import os
import shlex
import logging
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
    
    
  def file_opt(self, _dir, _here=False):
    """make tree dir and get into it"""
    sp.run(["mkdir", "-p", _dir])
    if _here:
      os.chdir(os.path.join(_here, _dir))
    
    
  def into_file(self, fls, fls_cmd, file=None):
    """
    create files within current directory of '''self.file_opt()'''
    """
    for _fls in fls:
      if _fls[:-3] == file:
        sp.run(shlex.split(f"{fls_cmd} {_fls}"))
        
        # building the run module
        with open(_fls, "w") as pay_fls:
          pay_fls.write(f"# Your project {_fls} file\n\n{pro_default_dummy}")
          
          
  def dir_tree(self, proj_name=None):
    """create a directory tree where file will reserved as well as modules too"""
    
    dirs = [proj_name, f"{proj_name}/{proj_name}", "templates", "static"]
    fls_name = ["__init__", "config", "models", "routes", "tunder"]
    fls = [i+".py" for i in fls_name]
    
    # getting the directory that user run the initial command
    # that make project default dirs trees and files
    _here = os.getcwd()
    fls_cmd = "touch"
    
    # check if the project already exist
    if os.path.exists(os.path.join(_here, proj_name)):
      print(f"\nProject ({proj_name}) already exist in this directory\n\t" + os.path.realpath(proj_name))
      logger.info(_here)
      print()
      
    else:
      # making directories trees and their default files
      for _dir in dirs:
        if _dir == dirs[0]:
          self.file_opt(_dir, _here)
          
          # to maker tunder file
          self.into_file(fls, fls_cmd, file="tunder")
          
          # base dir of project
          project_folder = os.getcwd()
          _exs = [".html", ".css", ".js"]
          
          # static folders
          for static_dir in dirs[2:]:
            
            # index.html
            if static_dir == dirs[2:][0]:
              self.file_opt(static_dir)
              os.chdir(os.path.join(project_folder, static_dir)) # templates
              
              with open(f"index{_exs[0]}", "w") as pay_fls:
                pay_fls.write(f"{_html}")
              os.chdir(project_folder)
              
            if static_dir == dirs[2:][1]:
              self.file_opt(static_dir)
              os.chdir(os.path.join(project_folder, static_dir)) # static
              
              inn_static = os.getcwd() # base dir of static dir
              self.file_opt(_exs[1][1:])
              os.chdir(os.path.join(inn_static, _exs[1][1:])) # css
              
              # index.css
              with open(f"index{_exs[1]}", "w") as pay_fls:
                pay_fls.write(f"{_css}")
                
              os.chdir(inn_static)
              self.file_opt(_exs[2][1:])
              os.chdir(os.path.join(inn_static, _exs[2][1:])) # js
              
              # index.js
              with open(f"index{_exs[2]}", "w") as pay_fls:
                pay_fls.write(f"{_js}")
              os.chdir(project_folder)
              
          os.chdir(_here)
          
        if _dir == dirs[0] + "/" + dirs[0]:
          self.file_opt(_dir, _here)
          
          for _fls in fls:
            if _fls[:-3] != "tunder":
              sp.run(shlex.split(f"{fls_cmd} {_fls}"))
              with open(_fls, "w") as pay_fls:
                pay_fls.write(f"# Hello world from {_fls}")
          os.chdir(_here)
      print()
      logger.info(f"Project ({proj_name}) created successfully!")
      print()

