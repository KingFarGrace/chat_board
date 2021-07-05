import os

from flask import Blueprint, render_template, request, redirect, url_for, make_response, send_from_directory

from config import pdfconfilg
from exts import app, db
from models import attachment
from utils import cryptoutil
from utils.dbutils import accountDAO
from utils.dbutils import updownload_tool
from views.interface import account_itf

router = Blueprint('router', __name__)


# 用于测试练习的页面 随便怎么搞都行
@router.route('/test')
def test():
    app.logger.info('GET test page')
    return render_template('test.html')


@router.route('/', methods=['POST', 'GET'])
def index():
    cookie = request.cookies.get("username")
    if request.method == 'POST':
        # 登录
        # login_method = request.form.get('method')
        login_method = 'username'
        username = request.form.get('username')
        password = request.form.get('password')
        app.logger.warning('{} request login by {}'.format(username, login_method))
        user = account_itf.login(login_method, username, password)
        if user['msg'] == 'successfully login!':
            # 设置cookie
            resp = make_response(render_template('index.html', username=username))
            resp.set_cookie("username", username)
            return resp
        return render_template('index.html', username=None)
    return render_template('index.html', username=cookie)


@router.route('/quit')
def quit():
    resp = make_response(render_template('index.html', username=None))
    resp.delete_cookie("username")
    return resp


@router.route('/xss/', methods=['POST', 'GET'])
def xss():
    app.logger.info('GET xss page')
    cookie = request.cookies.get("username")
    user = None
    if cookie is not None:
        user = accountDAO.select_user_by_name(cookie)
    # POST更新签名请求
    if request.method == 'POST':
        user = accountDAO.select_user_by_name(cookie)
        uid = user.uid
        new_signature = request.form.get('new_signature')
        print(account_itf.update_info(uid, gender=user.gender, age=user.age, email=user.email, signature=new_signature))
        return render_template('xss.html', user=user)
    return render_template('xss.html', user=user)


@router.route('/csrf/', methods=['POST', 'GET'])
def csrf():
    app.logger.info('GET csrf page')
    cookie = request.cookies.get("username")
    user = None
    if cookie is not None:
        user = accountDAO.select_user_by_name(cookie)
    # POST转账请求
    if request.method == 'POST':
        touser = request.form.get('touser')
        money = request.form.get('money')
        user = accountDAO.select_user_by_name(cookie)
        uid = user.uid
        new_money = user.money - int(money)
        print(account_itf.updata_money(uid, new_money=new_money))
        return '{}转账{}元到{}成功！'.format(cookie, money, touser)
    return render_template('csrf.html', user=user)


@router.route('/httpHeader/')
def httpHeader():
    app.logger.info('GET httpHeader page')
    return render_template('httpHeader.html')


@router.route('/contentTraverse/')
def contentTraverse():
    app.logger.info('GET contentTraverse page')
    return render_template('contentTraverse.html')


@router.route('/sqlPush/', methods=['GET', 'POST'])
def sqlPush():
    app.logger.info('get sqlPush page')
    if request.method == 'POST':
        id = request.form.get('id')
        pwd = request.form.get('pwd')
        select_sql = "select * from user where uid=" + id + " and password='" + pwd + "'"
        result = db.session.execute(select_sql).fetchall()
        if result:
            return redirect(url_for('router.index'))
    return render_template('sqlPush.html')


@router.route('/fileUpload/', methods=['GET', 'POST'])
def fileUpload():
    app.logger.info('GET fileUpload page')
    if request.method == 'POST':
        file = request.files.get('pdf')
        # 为防护文件上传漏洞而进行文件过滤 判断是否为符合pdf后缀的文件
        # if file and updownload_tool.allowed_file(file.filename):
        pdf_name = os.path.splitext(file.filename)[0]
        suffix = os.path.splitext(file.filename)[1]
        # 拼接文件名
        # filename = pdf_name + updownload_tool.rand_str() + '.pdf'
        filename = pdf_name + updownload_tool.rand_str() + suffix
        file.save(os.path.join(pdfconfilg.UPLOAD_FOLDER, filename))
        new_filename = attachment.Attachment(filename=filename)
        db.session.add(new_filename)
        db.session.commit()
        return redirect(url_for('router.fileDownload'))
    app.logger.info('GET sqlPush page')
    return render_template('sqlPush.html')


@router.route('/fileDownload/')
def fileDownload():
    app.logger.info('GET fileDownload page')
    files = attachment.Attachment.query.all()
    return render_template('fileDownload.html', files=files)


@router.route('/download/')
def download():
    if request.method == 'GET':
        filepath = request.args['filepath']
        # 切割出文件名称
        filename = filepath.split('/')[-1]
        # 文件路径重命名 -> 去掉文件名 获得路径
        filepath = filepath.replace(filename, '')
        return send_from_directory(os.path.join(filepath), filename, as_attachment=True)
        # 无漏洞的文件下载 后端拼接路径 前端获取文件名
        # filename = request.args['filename']
        # return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER']), filename, as_attachment=True)


