from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import dbconfig

app = Flask(__name__)
app.config.from_object(dbconfig)
db = SQLAlchemy(app)
db.create_all()

@app.route('/')
def index():
    return '<h1>Index</h1>'

if __name__ == '__main__':
    app.run(debug=True)