# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages
from sakyum import (__title__, __version__, __author__, __author_email__, __repository__, __website__)


setup(
  
  # name of the main package (base folder)
  name=__title__,
  version=__version__,
  description='An extension of flask web framework that erase the complexity of structuring flask project blueprint, packages, and other annoying stuffs',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG').read(),
  long_description_content_type="text/markdown",
  python_requires='>=3.6',
  # platforms='any',
  
  # The URL of your package's (project) home page e.g. github link
  url=__website__,
  repo=__repository__,
  author=__author__,
  author_email=__author_email__,
  License='MIT',
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    # 'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.10',
  ],
  
  # used when people are searching for a module, keywords separated with a space
  keywords='sakyum',
  include_package_data = True, # include files listed in MANIFEST.in
  
  # The list of packages(directories) for your library
  packages=find_packages(), # OR packages=['sakyum'] 
  # If your package is a single module, use this instead of 'packages':
  # py_modules=[''] # list of files (modules) that are not in any directory (at the root dir)
  # the libraries it depends on
  
  # List of other python modules which this module depends on.  For example RPi.GPIO
  install_requires = [
    "bcrypt==4.0.1",
    "click==8.1.3",
    "dnspython==2.3.0",
    "email-validator==1.3.1",
    "Flask==2.2.3",
    "Flask-Admin==1.6.0",
    "Flask-Bcrypt==1.0.1",
    "Flask-Login==0.6.2",
    "Flask-SQLAlchemy==3.0.3",
    "Flask-WTF==1.1.1",
    "greenlet==2.0.2",
    "idna==3.4",
    "importlib-metadata==6.0.0",
    "itsdangerous==2.1.2",
    "Jinja2==3.1.2",
    "MarkupSafe==2.1.2",
    "SQLAlchemy==1.4.45",
    "typing-extensions==4.5.0",
    "Werkzeug==2.2.3",
    "WTForms==3.0.1",
    "zipp==3.13.0",
  ]
)
