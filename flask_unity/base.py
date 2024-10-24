# -*- coding: utf-8 -*-
import os
import sys
import shlex
import logging
import argparse
import platform
import subprocess as sp

from pathlib import Path

from .mute import run_dummy
from .mute.page import _js
from .mute.page import _css
from .mute.page import _html
from .mute.app import app_admin_dummy
from .mute.app import app_forms_dummy
from .mute.app import app_models_dummy
from .mute.app import app_views_dummy
from .mute.app import app_init_dummy
from .mute.project import pro_init_dummy
from .mute.project import pro_secret_dummy
from .mute.project import pro_config_dummy
from .mute.project import pro_routes_dummy
from . mute.db import generate_ini
from . mute.db import generate_env
from . mute.db import generate_script_py_mako
from . mute.db import generate_readme
from .auth.models import User
from .contrib import db, bcrypt
from . _log import log_style
from . import __title__
from . import __version__

"""
    NOTSET    ---  0
    DEBUG     ---  10
    INFO      ---  20
    WARNING   ---  30  (default)
    ERROR     ---  40
    CRITICAL  ---  50
"""

FORMATTER = '[+] [%(asctime)s] [%(levelname)s] %(message)s'
logging.basicConfig(format=FORMATTER)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

# used for relative path to default image to copy for a project (only)
ORIGIN = Path(__file__).resolve().parent

# platform-specific path separator (for linux `/`, for windows `\\`)
OS_SEP = os.path.sep


