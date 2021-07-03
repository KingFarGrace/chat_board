from logging import info
from flask import Blueprint, render_template, request, redirect, url_for, make_response, send_from_directory
from views.interface import account_itf
from utils.dbutils import accountDAO
from exts import app
from config import pdfconfilg
from utils.dbutils import updownload_tool
import os
from exts import db
from models import attachment

router = Blueprint('router', __name__)


# 用于测试练习的页面 随便怎么搞都行
@router.route('/test')
def test():
    app.logger.info('get test page')
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

# @router.route('/login/')
# def login():
#     return render_template('login.html')

# @router.route('/register/')
# def register():
#     return render_template('register.html')

# @router.route('/myPage/')
# def myPage():
#     return render_template('myPage.html')

# @router.route('/textEdit/')
# def textEdit():
#     return render_template('textEdit.html')

# @router.route('/textView/')
# def textView():
#     return render_template('textView.html')


@router.route('/xss/', methods=['POST', 'GET'])
def xss():
    app.logger.info('get xss page')
    # 发送POST请求更改内容
    if request.method == 'POST':
        search_content = request.form.get('searchContent')
        app.logger.warning('form value:{}'.format(search_content))
        return render_template('xss.html', searchContent=search_content)
    return render_template('xss.html')


@router.route('/csrf/', methods=['POST', 'GET'])
def csrf():
    app.logger.info('get csrf page')
    cookie = request.cookies.get("username")
    user = None
    if cookie != None:
        user = accountDAO.select_user_by_name(cookie)
    # POST转账请求
    if request.method == 'POST':
        touser = request.form.get('touser')
        money = request.form.get('money')
        user = accountDAO.select_user_by_name(cookie)
        uid = user.uid
        new_money = user.money - int(money)
        print(account_itf.updata_money(uid, new_money=new_money))
        return '{}转账{}元到{}成功！'.format(cookie ,money, touser)
    return render_template('csrf.html', user=user)


@router.route('/httpHeader/')
def httpHeader():
    app.logger.info('get httpHeader page')
    return render_template('httpHeader.html')


@router.route('/contentTraverse/')
def contentTraverse():
    app.logger.info('get contentTraverse page')
    return render_template('contentTraverse.html')


@router.route('/sqlPush/',methods=['GET','POST'])
def sqlPush():
    app.logger.info('get sqlPush page')
    if request.method == 'POST':
        id = request.form.get('id')
        pwd = request.form.get('pwd')
        select_sql = "select * from user where uid=" + id + " and password='" + pwd + "'"
        result = db.session.execute(select_sql).fetchall()
        if result != []:
            return redirect(url_for('router.index'))
    return render_template('sqlPush.html')


@router.route('/fileUpload/',methods=['GET','POST'])
def fileUpload():
    app.logger.info('get fileUpload page')
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
    return render_template('fileUpload.html')


@router.route('/fileDownload/')
def fileDownload():
    files = attachment.Attachment.query.all()
    return render_template('fileDownload.html',files=files)


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
    app.logger.info('get diaryLoss page')
    return render_template('diaryLoss.html')


@router.route('/penetration/')
def penetration():
    app.logger.info('get penetration page')
    return render_template('penetration.html')
