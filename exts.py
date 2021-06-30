#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
db = SQLAlchemy()
