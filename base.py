
import os
import shlex
import logging
import subprocess as sp

from pathlib import Path

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


class Filing:
  """filiing class"""
  
  def __init__(self, autoOpenMap=False):
    """Filing class initializer"""
    self.autoOpenMap = autoOpenMap
    
    
  def file_opt(self, _dir, _here):
    """make tree dir and get into it"""
    sp.run(["mkdir", "-p", _dir])
    os.chdir(os.path.join(_here, _dir))
    
    
  def into_file(self, fls, fls_cmd, file=None, proj_name=None):
    """
    create files within current directory of '''self.file_opt()'''
    """
    for _fls in fls:
      if _fls[:-3] == file:
        sp.run(shlex.split(f"{fls_cmd} {_fls}"))
        pro_default_dummy = r"""from flaskblog import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

"""
        app_default_dummy = r"""from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
  return "Hello world"
  
  
if __name__ == '__main__':
  app.run(debug=True)
"""
        with open(_fls, "w") as pay_fls:
          pay_fls.write(f"# Your project {_fls} file\n\n{pro_default_dummy}")
          
          
  def dir_tree(self, proj_name=None):
    """create a directory tree where file will reserved"""
    
    flskey = "flaskey"
    # flskey = proj_name
    dirs = [flskey, f"{flskey}/{flskey}"]
    fls_name = ["__init__", "config", "models", "routes", "tunder"]
    
    # appending `.py` extension to each fls_name item
    fls = [i+".py" for i in fls_name]
    logger.info(os.getcwd())
    
    # getting the directory that user run the first command
    # that make default dir trees and files
    _here = os.getcwd()
    fls_cmd = "touch"
    if os.path.exists(os.path.join(_here, 'flaskey')):
      print('\n  Project already exist in this directory\n\t' + os.path.realpath('flaskey') + '\n')
    
    # making directories trees and their default files
    for _dir in dirs:
      if _dir == dirs[0]:
        self.file_opt(_dir, _here)
        
        # to maker tunder file
        self.into_file(fls, fls_cmd, file="tunder")
        print(os.getcwd())
        os.chdir(_here)
        print(os.getcwd())
        
      if _dir == dirs[0] + "/" + dirs[0]:
        self.file_opt(_dir, _here)
        
        for _fls in fls:
          if _fls[:-3] != "tunder":
            sp.run(shlex.split(f"{fls_cmd} {_fls}"))
            with open(_fls, "w") as pay_fls:
              pay_fls.write(f"# Hello world from {_fls}")
        print(os.getcwd())
        os.chdir(_here)
        print(os.getcwd())

