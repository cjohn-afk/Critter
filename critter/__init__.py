from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from db_models import Users, db, login
from flask_login import login_required, current_user, login_user, logout_user

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' ##DONT USE THIS IN PRODUCTION, JUST FOR TESTING

## SQL Configuration ##
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db' #for testing
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://USER@PATHTOSERVER'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
####

#Initialize db
db.init_app(app)

## Create Database File (for testing) ##
#@app.before_first_request
#def create_table():
#    db.create_all()
####

## Initialize Login ##
login.init_app(app)
login.login_view = 'login'
####

@app.route('/')
@login_required
def timeline():
	return render_template('timeline.html')

@app.route('/profile/<string:username>')
@login_required
def profile(username):
    return render_template('profile.html')

@app.route('/messages')
@login_required
def messages():
    return render_template('messages.html')

@app.route('/settings')
@login_required
def settings():
    return render_template('settings.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if current_user.is_authenticated:
            return redirect('/')
    
    if request.method == 'POST':
        email = request.form['email']
        user  = Users.query.filter_by(email = email).first()
        if user is not None and user.check_password(request.form['password']):
            login_user(user)
            return redirect('/')
        else:
            ## show "Either password incorrect or no user with email *PROVIDED EMIAL*" error message on login screen.
            pass

    return render_template('login.html')

@app.route('/signup')
def sign_up():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

#app.run() #for testing