class BaseStructure:
    """Base structure class"""

    def __init__(self, is_software=True):
        """Base structure class initializer"""

        self.is_software = is_software

        # we can use any of the below three variables to make our code compatible with
        # many OS, but we go with the first one which is `self.os_name`
        
        # nt or posix
        self.os_name = os.name
        # win32 or linux or darwin or android
        self.platform_name_1 = sys.platform
        # Windows, Darwin, Linux, etc.
        self.platform_name_2 = platform.system()

        if self.os_name == 'nt':
            # if self.platform_name_1 == 'win32':
            # if self.platform_name_2 == 'Windows':
            self.fls_cmd = 'echo >'
        elif self.os_name == 'posix':
            # elif self.platform_name_1 == 'linux' or self.platform_name_1 == 'darwin' or self.platform_name_1 == 'android':
            # elif self.platform_name_2 == 'Linux' or self.platform_name_2 == 'Darwin':
            self.fls_cmd = 'touch'
        else:
            err_compt = f'{__title__.capitalize()} v{__version__} is not compatible with your OS'
            print()
            LOGGER.error(err_compt)
            print()
            exit()
        self._exs_first = ['index', 'style']
        self._exs_last = ['.html', '.css', '.js']

    def append_exs_to_file(self, fls_name=False, _exs_='.py', name=None):
        """Append .py extension for files if _exs_ value is '.py' or type is str, else if _exs_ type is list, make list of static files `['index.html', 'index.js', 'style.css']`
        """

        if type(_exs_) == list:
            name, exst = self._exs_first, self._exs_last
            lst = []

            for i in exst:
                if i == exst[1]:  # css
                    idx = name[1]
                    lst.append(f'{idx}{i}')

                if i == exst[0] or i == exst[2]:  # html & js
                    for j in exst:
                        if j != exst[1]:
                            idx = name[0]
                            if f'{idx}{j}' in lst:
                                pass
                            else:
                                lst.append(f'{idx}{j}')
            return lst
        if type(_exs_) == str:
            return [i+f'{_exs_}' for i in fls_name]

    def file_content(
        self,
        _exs=False,
        content=None,
        file_name='index',
        dir_togo=None,
        route_go=True
    ):
        """Insert content in a file"""

        if _exs:
            with open(f'{file_name}{_exs}', 'w') as pay_fls:
                pay_fls.write(f'{content}')
        else:
            with open(f'{file_name}', 'w') as pay_fls:
                pay_fls.write(f'{content}')
        if route_go:
            os.chdir(dir_togo)

    def instanciate_default_img(self):
        """Instanciate user default image"""

        file_path = os.path.join(
            ORIGIN, 'static', 'default_style', 'media', 'default_img.png')
        with open(file_path, mode='rb') as img_read:
            img_read_data = img_read.read()
        with open('default_img.png', mode='wb') as img_write:
            img_write.write(img_read_data)

    def file_opt(self, _dir, tree=True, _here=False, _where=False):
        """Make dir tree if `tree=True` and get into it, if `_here` or `_where` is equal to True"""

        if tree:
            if self.os_name == 'nt':
                os.makedirs(_dir, exist_ok=True)
                # The exist_ok=True argument ensures that the function
                # does not raise an exception if the directory already exists.
            elif self.os_name == 'posix':
                sp.run(['mkdir', '-p', _dir])
            else:
                err_compt = f'{__title__.capitalize()} v{__version__} is not compatible with your OS'
                print()
                LOGGER.error(err_compt)
                print()
                exit()
        if _here:
            os.chdir(os.path.join(_here, _dir))
        if _where:
            os.chdir(_where)

    def validate_project_or_app_name(self, name, type_of=False):
        """Validate project or app name"""

        if type_of:
            proj_or_app = 'project'
        else:
            proj_or_app = 'app'
        un_accept_char = '@-/\\^+#&*!=%$?.>\'<,"\';:`~|}{][)('

        for i in un_accept_char:
            if i in name:
                name_err = f'[{un_accept_char}] are characters that are not allowed to be in your {proj_or_app} name, we found `{i}` in the name ({name})\n'
                print()
                LOGGER.error(name_err)
                exit()

    def into_file(
        self,
        fls,
        fls_cmd,
        file=None,
        app_default_dummy=None,
        is_static_file=False,
        is_app=False,
        proj_nm=None
    ):
        """Create files within current directory of `self.file_opt()`
        is_app: if it is True, that mean it will do operation of making app files,
        else it will make for the entire project
        """

        if is_app:
            for _fls in fls:
                app_name = os.getcwd().split(OS_SEP)[-1]
                if self.os_name == 'nt':
                    sp.run(shlex.split(f'{fls_cmd} {_fls}'), shell=True)
                elif self.os_name == 'posix':
                    sp.run(shlex.split(f'{fls_cmd} {_fls}'))
                else:
                    err_compt = f'{__title__.capitalize()} v{__version__} is not compatible with your OS'
                    print()
                    LOGGER.error(err_compt)
                    print()
                    exit()
                if is_static_file:
                    # building app default files (html, css, js)
                    self.file_content(
                        file_name=_fls, content=f'{app_default_dummy}', route_go=False)
                else:
                    # building app default files (__init__.py, admin.py, forms.py, models.py, views.py)
                    if _fls == '__init__.py':
                        self.file_content(
                            file_name=_fls, content=f'# from {__title__} software, your app ({app_name}) {_fls} file\n{app_init_dummy()}', route_go=False)
                    elif _fls == 'admin.py':
                        self.file_content(
                            file_name=_fls, content=f'# from {__title__} software, your app ({app_name}) {_fls} file\n{app_admin_dummy()}', route_go=False)
                    elif _fls == 'forms.py':
                        self.file_content(
                            file_name=_fls, content=f'# from {__title__} software, your app ({app_name}) {_fls} file\n{app_forms_dummy()}', route_go=False)
                    elif _fls == 'models.py':
                        self.file_content(
                            file_name=_fls, content=f'# from {__title__} software, your app ({app_name}) {_fls} file\n{app_models_dummy()}', route_go=False)
                    elif _fls == 'views.py':
                        self.file_content(
                            file_name=_fls, content=f'# from {__title__} software, your app ({app_name}) {_fls} file\n{app_views_dummy(app_name)}', route_go=False)
        else:
            for _fls in fls:
                if _fls[:-3] == file:
                    if self.os_name == 'nt':
                        sp.run(shlex.split(f'{fls_cmd} {_fls}'), shell=True)
                    elif self.os_name == 'posix':
                        sp.run(shlex.split(f'{fls_cmd} {_fls}'))
                    else:
                        err_compt = f'{__title__.capitalize()} v{__version__} is not compatible with your OS'
                        print()
                        LOGGER.error(err_compt)
                        print()
                        exit()

                    self.file_content(
                        file_name='alembic.ini', content=f'{generate_ini(proj_nm)}', route_go=False
                    )  # building the alembic ini file `alembic.ini`
                    self.file_content(
                        file_name=_fls, content=f'# Your project {_fls} file\n{run_dummy(proj_nm)}', route_go=False
                    )  # building the run module `run.py`

    def dir_tree(self, proj_name=None):
        """Create a directory tree where file will reserved as well as modules too"""

        self.validate_project_or_app_name(proj_name, type_of=True)
        dirs = [proj_name, f'{proj_name}{OS_SEP}{proj_name}', 'media', 'templates', 'static']

        # default files of project sub folder, except `run` which is for project base dir
        fls_name = ['__init__', 'config', 'routes', 'secret', 'run']
        # appending extensions to files
        fls = self.append_exs_to_file(fls_name=fls_name)
        _here = os.getcwd()  # initial `cwd` where the project was e.g `Desktop`

        # check if the project already exist
        if os.path.exists(os.path.join(_here, proj_name)):
            print(
                f'\nProject ({proj_name}) already exist in this directory\n\t' + os.path.realpath(proj_name))
            LOGGER.info(_here)
            print()
        else:
            # making directories trees and their default files in the loop
            for _dir in dirs:
                if _dir == dirs[0] + OS_SEP + dirs[0]:
                    self.file_opt(_dir, _here=_here)
                    # create default modules inside project sub dir
                    for _fls in fls:
                        if _fls[:-3] != 'run':
                            if self.os_name == 'nt':
                                sp.run(shlex.split(
                                    f'{self.fls_cmd} {_fls}'), shell=True)
                            elif self.os_name == 'posix':
                                sp.run(shlex.split(f'{self.fls_cmd} {_fls}'))
                            else:
                                err_compt = f'{__title__.capitalize()} v{__version__} is not compatible with your OS'
                                print()
                                LOGGER.error(err_compt)
                                print()
                                exit()
                            # building project default files (__init__.py, config.py, routes.py, secret.py)
                            if _fls == '__init__.py':
                                self.file_content(
                                    file_name=_fls, content=f'# from {__title__} software, your ({proj_name}) project {_fls} file\n{pro_init_dummy()}', route_go=False)
                            elif _fls == 'config.py':
                                self.file_content(
                                    file_name=_fls, content=f'# from {__title__} software, your ({proj_name}) project {_fls} file\n{pro_config_dummy(proj_name)}', route_go=False)
                            elif _fls == 'routes.py':
                                self.file_content(
                                    file_name=_fls, content=f'# from {__title__} software, your ({proj_name}) project {_fls} file\n{pro_routes_dummy(proj_name)}', route_go=False)
                            elif _fls == 'secret.py':
                                self.file_content(
                                    file_name=_fls, content=f'# from {__title__} software, your ({proj_name}) project {_fls} file\n{pro_secret_dummy()}', route_go=False)
                    os.chdir(_here)

                if _dir == dirs[0]:
                    self.file_opt(_dir, _here=_here)
                    # to make run file
                    self.into_file(fls, self.fls_cmd, file='run', proj_nm=proj_name)
                    # to make alembic.ini file
                    self.into_file(['alembic.ini'], self.fls_cmd)
                    
                    project_folder = os.getcwd()  # base dir path of the project (parent dir)

                    # making directories trees and their default files in the loop
                    for _dir in ['migrations']:
                        self.file_opt(_dir, _here=project_folder)
                        for _fls_migrations in ['env.py', 'script.py.mako', 'README']:
                            if self.os_name == 'nt':
                                sp.run(shlex.split(
                                    f'{self.fls_cmd} {_fls_migrations}'), shell=True)
                            elif self.os_name == 'posix':
                                sp.run(shlex.split(f'{self.fls_cmd} {_fls_migrations}'))
                            else:
                                err_compt = f'{__title__.capitalize()} v{__version__} is not compatible with your OS'
                                print()
                                LOGGER.error(err_compt)
                                print()
                                exit()
                            # building migrations files (env.py, script.py.mako, README)
                            if _fls_migrations == 'env.py':
                                self.file_content(
                                    file_name=_fls_migrations, content=generate_env(), route_go=False)
                            elif _fls_migrations == 'script.py.mako':
                                self.file_content(
                                    file_name=_fls_migrations, content=generate_script_py_mako(), route_go=False)
                            elif _fls_migrations == 'README':
                                self.file_content(
                                    file_name=_fls_migrations, content=generate_readme(), route_go=False)
                        self.file_opt('versions')
                        os.chdir(project_folder)

                    for static_dir in dirs[3:]:  # templates & static
                        if static_dir == dirs[3:][0]:  # templates
                            # make templates dir and cd into it
                            self.file_opt(static_dir, _here=project_folder)
                            templates_folder = os.getcwd()  # base dir path of templates folder
                            
                            # make project admin dir in templates and cd into it
                            self.file_opt('admin', _here=templates_folder)
                            # create project admin index.html and back to project base dir path
                            self.file_content(self._exs_last[0], content=f'<!-- @{__title__}, {proj_name} (project) admin index.html page -->\n'+_html(
                                'do_nothing', is_admin=True, project_name=proj_name), dir_togo=project_folder)

                        if static_dir == dirs[3:][1]:  # static
                            # make static dir and cd into
                            self.file_opt(static_dir, _here=project_folder)
                            static_base_dir = os.getcwd()  # base dir path of static folder
                            
                    os.chdir(project_folder)
                    # make media folder and default image inside it
                    self.file_opt(dirs[2], _where=dirs[2])
                    self.instanciate_default_img()
                    os.chdir(_here)

            print()
            # # LOGGER.info(f'Project ({proj_name}) created successfully!')
            log_style(f'Project ({proj_name}) created successfully!')
            log_style('Make migrations before proceeding', col='yellow')
            print()


