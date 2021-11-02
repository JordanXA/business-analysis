
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from secrets import dbusername, dbpassword, dburl

# don't edit this, if you need to use a local DB change the username, password, and url inside secrets.py 
databaseURL = f'mysql://{dbusername}:{dbpassword}@{dburl}/greenmotors'

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = databaseURL
db = SQLAlchemy(app)

class Models(db.Model):
    # may need to double check the primary key stuff
    id = db.Column('modelNum', db.Integer, primary_key = True)
    modelName = db.Column(db.String(10))
    # unsure if Numeric is a valid data type
    modelCost = db.Column(db.Numeric(7,2))

class Colors(db.Model):
    id = db.Column('colorNum', db.Integer, primary_key = True)
    colorCombo = db.Column(db.String(30))
    colorCost = db.Column(db.Numeric(6,2))

class Wheels(db.Model):
    id = db.Column('wheelNum', db.Integer, primary_key = True)
    wheelType = db.Column(db.String(10))
    wheelCost = db.Column(db.Numeric(6,2))

def __init__(self, modelName, modelCost, colorCombo, colorCost, wheelType, wheelCost):
    self.modelName = modelName
    self.modelCost = modelCost
    self.colorCombo = colorCombo
    self.colorCost = colorCost
    self.wheelType = wheelType
    self.wheelCost = wheelCost

#db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buy')
def buy():
    # maybe rename, this is really more like models. It displays the motorcycle models
    # we want to add code here that accesses the list of models from the database
    # we can pass the list of models into render_template() and it will load them
    #motors = LOADFROMDB()
    return render_template('buy.html')#, motors)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/login')
def login():
    return render_template('login.html')

# GET endpoint for a model making page
# this page will also load the model information, and display a form that you can use to edit models
# creates a POST request on submit
# then the endpoint can also handle a POST request, and enter the updated stuff into the database
# alternatively, we could do this using proper REST/CRUD endpoints (fancy business words)
# where we make just endpoints like GET /api/motors, POST /api/motors to create, PUT /api/motors to edit, DELETE /api/motors to delete
# the first way is probably simpler in flask though

if __name__ == '__main__':
    # stuff to run when developing
    db.create_all()
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()