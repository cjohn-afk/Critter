import re
from flask import Flask, redirect, render_template, request, flash, get_flashed_messages, url_for, abort, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user, login_url, login_user, logout_user
from db_models import Post_Types, User_Profiles, Users, db, login
import db_queries
from jinja2 import Undefined

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' ##DONT USE THIS IN PRODUCTION, JUST FOR TESTING

## SQL Configuration ##
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testing.db' #for testing
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@127.0.0.1/Critter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
####

#Initialize db
db.init_app(app)

## Create Database File (for testing) ##
@app.before_first_request
def create_table():
    db.create_all()
####

## Initialize Login ##
login.init_app(app)
login.login_view = 'login'
####

@app.route('/', methods = ['POST', 'GET'])
@login_required
def timeline():
    if request.method == 'POST' and request.form['text'] is not None:
        db_queries.insertPost(current_user.get_id(), 'text', request.form['text'], None)
        
    posts = db_queries.getPostsByUserID(1) # TODO: Make method to return n latest posts from self and all followed accounts.
    return render_template('timeline.html', posts=posts)

@app.route('/profile/<string:username>', defaults={'username': None})
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
    login_failed = False
    if current_user.is_authenticated:
            return redirect(url_for('timeline'))
    
    if request.method == 'POST':
        email = request.form['email']
        user  = Users.query.filter_by(Email = email).first()
        remember_state = request.form['remember'] == "true"

        if user is not None and user.check_password(request.form['password']):
            login_user(user, remember=remember_state)
            return redirect(url_for('timeline'))
        else:
            #show "Either password incorrect or no user with email *PROVIDED EMIAL*" error message on login screen.
            login_failed = True
            pass

    return render_template('login.html', login_failed=login_failed)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/signup')
def sign_up():
    return render_template('signup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/API/like', methods = ['POST'])
def like():
    if request.method == 'POST':
        like = db_queries.getSpecificLike(current_user.get_id(), request.json['id'])
        if like is None:
            if db_queries.insertLike(current_user.get_id(), request.json['id']) is not None: result = "ADDED"
        else:
            if db_queries.deleteLike(current_user.get_id(), request.json['id']) is not None: result = "DELETED"
        if result is not None:
            return result
        else:
            abort(409)
    abort(400)

@app.route('/API/post', methods = ['POST'])
def post():
    if request.method == 'POST':
        if request.json.get('text') is not None:
            db_queries.insertPost(current_user.get_id(), 'text', request.json['text'], None)
            return "ADDED"
        elif request.json.get('id') is not None:
            post = db_queries.getPostByPostID(request.json['id'])
            if post.UserID == current_user.get_id():
                db_queries.deletePost(request.json['id'])
                return "DELETED"
            else:
                abort(403)
    abort(400)

app.run() #for testing