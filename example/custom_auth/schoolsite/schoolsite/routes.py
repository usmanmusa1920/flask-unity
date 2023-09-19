# from flask_unity software, your (schoolsite) project routes.py file
from flask_unity.utils import reg_blueprints_func
from exam.views import exam
from custom_auth.views import custom_auth


reg_blueprints = reg_blueprints_func(
    exam,
    custom_auth,
)


# overwrite (customise) error pages here
