from config import dbconfig, pdfconfilg
from config import logconfig
from exts import db, app
from views.router import router
from models import user
from flask_bootstrap import Bootstrap

app.register_blueprint(router)
app.config.from_object(dbconfig)
app.config.from_object(pdfconfilg)
db.init_app(app)
bootstrap = Bootstrap(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5100)
