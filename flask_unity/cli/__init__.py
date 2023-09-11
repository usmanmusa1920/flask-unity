# -*- coding: utf-8 -*-
import argparse


def cli():
    """Flask-Unity command-line utility function that instanciate project"""

    parser = argparse.ArgumentParser(
        prog='project', description='This create your project')
    # metavar make the -help to look cleaan
    parser.add_argument(
        '--project', '-p', required=True, type=str, metavar='', help='What is the project name')
    args = parser.parse_args()
    
    from flask_unity import project
    project(args.project)
