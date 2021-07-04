#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from exts import db


class Admin(db.Model):
    __tablenname__ = 'admin'
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
