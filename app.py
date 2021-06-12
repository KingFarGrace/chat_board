#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from flask import Flask, render_template
from config import dbconfig
from exts import db
from views.router import router
from models import user

app = Flask(__name__)
app.register_blueprint(router)
app.config.from_object(dbconfig)
db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)