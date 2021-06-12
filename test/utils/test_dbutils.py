from utils import dbutils
from models import user
from exts import db


class TestDBUtils:

    def test_register(self):
        assert dbutils.register('test', '123456') == True


    def test_select_user_by_name(self):
        assert dbutils.select_user_by_name('test') == user.User(username='test', password='123456', gender='空', age=0, email='空', signature='这个人很懒，什么也没有写~')