# Your project thunder.py file
from sakyum import Boot
  
boot = Boot()

if __name__ == "__main__":
  boot.run()

from todo_project import app
from todo_project.routes import base
from todo_app.views import todo_app

app.register_blueprint(base)
app.register_blueprint(todo_app)

app.run(debug=boot.d, port=boot.p, host=boot.h)
