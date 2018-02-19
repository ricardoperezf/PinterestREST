#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS

pinterest_app = Flask(__name__)

CORS(pinterest_app)

from pinterest.endpoints import *
