from config import dbconfig, pdfconfilg
# 注释掉该行import语句，即可关闭日志功能
# from config import logconfig
from exts import db, app
from views.router import router
from models import user, attachment
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CsrfProtect

app.register_blueprint(router)
app.config.from_object(dbconfig)
app.config.from_object(pdfconfilg)
app.config["SECRET_KEY"] = '79537d00f4834892986f09a100aa1edf'
db.init_app(app)
bootstrap = Bootstrap(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # csrf保护，所有表单前添加 <input type="hidden" name="csrf_token" value="{{ csrf_token() }}"> 即可
    # CsrfProtect(app)
    app.run(debug=True, port=4500)
