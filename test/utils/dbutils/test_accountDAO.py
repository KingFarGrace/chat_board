from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import dbconfig
from models import user
from utils.dbutils import accountDAO


class TestAccountDAO:
    select_test_result = user.User()

    def setup(self):
        app = Flask(__name__)
        app.config.from_object(dbconfig)
        db = SQLAlchemy()
        db.init_app(app)
        app.app_context().push()

        self.select_test_result = accountDAO.select_user_by_name('test')

    def test_register(self):
        assert accountDAO.register('test', '123456') is False

    def test_login_by_username(self):
        assert accountDAO.login_by_username('best', '123456') == -1
        assert accountDAO.login_by_username('test', '1234567') == 0
        assert accountDAO.login_by_username('test', '123456') == 1

    def test_login_by_uid(self):
        assert accountDAO.login_by_uid(0, '123456') == -1
        assert accountDAO.login_by_uid(1, '1234567') == 0
        assert accountDAO.login_by_uid(1, '123456') == 1

    def test_select_user_by_name(self):
        assert accountDAO.select_user_by_name('test') == self.select_test_result

    def test_selece_user_by_uid(self):
        assert accountDAO.select_user_by_uid(1) == self.select_test_result

    def test_update_username(self):
        assert accountDAO.update_username(1, 'test') is True
        assert accountDAO.update_username(0, 'test') is False

    def test_update_gender(self):
        assert accountDAO.update_gender(1, '空') is True
        assert accountDAO.update_gender(0, '空') is False
