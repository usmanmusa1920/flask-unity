# from sakyum software, your (schoolsite) project __init__.py file
from .config import create_app
from .config import db

app = create_app()
