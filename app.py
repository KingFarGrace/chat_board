from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import dbconfig

app = Flask(__name__)
app.config.from_object(dbconfig)
db = SQLAlchemy(app)
db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

@app.route('/myPage')
def myPage():
    return render_template('myPage.html')

@app.route('/textEdit')
def textEdit():
    return render_template('textEdit.html')

@app.route('/textView')
def textView():
    return render_template('textView.html')

if __name__ == '__main__':
    app.run(debug=True)