# Your project thunder.py file
from sakyum import Boot
  
boot = Boot()
if __name__ == "__main__":
  boot.run()

from todo_project import app
from todo_project.routes import reg_blueprints

for reg_blueprint in reg_blueprints:
  app.register_blueprint(reg_blueprint)
app.run(debug=boot.d, port=boot.p, host=boot.h)
