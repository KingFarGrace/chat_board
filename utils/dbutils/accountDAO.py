#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from exts import db
from models import user


def register(username, password):
    result = select_user_by_name(username)
    if result is None:
        new_user = user.User(username=username, password=password, gender='空', age=0, email='空', signature='这个人很懒，什么也没有写~', icon_url='static/img/default_figure.ico')
        db.session.add(new_user)
        db.session.commit()
        return True
    else:
        return False


def login_by_username(username, password):
    result = select_user_by_name(username)
    if result is None:
        return -1
    elif result.password != password:
        return 0
    else:
        return 1


def login_by_uid(uid, password):
    result = select_user_by_uid(uid)
    if result is None:
        return -1
    elif result.password != password:
        return 0
    else:
        return 1


def select_user_by_name(username):
    result = user.User.query.filter(user.User.username == username).first()
    return result


def select_user_by_uid(uid):
    result = user.User.query.filter(user.User.uid == uid).first()
    return result


def update_username(uid, new_n):
    result = user.User.query.filter(user.User.uid == uid).first()
    if result is not None:
        result.username = new_n
        db.session.commit()
        return True
    else:
        return False


def update_password(uid, new_p):
    result = user.User.query.filter(user.User.uid == uid).first()
    if result is not None:
        result.password = new_p
        db.session.commit()
        return True
    else:
        return False


def update_gender(uid, new_g):
    result = user.User.query.filter(user.User.uid == uid).first()
    if result is not None:
        result.gender = new_g
        db.session.commit()
        return True
    else:
        return False


def update_age(uid, new_a):
    result = user.User.query.filter(user.User.uid == uid).first()
    if result is not None:
        result.age = new_a
        db.session.commit()
        return True
    else:
        return False        


def update_email(uid, new_em):
    result = user.User.query.filter(user.User.uid == uid).first()
    if result is not None:
        result.email = new_em
        db.session.commit()
        return True
    else:
        return False        


def update_signature(uid, new_s):
    result = user.User.query.filter(user.User.uid == uid).first()
    if result is not None:
        result.signature = new_s
        db.session.commit()
        return True
    else:
        return False                


def update_figure(uid, new_url):
    result = user.User.query.filter(user.User.uid == uid).first()
    if result is not None:
        result.icon_url = new_url
        db.session.commit()
        return True
    else:
        return False    

def update_money(uid, new_money):
    result = user.User.query.filter(user.User.uid == uid).first()
    if result is not None:
        result.money = new_money
        db.session.commit()
        return True
    else:
        return False    

def remove_user(uid):
    result = user.User.query.filter(user.User.uid == uid).first()
    db.session.delete(result)
    db.session.commit()