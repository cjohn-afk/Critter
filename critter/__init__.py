from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pyodbc

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@127.0.0.1/Critter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from critter import db_queries

@app.route('/')
def root_dir():
	#return "<p> test </p>"
    return "<b>" + db_queries.getPostByUserID(2)["Text"] + "</b>"

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/home/')
def timeline():
    return render_template('timeline.html')

@app.route('/signup/')
def sign_up():
    return render_template('signup.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/messages/')
def messages():
    return render_template('messages.html')

@app.route('/profile/<string:username>')
def profile(username):
    return render_template('profile.html')

@app.route('/settings/')
def settings():
    return render_template('settings.html')
