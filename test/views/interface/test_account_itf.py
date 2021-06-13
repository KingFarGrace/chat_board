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
        assert account_itf.login('uid', '0', '123456') == {'msg': 'no such user.', 'info' : None}
        assert account_itf.login('uid', '1', '1234567') == {'msg': 'wrong password.', 'info' : None}
        assert account_itf.login('uid', '1', '123456') == {'msg': 'succesfully login!', 'info' : self.select_test_result}
        assert account_itf.login('username', 'best', '123456') == {'msg': 'no such user.', 'info' : None}
        assert account_itf.login('username', 'test', '1234567') == {'msg': 'wrong password.', 'info' : None}
        assert account_itf.login('username', 'test', '123456') == {'msg': 'succesfully login!', 'info' : self.select_test_result}
