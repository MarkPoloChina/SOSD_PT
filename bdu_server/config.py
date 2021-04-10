import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/bdu?charset=utf8'
    SECRET_KEY = 'WANGCH8131'
    SQLALCHEMY_TRACK_MODIFICATIONS = False