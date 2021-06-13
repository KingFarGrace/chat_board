from utils.dbutils import accountDAO


def register(username, password):
    if accountDAO.register(username, password) is True:
        return 'successfully register!'
    else:
        return 'fail to register, please change your username and try again.'


def login(method, key, password):
    if method == 'uid':
        code = accountDAO.login_by_uid(key, password)
        if code == -1:
            user = {'msg': 'no such user.', 'info' : None}
        elif code == 0:
            user = {'msg': 'wrong password.', 'info' : None}
        else:
            info = accountDAO.select_user_by_uid(key)
            user = {'msg': 'succesfully login!', 'info' : info}
    
    if method == 'username':
        code = accountDAO.login_by_username(key, password)
        if code == -1:
            user = {'msg': 'no such user.', 'info' : None}
        elif code == 0:
            user = {'msg': 'wrong password.', 'info' : None}
        else:
            info = accountDAO.select_user_by_name(key)
            user = {'msg': 'succesfully login!', 'info' : info}
    
    return user