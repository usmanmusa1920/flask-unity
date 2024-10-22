# from flask_unity software, your (schoolsite) project routes.py file
from flask import (Blueprint)
from flask_unity.utils import template_dir, static_dir
from flask_unity.utils import reg_blueprints_func
# from <app_name>.views import <app_name>


base = Blueprint(
    'base', __name__, template_folder=template_dir(), static_folder=static_dir('schoolsite')
)


reg_blueprints = reg_blueprints_func(
    base,
    # <app_name>,
)


# overwrite (customise) error pages here
