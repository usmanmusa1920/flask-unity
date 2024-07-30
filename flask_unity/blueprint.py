# -*- coding: utf-8 -*-
from flask import Blueprint, render_template
from flask_admin.contrib.sqla import ModelView
from .utils import footer_style, template_dir, static_dir


# static_folder: the folder where the Blueprint's static files can be found
# static_url_path: the URL to serve static files from
# template_folder: the folder containing the Blueprint's templates
# url_prefix: the path to prepend to all of the Blueprint's URLs
# subdomain: the subdomain that this Blueprint's routes will match on by default
# url_defaults: a dictionary of default values that this Blueprint's views will receive
# root_path: the Blueprint's root dictionary path, whose default values is obtained from the Blueprint's import


default = Blueprint(
    'default', __name__, template_folder=template_dir(temp_from_pkg='default_page'), static_folder=static_dir('default_style', static_from_pkg=True)
)

errors = Blueprint(
    'errors', __name__, template_folder=template_dir(temp_from_pkg='default_errors')
)

auth = Blueprint(
    'auth', __name__, template_folder=template_dir(temp_from_pkg='default_page')
)


"""
The `default` blueprint above is the blueprint that is been used by flask_unity for linking
it default pages (css, js, and favicon.ico) files and also it can be use for our project
default html pages (landing page route) that is located in your project route.py file
`<project_name>/route.py` like ` @default.route() `, but instead we use ` @base.route() `
for that `<project_name>/routes.py` as default. We also register it in the project routes.py
file `reg_blueprints` list to make it accessible

The `errors` blueprint above is for error pages, you can overite the error pages by
defining them in your project routes.py file `<project_name>/route.py` just like the
way we did in here down below for some of our default error pages (400, 403, 500, etc)
by giving your desire template file path (correspond to your project templates folder)
for each error page

The `auth` blueprint above is for the `login, logout, register, change_password` and
other default authentication system (route) of your project, which will let you log into admin page
"""


@default.route('/', methods=['POST', 'GET'])
def index():
    """If there is no route like this in a project, then it will use this as default"""

    context = {
        'footer_style': footer_style,
    }
    return render_template('default_base.html', context=context)


def adminModelRegister(admin, reg_models, db):
    """Function that will register a direct model (not model view)"""

    for reg_model in reg_models:
        admin.add_view(ModelView(reg_model, db.session))


@errors.app_errorhandler(400)
def error_400(error):
    """Error page of 400"""

    context = {
        'head_title': 'error page',
        'err_msg': {"code": 400, "status": "bad request"},
        'footer_style': footer_style,
    }
    return render_template('error_page.html', context=context), 400


@errors.app_errorhandler(401)
def error_401(error):
    """Error page of 401"""
    
    context = {
        'head_title': 'error page',
        'err_msg': {"code": 401, "status": "unauthorized"},
        'footer_style': footer_style,
    }
    return render_template('error_page.html', context=context), 401


@errors.app_errorhandler(403)
def error_403(error):
    """Error page of 403"""
    
    context = {
        'head_title': 'error page',
        'err_msg': {"code": 403, "status": "forbidden"},
        'footer_style': footer_style,
    }
    return render_template('error_page.html', context=context), 403


@errors.app_errorhandler(404)
def error_404(error):
    """Error page of 404"""
    
    context = {
        'head_title': 'error page',
        'err_msg': {"code": 404, "status": "not found"},
        'footer_style': footer_style,
    }
    return render_template('error_page.html', context=context), 404


@errors.app_errorhandler(406)
def error_406(error):
    """Error page of 406"""
    
    context = {
        'head_title': 'error page',
        'err_msg': {"code": 406, "status": "not acceptable"},
        'footer_style': footer_style,
    }
    return render_template('error_page.html', context=context), 406


@errors.app_errorhandler(415)
def error_415(error):
    """Error page of 415"""
    
    context = {
        'head_title': 'error page',
        'err_msg': {"code": 415, "status": "unsupported media type"},
        'footer_style': footer_style,
    }
    return render_template('error_page.html', context=context), 415


@errors.app_errorhandler(429)
def error_429(error):
    """Error page of 429"""
    
    context = {
        'head_title': 'error page',
        'err_msg': {"code": 429, "status": "too many requests"},
        'footer_style': footer_style,
    }
    return render_template('error_page.html', context=context), 429


@errors.app_errorhandler(500)
def error_500(error):
    """Error page of 500"""
    
    context = {
        'head_title': 'error page',
        'err_msg': {"code": 500, "status": "internal server error"},
        'footer_style': footer_style,
    }
    return render_template('error_page.html', context=context), 500


@errors.app_errorhandler(501)
def error_501(error):
    """Error page of 501"""
    
    context = {
        'head_title': 'error page',
        'err_msg': {"code": 501, "status": "not implemented"},
        'footer_style': footer_style,
    }
    return render_template('error_page.html', context=context), 501


@errors.app_errorhandler(502)
def error_502(error):
    """Error page of 502"""
    
    context = {
        'head_title': 'error page',
        'err_msg': {"code": 502, "status": "bad gateway"},
        'footer_style': footer_style,
    }
    return render_template('error_page.html', context=context), 502


@errors.app_errorhandler(503)
def error_503(error):
    """Error page of 503"""
    
    context = {
        'head_title': 'error page',
        'err_msg': {"code": 503, "status": "service unavailable"},
        'footer_style': footer_style,
    }
    return render_template('error_page.html', context=context), 503


@errors.app_errorhandler(504)
def error_504(error):
    """Error page of 504"""
    
    context = {
        'head_title': 'error page',
        'err_msg': {"code": 504, "status": "gateway timeout"},
        'footer_style': footer_style,
    }
    return render_template('error_page.html', context=context), 504
