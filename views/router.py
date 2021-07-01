from flask import Blueprint, render_template, request, redirect, url_for
from views.interface import account_itf
from exts import app

router = Blueprint('router', __name__)


# 用于测试练习的页面 随便怎么搞都行
@router.route('/test')
def test():
    app.logger.info('get test page')
    return render_template('test.html')


@router.route('/')
def index():
    return render_template('index.html')

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
    # 登录
    if request.method == 'POST':
        # # Here is an advise to revise
        # login_method = request.form.get('method')
        # username = request.form.get('username')
        # password = request.form.get('password')
        # app.logger.warning('{} request login by {}'.format(username, login_method))
        # user = account_itf.login(login_method, username, password)
        user = account_itf.login('username', request.form.get('username'), request.form.get('password'))
        # if user['msg'] == 'successfully login!':
        #     return render_template('csrf.html', user = user )
        return render_template('csrf.html', user=user)
    return render_template('csrf.html')


@router.route('/httpHeader/')
def httpHeader():
    app.logger.info('get httpHeader page')
    return render_template('httpHeader.html')


@router.route('/contentTraverse/')
def contentTraverse():
    app.logger.info('get contentTraverse page')
    return render_template('contentTraverse.html')


@router.route('/sqlPush/')
def sqlPush():
    app.logger.info('get sqlPush page')
    return render_template('sqlPush.html')


@router.route('/fileDownload/')
def fileDownload():
    app.logger.info('get fileDownload page')
    return render_template('fileDownload.html')


@router.route('/fileUpload/')
def fileUpload():
    app.logger.info('get fileUpload page')
    return render_template('fileUpload.html')


@router.route('/diaryLoss/')
def diaryLoss():
    app.logger.info('get diaryLoss page')
    return render_template('diaryLoss.html')


@router.route('/penetration/')
def penetration():
    app.logger.info('get penetration page')
    return render_template('penetration.html')
