from exts import app
from utils.dbutils import accountDAO


def register(username, password):
    if accountDAO.register(username, password) is True:
        app.logger.info('Success to register. new user: {}'.format(username))
        return 'Successfully register!'
    else:
        app.logger.error('Failed to register with username: {}'.format(username))
        return 'Fail to register, please change your username and try again.'


def login(method, key, password):
    user = None
    if method == 'uid':
        code = accountDAO.login_by_uid(key, password)
        if code == -1:
            app.logger.error('Failed to login by {}, no such user.'.format(key))
            user = {'msg': 'no such user.', 'info': None}
        elif code == 0:
            app.logger.error('Failed to login by {}, wrong password.'.format(key))
            user = {'msg': 'wrong password.', 'info': None}
        else:
            info = accountDAO.select_user_by_uid(key)
            app.logger.info('Login successfully')
            user = {'msg': 'successfully login!', 'info': info}

    if method == 'username':
        code = accountDAO.login_by_username(key, password)
        if code == -1:
            app.logger.error('Failed to login by {}, no such user.'.format(key))
            user = {'msg': 'no such user.', 'info': None}
        elif code == 0:
            app.logger.error('Failed to login by {}, wrong password.'.format(key))
            user = {'msg': 'wrong password.', 'info': None}
        else:
            info = accountDAO.select_user_by_name(key)
            app.logger.info('Login successfully')
            user = {'msg': 'successfully login!', 'info': info}
    return user


def change_figure():
    # 更换头像接口
    pass


def change_username(uid, old_name, new_name):
    if accountDAO.select_user_by_name(new_name) is not None and new_name != old_name:
        return 'replicated username, please change and try again'
    else:
        if accountDAO.update_username(uid, new_name) is True:
            return 'success to change username'
        else:
            return 'failed to identify, please check your account and try again.'


def change_pwd(uid, old_pwd, new_pwd):
    result = accountDAO.select_user_by_uid(uid)
    if result.password == old_pwd:
        if accountDAO.update_password(uid, new_pwd) is True:
            return 'success to change password'
        else:
            return 'failed to identify, please check your account and try again.'
    else:
        return 'wrong password.'


def update_info(uid, **kwargs):
    if (accountDAO.update_gender(uid, kwargs['gender']) and
            accountDAO.update_age(uid, kwargs['age']) and
            accountDAO.update_email(uid, kwargs['email']) and
            accountDAO.update_signature(uid, kwargs['signature'])) is False:
        return 'failed to identify, please check your account and try again.'
    else:
        return 'success to update info.'


def updata_money(uid, new_money):
    result = accountDAO.select_user_by_uid(uid)
    if accountDAO.update_money(uid, new_money) is True:
        return 'success to change money'
    else:
        return 'failed to identify, please check your account and try again.'


def is_admin(username):
    uid = accountDAO.get_uid_by_username(username)
    return accountDAO.check_admin_id(uid)
