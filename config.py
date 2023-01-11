import os

from decouple import config
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    FLASK_APP = config("FLASK_APP", default="main.py")
    SECRET_KEY = config("SECRET_KEY", default="secret_key")
