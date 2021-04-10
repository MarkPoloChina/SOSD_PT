# CPR MP FOR SOSD 2021 A.R.R.
from app import db
from datetime import datetime

class File(db.Model):
    __tablename__ = 'file'
    id = db.Column(db.Integer,primary_key=True)
    userId = db.Column(db.Integer)
    title = db.Column(db.String(120))
    path = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime,index=True,default=datetime.now)
    def __repr__(self):
        return '<file:{}>'.format(self.title)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    timestamp = db.Column(db.DateTime,index=True,default=datetime.now)
    def __repr__(self):
        return '<id:{}>'.format(self.id)