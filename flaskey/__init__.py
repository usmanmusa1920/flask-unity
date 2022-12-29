# =====================
# @ flaskey software
# =====================

"""
    ######  #         ##     ####   #    #  ######   #   #
    #       #        #  #   #       #   #   #         # #
    #####   #       #    #   ####   ####    #####      #
    #       #       ######       #  #  #    #          #
    #       #       #    #  #    #  #   #   #          #
    #       ######  #    #   ####   #    #  ######     #
    
    
    Abstract away complexity with `flaskey`
    
    an extension of flask python web frame work that erase the complexity
    of constructing flask project and packages within it (apps)
"""

__title__ = "flaskey"
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
from . dummy import pro_config_dummy
from . dummy import pro_models_dummy
from . dummy import pro_routes_dummy

from . dummy import app_init_dummy
from . dummy import app_routes_dummy
from . dummy import app_forms_dummy
from . dummy import app_utils_dummy
from . dummy import app_views_dummy

from . base import boot
from . api import project

