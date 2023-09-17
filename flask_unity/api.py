# -*- coding: utf-8 -*-
import os
import logging
from . import __title__
from . import __version__
from .base import BaseStructure


FORMATTER = '[+] [%(asctime)s] [%(levelname)s] %(message)s'
logging.basicConfig(format=FORMATTER)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


def project(name):
    """create project"""
    # we can use any of the below three variables to make our code compatible with
    # many OS, but we go with the first one which is `self.os_name`
    os_name = os.name  # nt or posix
    # platform_name_1 = sys.platform # win32 or linux or darwin or android
    # platform_name_2 = platform.system() # Windows, Darwin, Linux, etc.

    if os_name == 'nt' or os_name == 'posix':
        # if platform_name_1 == 'win32' or platform_name_1 == 'linux' or platform_name_1 == 'darwin' or platform_name_1 == 'android':
        # if platform_name_2 == 'Windows' or platform_name_2 == 'Linux' or platform_name_2 == 'Darwin'
        if name.lower() == __title__:
            print()
            LOGGER.error(
                f'Not allowed to use ({__title__}) package name as project name\n'
            )
            return False
        BaseStructure().dir_tree(name)
    else:
        err_compt = f'{__title__.capitalize()} v{__version__} is not compatible with your OS'
        print()
        LOGGER.error(err_compt)
        print()
        exit()
