# -*- coding: utf-8 -*-

"""
  =====================
  @ Flask-unity software
  =====================
       ____            _                     _____ ______
      /___ /    /|   /_  / /      /  / /|  /   /     /    |/
     /    /    /_|    / /_/      /  / / | /   /     /     /
    /    /___ /  | /_/ /  |     /__/ /  |/ __/__   /     /
  
  An extension of flask web framework that erase the complexity of structuring flask project blueprint, packages, and other annoying stuffs
"""


__title__ = "flask_unity"
__version__ = "0.0.3"
__author__ = "Usman Musa"
__author_email__ = "usmanmusa1920@gmail.com"
__author_website__ = "https://usmanmusa1920.github.io"
__repository__ = "https://github.com/usmanmusa1920/flask-unity"
__website__ = "https://flask-unity.readthedocs.io/en/latest/"
__copyright__ = "Copyright (C) 2022 - 2023 Usman Musa"


from .base import Boot
from .api import project
