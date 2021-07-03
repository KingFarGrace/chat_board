#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from exts import db

class Attachment(db.Model):
    __tablename__ = 'attachment'
    filename = db.Column(db.String(255), primary_key=True, autoincrement=False)
    