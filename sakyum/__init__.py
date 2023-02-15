# -*- coding: utf-8 -*-

"""
  =====================
  @ sakyum software
  =====================
      _
    /_  /|   / / |/ /  / /\  /|
     / /_|  /_/  / /  / /  \/ |
  /_/ /  | /  | / /__/ /      |

  Abstract away complexity with `sakyum`
  
  An extension of flask web framework of python that erase the complexity of constructing flask project blueprint, packages, and other annoying stuffs
"""


__title__ = "sakyum"
__version__ = "0.0.3"
__author__ = "Usman Musa"
__author_email__ = "usmanmusa1920@gmail.com"
__author_website__ = "https://usmanmusa1920.github.io"
__copyright__ = "Copyright (C) 2022 - 2023 Usman Musa"


from .base import Boot
from .api import project
from .utils import stylePage

version_style = stylePage("do_nothing", "do_nothing", version=True)
version_style_desc = version_style[0]
version_style_border = version_style[1]