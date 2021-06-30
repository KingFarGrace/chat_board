from flask import Blueprint, render_template, request, redirect, url_for
from views.interface import account_itf

router = Blueprint('router', __name__)

#用于测试练习的页面 随便怎么搞都行
@router.route('/test')
def test():
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

@router.route('/xss/', methods=['POST','GET'])
def xss():
    # 发送POST请求更改内容
    if request.method == 'POST':
        return render_template('xss.html', searchContent = request.form.get('searchContent'))
    return render_template('xss.html')

@router.route('/csrf/', methods=['POST','GET'])
def csrf():
    # 登录
    if request.method == 'POST':
        user = account_itf.login('username', request.form.get('username'), request.form.get('password'))
        # if user['msg'] == 'succesfully login!':
        #     return render_template('csrf.html', user = user )
        return render_template('csrf.html', user = user)
    return render_template('csrf.html')

@router.route('/httpHeader/')
def httpHeader():
    return render_template('httpHeader.html')

@router.route('/contentTraverse/')
def contentTraverse():
    return render_template('contentTraverse.html')

@router.route('/sqlPush/')
def sqlPush():
    return render_template('sqlPush.html')

@router.route('/fileDownload/')
def fileDownload():
    return render_template('fileDownload.html')

@router.route('/fileUpload/')
def fileUpload():
    return render_template('fileUpload.html')

@router.route('/diaryLoss/')
def diaryLoss():
    return render_template('diaryLoss.html')

@router.route('/penetration/')
def penetration():
    return render_template('penetration.html')