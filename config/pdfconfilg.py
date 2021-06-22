# 设置允许上传的文件后缀
ALLOWED_EXTENSIONS = set(['pdf'])
# 配置上传文件的最大尺寸10M
MAX_CONTENT_LENGTH = 1024 * 1024 * 10
# 配置上传文件的保存目录
UPLOAD_FOLDER = 'pdf_files'