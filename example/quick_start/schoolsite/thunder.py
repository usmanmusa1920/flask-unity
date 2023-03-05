# Your project thunder.py file
from sakyum import Boot
from auth.models import User
from schoolsite import db
from schoolsite.routes import reg_blueprints
from schoolsite.config import bcrypt, create_app


boot = Boot(db=db, model=User, pwd_hash=bcrypt)
if __name__ == "__main__":
  boot.run()


app = create_app(reg_blueprints)
app.run(debug=boot.d, port=boot.p, host=boot.h)
