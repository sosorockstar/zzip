from flask import Flask, request
from flask_restful import Resource, Api, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)
db = SQLAlchemy(app)

parser = reqparse.RequestParser()
parser.add_argument('admin', type=bool, help='Use super manager mode', default=False)

