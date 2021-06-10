#!/usr/bin/python3
# -*- encoding: utf-8 -*-

from flask import Flask, render_template
from config import dbconfig
from exts import db

app = Flask(__name__)
app.config.from_object(dbconfig)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/myPage')
def myPage():
    return render_template('myPage.html')

@app.route('/textEdit')
def textEdit():
    return render_template('textEdit.html')

@app.route('/textView')
def textView():
    return render_template('textView.html')

if __name__ == '__main__':
    app.run(debug=True)