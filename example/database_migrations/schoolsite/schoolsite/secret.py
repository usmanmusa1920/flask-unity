# from sakyum software, your (schoolsite) project secret.py file
import os
from pathlib import Path


ORIGIN_PATH = Path(__file__).resolve().parent.parent
OS_SEP = os.path.sep # platform-specific path separator (for linux `/`, for windows `\`)


class Config:
  SECRET_KEY = 'EK5oYCOUpEYLIVduxkS4b7qOHGasw1'
  # The `SQLALCHEMY_DATABASE_URI` might not be compatible with windows OS,
  # change it to your windows drive like: 'C:\path	o\your\default.db'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///'+str(ORIGIN_PATH)+OS_SEP+'default.db'
  # set optional bootswatch theme
  FLASK_ADMIN_SWATCH = 'cerulean'
  UPLOAD_FOLDER = os.path.join(ORIGIN_PATH, 'media')
  ALLOWED_EXTENSIONS = ('png', 'jpg', 'jpeg')
  MAX_CONTENT_LENGTH = 16 * 1024 * 1024


def load_env():
  os.environ['FLASK_UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
  os.environ['FLASK_ORIGIN_PATH'] = str(ORIGIN_PATH)
  os.environ['FLASK_ALLOWED_EXTENSIONS'] = str(Config.ALLOWED_EXTENSIONS)
