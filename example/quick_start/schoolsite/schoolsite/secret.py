# from sakyum software, your (schoolsite) project secret.py file
import os
from pathlib import Path

origin_path = Path(__file__).resolve().parent.parent

class Config:
  SECRET_KEY = 'n5I4hgQJFMp2HWQEoFoMN6GcE5SaAZDVyChWgdD'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///'+str(origin_path)+'/default.db'
  # set optional bootswatch theme
  FLASK_ADMIN_SWATCH = 'cerulean'
  UPLOAD_FOLDER = os.path.join(origin_path, 'media')
  ALLOWED_EXTENSIONS = ('png', 'jpg', 'jpeg', 'gif')
  MAX_CONTENT_LENGTH = 16 * 1024 * 1024


def load_env():
  os.environ['FLASK_UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
  os.environ['FLASK_ORIGIN_PATH'] = str(origin_path)
  os.environ['FLASK_ALLOWED_EXTENSIONS'] = str(Config.ALLOWED_EXTENSIONS)
