DIALECT = 'mysql'
DRIVER = 'mysqldb'
# 配置自己的用户名和密码
USERNAME = 'zkh'
PASSWORD = 'ZKH%KingFarGrace4096'
HOST = '121.196.40.74'
PORT = '3306'
DATABASE = 'chat_board_sys'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format( DIALECT, 
                                                                        DRIVER, 
                                                                        USERNAME, 
                                                                        PASSWORD, 
                                                                        HOST, 
                                                                        PORT, 
                                                                        DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True
