# -*- coding: utf-8 -*-
import os
import sys
import shlex
import argparse
import subprocess as sp
from .._log import log_style


def cli():
    """Flask-Unity command-line utility function"""

    error_help = f'''\nUsage:

    To create project:
        flask_unity -p <project_name>, or
        flask_unity --project <project_name>

    To make migrations:
        flask_unity db makemigrations

    To migrate your database:
        flask_unity db migrate
        '''
    
    def err_log():
        """error log"""
        print()
        log_style(
            'Please run the command with correct positional argument and flag if needed', log='info')
        print(error_help)
        exit()

    if len(sys.argv) == 2 or len(sys.argv) == 1:
        err_log()

    if sys.argv[1] == 'db':
        os_name = os.name  # nt or posix
        
        # make migrations
        if sys.argv[2] == 'makemigrations':
            if os_name == 'nt':
                sp.run(shlex.split(f'alembic revision --autogenerate -m "Changes migrated!"'), shell=True)
            elif os_name == 'posix':
                sp.run(shlex.split(f'alembic revision --autogenerate -m "Changes migrated!"'))
            else:
                pass
            
        # apply migrations
        elif sys.argv[2] == 'migrate':
            if os_name == 'nt':
                sp.run(shlex.split(f'alembic upgrade head'), shell=True)
            elif os_name == 'posix':
                sp.run(shlex.split(f'alembic upgrade head'))
            else:
                pass
        else:
            err_log()
            
    # initialise project
    if sys.argv[1] != 'db':
        parser = argparse.ArgumentParser(
            prog='project', description='This create your project')
        # metavar make the -help to look cleaan
        parser.add_argument(
            '--project', '-p', required=True, type=str, metavar='', help='What is the project name')
        args = parser.parse_args()
        
        from flask_unity.api import project
        project(args.project)
