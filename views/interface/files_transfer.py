from flask import Flask, app, request, url_for, send_from_directory
import os

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['pdf'])
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 10
app.config['UPLOAD_FOLDER'] = 'pdf_files'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def upload(file):
    if request.method == 'POST':
        file = request.files.get('pdf')
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            url_for('download',filename=filename)


def download(filename):
    return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER']), filename, as_attachment=True)