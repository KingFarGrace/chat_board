# -*- encoding: utf-8 -*-

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'Root%132546'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'chat_board_sys'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf-8".format(DIALECT, 
                                                                        DRIVER, 
                                                                        USERNAME, 
                                                                        PASSWORD, 
                                                                        HOST, 
                                                                        PORT, 
                                                                        DATABASE)