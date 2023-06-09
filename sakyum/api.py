# -*- coding: utf-8 -*-

import logging
from . import __title__
from .base import BaseStructure


formatter = '[+] [%(asctime)s] [%(levelname)s] %(message)s'
logging.basicConfig(format = formatter)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def project(name):
  """create project"""
  if name.lower() == __title__:
    print()
    logger.error(f'Not allowed to use ({__title__}) package name as project name\n')
    return False
  BaseStructure().dir_tree(name)
