from setuptools import setup
from setuptools import find_packages


setup(
  
  # name of the main package (sakyum)
  name='sakyum',
  version='0.0.3',
  
  description='An extension of flask web framework that erase the complexity of structuring flask project blueprint, packages, and other annoying stuffs',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG').read(),
  long_description_content_type="text/markdown",
  
  # The URL of your package's (project) home page e.g. github link
  url='https://github.com/usmanmusa1920/sakyum',
  
  # Author details
  author='Usman Musa',
  author_email='usmanmusa1920@gmail.com',
  
  # Choose your license, note the American spelling
  License='MIT',
  
  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3'
  ],
  
  # used when people are searching for a module, keywords separated with a space
  keywords='sakyum',
  
  # The list of packages(directories) for your library
  packages=find_packages(), # OR packages=['sakyum'] 
  
  # If your package is a single module, use this instead of 'packages':
  # py_modules=[''] # list of files (modules) that are not in any directory (at the root dir)
  # the libraries it depends on
  
  include_package_data = True, # include files listed in MANIFEST.in
  
  # List of other python modules which this module depends on.  For example RPi.GPIO
  install_requires=['click==8.1.3', 'Flask==2.2.2', 'Flask-Admin==1.6.0', 'Flask-SQLAlchemy==3.0.2', 'Flask-WTF==1.0.1', 'greenlet==2.0.1', 'importlib-metadata==6.0.0', 'itsdangerous==2.1.2', 'Jinja2==3.1.2', 'MarkupSafe==2.1.1', 'SQLAlchemy==1.4.45', 'Werkzeug==2.2.2', 'WTForms==3.0.1', 'zipp==3.11.0']
  # install_requires=['click==8.1.3', 'Flask==2.2.2', 'Flask-Admin==1.6.0', 'Flask-SQLAlchemy==3.0.2', 'Flask-WTF==1.0.1', 'greenlet==2.0.1', 'importlib-metadata==6.0.0', 'itsdangerous==2.1.2', 'Jinja2==3.1.2', 'MarkupSafe==2.1.1', 'SQLAlchemy==1.4.45', 'Werkzeug==2.2.2', 'WTForms==3.0.1', 'zipp==3.11.0']
)