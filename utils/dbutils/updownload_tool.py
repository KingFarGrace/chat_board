from config import pdfconfilg


# 判断是否是允许的文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in pdfconfilg.ALLOWED_EXTENSIONS


# 生成随机数向pdf文件名填充 保证文件名的唯一性 便于download
def rand_str(length=10):
    import random
    base_str = 'abcdefghijklmnopqrstuvwxyz1234567890'
    return ''.join(random.choice(base_str) for i in
                   range(length))
