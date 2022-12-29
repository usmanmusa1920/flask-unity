
# =====================
# @ flaskey software
# =====================

"""___________________________________
       ____             _        __
      /___  /    /|   /_  /    /    \/
     /     /    /_|    / /_/  /__   /
    /     /___ /  | /_/ /  / /__   /
    
    Abstract away complexity with `flaskey`
    
    An extension of flask web framework of python that erase the complexity of constructing flask project blueprint, packages, and other annoying stuffs
"""

__title__ = "flaskey"
__version__ = "0.0.1"
__author__ = "Usman Musa"
__author_email__ = "usmanmusa1920@gmail.com"
__author_website__ = "https://usmanmusa1920.github.io"
__copyright__ = "Copyright 2022 Usman Musa"

from . dummy import _js
from . dummy import _css
from . dummy import _html

from . dummy import null
from . dummy import thunder_dummy

from . dummy import pro_init_dummy
from . dummy import pro_routes_dummy
from . dummy import app_views_dummy

from . base import boot
from . api import project
