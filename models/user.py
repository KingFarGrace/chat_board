#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from exts import db

class User(db.Model):
    __tablenname__ = 'user'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    signature = db.Column(db.String(255), nullable=False)
    icon_url = db.Column(db.String(255), nullable=False)