# Your project thunder.py file
from sakyum import Boot
from schoolsite.routes import reg_blueprints
from schoolsite.config import create_app
from schoolsite.secret import load_env


load_env()
boot = Boot()
if __name__ == "__main__":
  boot.run()


app = create_app(reg_blueprints)
app.run(debug=boot.d, port=boot.p, host=boot.h)
