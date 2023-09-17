# -*- coding: utf-8 -*-
import re
import os
from setuptools import setup
from setuptools import find_packages


def grep(attrname):
    """get package info from __init__.py file"""
    file_path = os.path.join(os.path.dirname(__file__), 'flask_unity/__init__.py')

    # content of the file
    read_file = open(file_path).read()

    # pattern match using regex
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)

    # our regex value
    attr_value, = re.findall(pattern, read_file)
    return attr_value


setup(
    # name of the main package (base folder i.e flask_unity)
    name = grep('__title__'),
    version = grep('__version__'),
    description = grep('__description__'),
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG').read(),
    long_description_content_type = 'text/markdown',
    python_requires = '>=3.6',
    platforms = 'any',
    
    # Use console_scripts to hook to a specific Python method (not a whole executable),
    entry_points = {
        'console_scripts': [f'{grep("__title__")}={grep("__title__")}.cli:cli'],
    },
    
    url = grep('__url__'),
    download_url = 'https://pypi.org/project/flask-unity',
    author = grep('__author__'),
    author_email = grep('__author_email__'),
    license = grep('__license__'),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Flask',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    
    # used when people are searching for a module, keywords separated with a space
    keywords = 'flask_unity',
    include_package_data = True,  # include files listed in MANIFEST.in
    
    # The list of packages(directories) for your library
    packages = find_packages(),  # OR packages = ['flask_unity']
    # If your package is a single module, use this instead of 'packages':
    # py_modules = [''] # list of files (modules) that are not in any directory (at the root dir)
    # the libraries it depends on
    
    # List of other python modules which this module depends on. For example RPi.GPIO
    install_requires = [
        'alembic>=1.9.4',
        'bcrypt>=4.0.1',
        'click>=8.1.3',
        'dnspython>=2.3.0',
        'email-validator>=1.3.1',
        'Flask>=2.2.3',
        'Flask-Admin>=1.6.0',
        'Flask-Bcrypt>=1.0.1',
        'Flask-Login>=0.6.2',
        'Flask-SQLAlchemy>=3.0.3',
        'Flask-WTF>=1.1.1',
        'greenlet>=2.0.2',
        'idna>=3.4',
        'importlib-metadata>=6.0.0',
        'itsdangerous==2.1.2', #  (Dec 10, 2022)
        'Jinja2>=3.1.2',
        'Mako>=1.2.4',
        'MarkupSafe>=2.1.2',
        'SQLAlchemy>=1.4.45',
        'typing-extensions>=4.5.0',
        'Werkzeug>=2.2.3',
        'WTForms>=3.0.1',
        'zipp>=3.13.0',
    ],
    project_urls = {
        'Documentation': grep('__url__'),
        'Source': grep('__repository__'),
    },
)