class AppStructure(BaseStructure):
    """Base structure class"""

    app_store_name = None  # app name
    proj_store_name = None  # project name

    def app_static_and_template(
        self,
        file_dummy,
        top_comment=False,
        _dir_=False,
        file=False,
        app=False,
        cmd=False,
        _here_=False
    ):
        """
        #: _dir_ = 'template or static'
        #: file = ['index.html']
        #: app = app name
        #: cmd = 'touch'
        #: _here_ = # initial `inside project folder` where the project was created
        """

        store_top_comment = top_comment

        if top_comment == 'html':
            top_comment = f'<!-- @{__title__}, {app} {file[0]} page -->\n'
        if top_comment == 'css':
            top_comment = f'/* @{__title__}, {app} {file[0]} file */\n'
        if top_comment == 'js':
            top_comment = f'// @{__title__}, {app} {file[0]} file\n'

        self.file_opt(_dir_, tree=False, _here=_here_)  # back to template dir
        self.file_opt(f'{app}', _where=app)  # make app dir inside `template`
        
        if os.getcwd().split(OS_SEP)[-2] == 'static':
            for stic_dir in ['css', 'js']:
                self.file_opt(stic_dir, _where=stic_dir) # make whether `css/js` in static dir
                # making app default file, if the file extension (store_top_comment) match current loop item
                if store_top_comment == stic_dir:
                    self.into_file(
                        file, cmd, is_static_file=True, app_default_dummy=f'{top_comment}{file_dummy}', is_app=True
                    )
                os.chdir(_here_ + OS_SEP + 'static' + OS_SEP + app)
        else:
            # making app default file (in template) dir
            self.into_file(
                file, cmd, is_static_file=True, app_default_dummy=f'{top_comment}{file_dummy}', is_app=True
            )

    def dir_tree(self, proj_app_name=None):
        """Create a directory tree where file will reserved as well as modules too"""

        dirs = [proj_app_name]
        self.validate_project_or_app_name(proj_app_name)

        app_store_name = proj_app_name  # store our app name
        fls_name = ['__init__', 'views', 'models', 'forms', 'admin']
        fls = self.append_exs_to_file(fls_name=fls_name)
        roove_dir = ['templates', 'static', 'static']
        _here_app = os.getcwd()  # initial `inside project folder` (parent) directory

        # check if the app already exist
        app_proj_name = _here_app.split(OS_SEP)[-1]
        self.proj_store_name = app_proj_name

        if os.path.exists(os.path.join(_here_app, proj_app_name)):
            print(f'\nApp ({proj_app_name}) already exist in this project ({app_proj_name})\n\t' +
                  os.path.realpath(proj_app_name))
            LOGGER.info(_here_app)
            print()
        else:
            # making directories trees and their default files
            for _dir in dirs:
                if _dir == dirs[0]:
                    self.file_opt(_dir, _here=_here_app)
                    # to maker app default files
                    self.into_file(fls, self.fls_cmd, is_app=True)

            self.app_static_and_template(
                _html(app_store_name, project_name=self.proj_store_name, is_base_app=True), top_comment='html', _dir_=roove_dir[0], file=[self.append_exs_to_file(_exs_=[])[0]], app=proj_app_name, cmd=self.fls_cmd, _here_=_here_app
            )
            self.app_static_and_template(
                _css(), top_comment='css', _dir_=roove_dir[1], file=[self.append_exs_to_file(_exs_=[])[2]], app=proj_app_name, cmd=self.fls_cmd, _here_=_here_app
            )
            self.app_static_and_template(
                _js(proj_app_name), top_comment='js', _dir_=roove_dir[2], file=[self.append_exs_to_file(_exs_=[])[1]], app=proj_app_name, cmd=self.fls_cmd, _here_=_here_app
            )
            self.file_opt('media')  # an app media folder
            self.file_opt('do_nothing', tree=False,
                          _where=_here_app)  # back to project dir
            print()
            log_style(f'App ({proj_app_name}) created successfully! in {app_proj_name}')
            print()


