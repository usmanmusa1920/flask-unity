# -*- coding: utf-8 -*-

long_comment = "\"\"\""


def null(long_comment=long_comment):
  return f"""{long_comment} write awesome code here! {long_comment}
"""

def thunder_dummy(project):
  return f"""from flask_unity import Boot
from auth.models import User
from {project} import app, db
from {project}.routes import reg_blueprints
from {project}.config import admin_runner


boot = Boot(db=db, model=User)
if __name__ == "__main__":
  boot.run()


for reg_blueprint in reg_blueprints:
  app.register_blueprint(reg_blueprint)
admin_runner()
app.run(debug=boot.d, port=boot.p, host=boot.h)
"""
