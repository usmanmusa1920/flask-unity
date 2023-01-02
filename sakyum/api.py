
import logging
from . import __title__
from . base import BaseStructure


formatter = "[+] [%(asctime)s] [%(levelname)s] %(message)s"
logging.basicConfig(format = formatter)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def project(name):
  """create project"""
  if name.lower() == __title__:
    logger.error("Not allowed to use that name as project name")
    return False
  BaseStructure().dir_tree(name)
  
def delete_app():
  """delete app"""
  pass
