# -*- coding: utf-8 -*-
from flask_unity import __title__
from flask_unity.utils import Security
from flask_unity.utils import style_page


secret = Security()
secure_app = secret.passcode_salt
f1 = '{'
l1 = '}'
f2 = '{{'
l2 = '}}'
long_comment = '"""'


def run_dummy(project):
    return f"""from flask_unity import Boot
from {project}.routes import reg_blueprints
from {project}.config import create_app
from {project}.secret import load_env


load_env()
boot = Boot()
if __name__ == '__main__':
    boot.run()


app = create_app(reg_blueprints)
app.run(debug=boot.d, port=boot.p, host=boot.h)
"""
