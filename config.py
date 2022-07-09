import os

from decouple import config
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config(object):
    FLASK_APP = config("SECRET_KEY", default="app.py")
    SECRET_KEY = config("SECRET_KEY", default="BRUH-MOMENT")
