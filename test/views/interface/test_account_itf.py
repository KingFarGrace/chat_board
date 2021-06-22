from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils.dbutils import accountDAO
from views.interface import account_itf
from models import user
from exts import db
from config import dbconfig

class TestAccountInterface:

    select_test_result = user.User()

    def setup(self):
        app = Flask(__name__)
        app.config.from_object(dbconfig)
        db = SQLAlchemy()
        db.init_app(app)
        app.app_context().push()
        self.select_test_result = accountDAO.select_user_by_name('test')
        

    def test_register(self):
        assert account_itf.register('test', '123456') == 'fail to register, please change your username and try again.'


    def test_login(self):
        assert account_itf.login('uid', 0, '123456') == {'msg': 'no such user.', 'info' : None}
        assert account_itf.login('uid', 1, '1234567') == {'msg': 'wrong password.', 'info' : None}
        assert account_itf.login('uid', 1, '123456') == {'msg': 'succesfully login!', 'info' : self.select_test_result}
        assert account_itf.login('username', 'best', '123456') == {'msg': 'no such user.', 'info' : None}
        assert account_itf.login('username', 'test', '1234567') == {'msg': 'wrong password.', 'info' : None}
        assert account_itf.login('username', 'test', '123456') == {'msg': 'succesfully login!', 'info' : self.select_test_result}


    def test_change_figure(self):
        # 完成主要逻辑后测试
        assert True


    def test_change_username(self):
        assert account_itf.change_username(1, 'test', 'test1') == 'replicated username, please change and try again'
        assert account_itf.change_username(1, 'test', 'test') == 'success to change username'

    
    def test_change_pwd(self):
        assert account_itf.change_pwd(1, '123457', '123456') == 'wrong password.'
        assert account_itf.change_pwd(1, '123456', '123456') == 'success to change password'

    
    def test_update_info(self):
        assert account_itf.update_info(0, gender='空', age = 0, email='空', signature='这个人很懒，什么也没有写~') == 'failed to identify, please check your accout and try again.'
        assert account_itf.update_info(1, gender='空', age = 0, email='空', signature='这个人很懒，什么也没有写~') == 'success to update info.'