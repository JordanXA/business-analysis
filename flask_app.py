
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
    # maybe rename, this is really more like models. It displays the motorcycle models
    # we want to add code here that accesses the list of models from the database
    # we can pass the list of models into render_template() and it will load them
    
    # using this while we don't have a real motorcycle class because flask doesn't care if its a real class
    class TempClass:
        def __init__(self, name, price):
            self.name = name
            self.price = price
    
    motors = []
    motors.append(TempClass("Lightning", 5123))
    motors.append(TempClass("Lightning II", 15123))

    wheels = []
    wheels.append(TempClass("Cool Wheel", 500))
    wheels.append(TempClass("Dumb Wheel", 1))

    colors = []
    colors.append(TempClass("Green", 0))
    colors.append(TempClass("Gold", 9999))

    return render_template('buy.html', motors=motors, wheels=wheels, colors=colors)

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