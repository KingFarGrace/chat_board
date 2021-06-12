#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from exts import db
from models import user


def register(username, password):
    result = select_user_by_name(username)
    if result is None:
        new_user = user.User(username=username, password=password, gender='空', age=0, email='空', signature='这个人很懒，什么也没有写~')
        db.session.add(new_user)
        db.session.commit()
        return True
    else:
        return False


def select_user_by_name(username):
    result = user.User.query.filter(user.User.username == username).one()
    return result