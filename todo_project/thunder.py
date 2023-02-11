# Your project thunder.py file
from sakyum import Boot
  
boot = Boot()

if __name__ == "__main__":
  boot.run()

from todo_project import app
from todo_project.routes import urls

for url in urls:
  app.register_blueprint(url)

app.run(debug=boot.d, port=boot.p, host=boot.h)
