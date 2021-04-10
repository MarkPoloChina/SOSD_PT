from flask import Flask
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.from_object(Config)
#建立数据库关系
db = SQLAlchemy(app)
#绑定app和数据库，以便进行操作
migrate = Migrate(app,db)

from app import routes,models