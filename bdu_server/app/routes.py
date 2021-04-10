# CPR MP FOR SOSD 2021 A.R.R.
from flask import flash, redirect, url_for, request, jsonify, abort
from app import app, db, Config
from sqlalchemy import and_
from app.models import *
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
import os
app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')

@app.after_request
def cors(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp

@app.route('/bdu/test')
def test():
    return jsonify({'status': 200, 'message': 'test Ok - CPR MP 2021'})

@app.route('/bdu/upload',methods=['POST'])
def upload_receiver():
    file = request.files.getlist('files')
    for obj in file:
        obj.save(os.path.join(app.config['UPLOAD_PATH'], obj.filename))
    return jsonify({'status': 200, 'message': 'test Ok - CPR MP 2021'})