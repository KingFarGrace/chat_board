from config import pdfconfilg
from utils.dbutils import updownload_tool
from flask import request, url_for, render_template, send_from_directory
import os

# 本地测试只用了一个index界面 所以之后根据前端安排再更改路由
# @app.route('/upload',methods=['GET','POST'])
def upload(file):
    if request.method == 'POST':
        file = request.files.get('pdf')
        if file and updownload_tool.allowed_file(file.filename):
            pdf_name = os.path.splitext(file.filename)[0]
            filename = pdf_name + updownload_tool.rand_str() + '.pdf'
            file.save(os.path.join(pdfconfilg.UPLOAD_FOLDER, filename))
            # 向数据库插入账号、pdf文件名、时间戳
            # new_user = user.Pdf_files(uid=,filename=filename,time=)
            # db.session.add(new_user)
            # return redirect(url_for('get_url'))
    # return render_template('')


# @app.route('/get_url')
# def get_url():
#     files = user.Pdf_files.query.filter_by(uid=,time=).first()
#     filename = files.filename
#     return filename


# @app.route('/download/<filename>')
def download(filename):
    return send_from_directory(os.path.join(pdfconfilg.UPLOAD_FOLDER), filename, as_attachment=True)