def app_init(app):
    """Initialize app in project"""

    AppStructure().dir_tree(app)
    exit()


class Boot:
    """Boot up project operation, app operation, and the server"""

    def __init__(self, p=None, d=False, h=None, db=db, model=User, pwd_hash=bcrypt):
        self.p = p  # port
        self.d = d  # debug
        self.h = h  # host
        self.db = db  # database
        self.model = model
        self.pwd_hash = pwd_hash

    def run(self):
        """Run method for creating app and booting up server"""

        error_ref_1 = f'''\n Run the command with one of this positional arguments:\n\tcreate_app   ---   ( for creating an app within your project )\n\tboot  ---   ( for booting up your server )'''

        error_ref_2 = f'''
  create_app:
    usage: create_app [-h] --app  [--debug]

    This create an app in your project

    positional arguments:
                    Put positional argument of `create_app` to create app, app are create inside your project

    optional arguments:
      -h, --help     show this help message and exit
      --app , -a     What is the app name
  create_user:
    usage: create user [-h] [--username] [--email] [--password]

    This create user

    positional arguments:
                        Put positional argument of `create_user` to create user

    options:
      -h, --help        show this help message and exit
      --username , -u   What is the username?
      --email , -e      What is the email?
      --password , -p   What is the password?

  boot:
    usage: boot up server [-h] [--port] [--host] [--debug]

    This boot up the server

    positional arguments:
                    Put positional argument of `boot` to bring server up running

    optional arguments:
      -h, --help     show this help message and exit
      --port , -p    What is the port number?
      --host , -H    What is the host?
      --debug , -d   Do you want debug?'''
        if len(sys.argv) == 1:
            print()
            LOGGER.error(
                f'please run the module with positional argument and flag if needed\n{error_ref_1}')
            exit()

        if sys.argv[1] == 'create_app':
            # prog is the name of the program, default=sys.argv[0]
            parser = argparse.ArgumentParser(
                prog='create_app', description='This create an app in your project')
            # metavar make the -help to look cleaan
            parser.add_argument('--app', '-a', required=True,
                                type=str, metavar='', help='What is the app name')
            parser.add_argument(dest='create_app', default='create_app', type=str, metavar='',
                                help='Put positional argument of `create_app` to create app, app are create inside your project')
            args = parser.parse_args()
            the_proj = os.getcwd().split(OS_SEP)[-1]

            if args.app.lower() == __title__:
                print()
                log_style(
                    f'Not allowed to use ({__title__}) package name as an app name\n', log='error')
                exit()
            elif args.app == the_proj:
                print()
                log_style(
                    f'Not allowed to use your ({the_proj}) project name as an app name\n', log='error')
                exit()
            app_init(args.app)

        elif sys.argv[1] == 'boot':
            parser = argparse.ArgumentParser(
                prog='boot up server', description='This boot up the server')
            parser.add_argument(
                '--port', '-p', default=5000, required=False, type=int, metavar='', help='What is the port number?')
            parser.add_argument(
                '--host', '-H', default=self.h, required=False, type=str, metavar='', help='What is the host?')
            parser.add_argument(
                '--debug', '-d', default=False, required=False, type=bool, metavar='', help='Do you want debug?')
            parser.add_argument(
                dest='boot', default='boot', type=str, metavar='', help='Put positional argument of `boot` to bring server up running')
            args = parser.parse_args()
            self.p = args.port
            self.h = args.host
            if os.environ.get('FLASK_DEBUG') and os.environ.get('FLASK_DEBUG') == '1':
                self.d = True
                LOGGER.info(
                    ' * You have set an environment variable of `FLASK_DEBUG` to \'1\'')
            else:
                self.d = args.debug

            # LOGGER.info(f'@{__title__} v{__version__} | visit: http://localhost:{args.port} (for development)')

        elif sys.argv[1] == 'create_user':
            parser = argparse.ArgumentParser(
                prog='create user', description='This create user')
            parser.add_argument(
                '--username', '-u', required=False, type=str, metavar='', help='What is the username?')
            parser.add_argument(
                '--email', '-e', required=False, type=str, metavar='', help='What is the email?')
            parser.add_argument(
                '--password', '-p', required=False, type=str, metavar='', help='What is the password?')
            parser.add_argument(
                dest='create_user', default='create_user', type=str, metavar='', help='Put positional argument of `create_user` to create user')
            args = parser.parse_args()

            from .utils import AuthCredentials
            if args.username != None:
                args_u = False
                usr = args.username
            else:
                args_u = True
                usr = None
            if args.email != None:
                args_e = False
                mail = args.email
            else:
                args_e = True
                mail = None
            if args.password != None:
                args_p = False
                pwd = args.password
            else:
                args_p = True
                pwd = None

            auth_class = AuthCredentials(
                username=usr, email=mail, password=pwd, u_args=args_u, e_args=args_e, p_args=args_p)
            auth_result = auth_class.result
            username = auth_result[0]
            email = auth_result[1]
            raw_password = auth_result[2]

            hashed_password = self.pwd_hash.generate_password_hash(
                raw_password).decode('utf-8')
            user = self.model(
                username=username, email=email, password=hashed_password, is_admin=True)
            self.db.session.add(user)
            self.db.session.commit()
            print()
            LOGGER.info(f'One user record added ({username})\n')
            exit()
        else:
            print()
            LOGGER.error(f'use a valid positional argument and flag if needed\n{error_ref_2}')
            exit()
