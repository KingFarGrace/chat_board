#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from flask import Blueprint, render_template

router = Blueprint('router', __name__)

@router.route('/')
def index():
    return render_template('index.html')

@router.route('/login')
def login():
    return render_template('login.html')

@router.route('/register')
def register():
    return render_template('register.html')

@router.route('/myPage')
def myPage():
    return render_template('myPage.html')

@router.route('/textEdit')
def textEdit():
    return render_template('textEdit.html')

@router.route('/textView')
def textView():
    return render_template('textView.html')