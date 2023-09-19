# from flask_unity software, your (schoolsite) project routes.py file
from flask_unity.utils import reg_blueprints_func
from exam.views import exam


reg_blueprints = reg_blueprints_func(
    exam,
)


# overwrite (customise) error pages here
