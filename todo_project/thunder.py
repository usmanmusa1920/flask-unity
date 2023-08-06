# Your project thunder.py file
from flask_unity import Boot
from auth.models import User
from todo_project import app, db
from todo_project.routes import reg_blueprints
from todo_project.config import admin_runner


boot = Boot(db=db, model=User)
if __name__ == "__main__":
  boot.run()


for reg_blueprint in reg_blueprints:
  app.register_blueprint(reg_blueprint)
admin_runner()
app.run(debug=boot.d, port=boot.p, host=boot.h)
