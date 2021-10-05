
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from secrets import dbusername, dbpassword, dburl

# don't edit this, if you need to use a local DB change the username, password, and url inside secrets.py 
databaseURL = f'mysql://{dbusername}:{dbpassword}@{dburl}/greenmotors'

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = databaseURL
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buy')
def buy():
    return render_template('buy.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')


if __name__ == '__main__':
    db.create_all()
    app.run()