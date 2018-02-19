#!/usr/bin/python
# -*- coding: utf-8 -*-
import pymongo as pymongo
from flask import Flask
from flask_cors import CORS

uri = "mongodb://virtualizacion:rG1odSRKrtYDjtDAnk1YVfoax2Fn8MTs3NUJ7RnXf7g7w1HwCtMMWekoxiPTlOp7I3Hcwt21ZFhHEWMLsaIJ7g==@virtualizacion.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(uri)
pinterest_app = Flask(__name__)

CORS(pinterest_app)

from pinterest.endpoints import *