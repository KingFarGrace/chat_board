DIALECT = 'mysql'
DRIVER = 'mysqldb'
# 配置自己的用户名和密码
<<<<<<< HEAD
USERNAME = 'myj'
PASSWORD = 'MYJ%DinnaMoyu2048'
=======
USERNAME = 'zkh'
PASSWORD = 'ZKH%KingFarGrace4096'
>>>>>>> 0636b3c96b6f0b09a6ddbe50ba97bef859cfee20
HOST = 'localhost'
PORT = '3306'
DATABASE = 'chat_board_sys'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format( DIALECT, 
                                                                        DRIVER, 
                                                                        USERNAME, 
                                                                        PASSWORD, 
                                                                        HOST, 
                                                                        PORT, 
                                                                        DATABASE)