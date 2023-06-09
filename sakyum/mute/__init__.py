# -*- coding: utf-8 -*-

from sakyum import __title__
from sakyum.utils import Security
from sakyum.utils import stylePage


secret = Security()
secure_app = secret.passcode_salt
f1 = '{'
l1 = '}'
f2 = '{{'
l2 = '}}'
long_comment = '"""'


def thunder_dummy(project):
  return f"""from sakyum import Boot
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