@router.route('/diaryLoss/')
def diaryLoss():
    app.logger.info('GET diaryLoss page')
    return render_template('diaryLoss.html')


@router.route('/penetration/validate', methods=['GET', 'POST'])
def validate():
    """
    使用WTForm进行前端表单传输，后端使用views.form.register_form文件中RegisterForm类进行接收，
    并进行鉴权，格式检验等操作，避免用户设置了过于简单的密码导致被暴力破解。
    在注册环节限定用户密码为8-16位包含大小写字母和数字的串，若不满足，则不允许注册，从而避免身份验证漏洞。
    （缺陷系统中去掉了密码格式验证器）
    """
    app.logger.info('GET penetration page')
    # register_form = RegisterForm()
    # if request.method == 'POST':
    #     app.logger.warning('register form from /penetration/validate')
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     if register_form.validate_on_submit():
    #         app.logger.info('valid form')
    #         flash(account_itf.register(username, password))
    #     else:
    #         app.logger.error('invalid form')
    #         flash(register_form.errors)
    # return render_template('validate.html', form=register_form)
    #
    message = []
    if request.method == 'POST':
        app.logger.warning('register form from /penetration/validate')
        username = request.form.get('username')
        password = request.form.get('password')
        repwd = request.form.get('repwd')
        if username == '':
            message.append('用户名不能为空')
        elif password == '':
            message.append('密码不能为空')
        elif password != repwd:
            message.append('两次输入的密码不相同')
        else:
            app.logger.info('valid form')
            account_itf.register(username, password)
            message.append('注册成功')
    return render_template('validate.html', message=message)


@router.route('/penetration/ultravires')
def ultra_vires():
    app.logger.info('GET ultra vires page')
    user = None
    if request.method == 'GET':
        username = request.cookies.get('username')
        app.logger.warning('check {}\'s info'.format(username))
        user = accountDAO.select_user_by_name(username)
    return render_template('ultravires.html', user=user)


@router.route('/penetration/horizon', methods=['GET', 'POST'])
def horizon():
    app.logger.info('GET ultra vires horizon page')
    user = None
    if request.method == 'GET':
        username = request.args.get('username')
        # 此部分为后端鉴权逻辑，缺陷系统中不启用
        # owner = request.cookies.get('username')
        # if owner != username:
        #     app.logger.error('Unauthenticated request')
        # else:
        #     app.logger.warning('check {}\'s info'.format(username))
        #     user = accountDAO.select_user_by_name(username)
        app.logger.warning('check {}\'s info'.format(username))
        user = accountDAO.select_user_by_name(username)
    return render_template('horizon.html', user=user)


@router.route('/penetration/vertical', methods=['GET', 'POST'])
def vertical():
    app.logger.info('GET ultra vires vertical page')
    user = None
    if request.method == 'POST':
        username = request.form.get('username')
        app.logger.warning('check {}\'s info'.format(username))
        user = accountDAO.select_user_by_name(username)
    return render_template('vertical.html', user=user)


@router.route('/admin', methods=['GET', 'POST'])
def admin():
    # 此部分为后端鉴权逻辑，缺陷系统中不启用
    # username = request.cookies.get('username')
    # if account_itf.is_admin(username):
    #     app.logger.warning('GET admin page')
    #     if request.method == 'POST':
    #         uid = request.form.get('uid')
    #         app.logger.warning('delete user: {}'.format(uid))
    #         accountDAO.remove_user(uid)
    #     return render_template('admin.html')
    # else:
    #     app.logger.error('Unauthenticated request')
    #     return render_template('index.html')
    app.logger.warning('GET admin page')
    if request.method == 'POST':
        uid = request.form.get('uid')
        app.logger.warning('delete user: {}'.format(uid))
        accountDAO.remove_user(uid)
    return render_template('admin.html')


@router.route('/penetration/encrypt', methods=['GET', 'POST'])
def encrypt():
    """
    前后端加密传输，对照 router.index 页中的登录模块
    在该页面中，前端表单密码被加密后才传到后端，提高了安全性
    后端解密方法 decrypt() 见 utils.cryptoutil 模块
    前端使用jsencrypt库进行加密，公钥由后端提供
    """
    user = None
    with open('config/public_key.pem', 'r') as reader:
        public_key = reader.read()
    if request.method == 'GET':
        app.logger.info('GET encrypt page')
        return render_template('encrypt.html', user=user, public_key=public_key)
    if request.method == 'POST':
        login_method = 'username'
        username = request.form.get('username')
        password = request.form.get('password')
        app.logger.info('decrypt pwd: {}'.format(password))
        password = cryptoutil.decrypt(password)
        app.logger.warning('{} request login by {}'.format(username, login_method))
        user = account_itf.login(login_method, username, password.decode('utf-8'))
        return render_template('encrypt.html', user=user['info'], public_key=public_key)
