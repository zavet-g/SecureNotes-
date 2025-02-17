import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "supersecretkey"
