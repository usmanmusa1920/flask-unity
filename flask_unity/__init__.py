# -*- coding: utf-8 -*-
"""
  ======================
  @ Flask-Unity software
  ======================
       ____            _                     _____ ______
      /___ /    /|   /_  / /      /  / /|  /   /     /    |/
     /    /    /_|    / /_/      /  / / | /   /     /     /
    /    /___ /  | /_/ /  |     /__/ /  |/ __/__   /     /
  
  An extension of flask web framework that erase the complexity of structuring flask project blueprint, packages, connecting other flask extensions, database migrations, and other annoying stuffs.
"""

from datetime import datetime


__title__ = 'flask_unity'
__version__ = '0.0.13'
__author__ = 'Usman Musa'
__author_email__ = 'usmanmusa1920@gmail.com'
__author_website__ = 'https://usmanmusa1920.github.io'
__repository__ = 'https://github.com/usmanmusa1920/flask-unity'
__url__ = 'https://flask-unity.readthedocs.io'
__license__ = 'MIT'
__copyright__ = f'Copyright (C) 2022 - {datetime.today().year} Usman Musa'
__description__ = 'An extension of flask web framework that erase the complexity of structuring flask project blueprint, packages, connecting other flask extensions, database migrations, and other annoying stuffs.'


from .base import Boot
