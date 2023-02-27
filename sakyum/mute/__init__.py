# -*- coding: utf-8 -*-

long_comment = "\"\"\""


def null(long_comment=long_comment):
  return f"""{long_comment} write awesome code here! {long_comment}
"""

def thunder_dummy(project):
  return f"""from sakyum import Boot
from auth.models import User
from {project} import db
from {project}.routes import reg_blueprints
from {project}.config import bcrypt, create_app


boot = Boot(db=db, model=User, pwd_hash=bcrypt)
if __name__ == "__main__":
  boot.run()


app = create_app(reg_blueprints)
app.run(debug=boot.d, port=boot.p, host=boot.h)
"""
