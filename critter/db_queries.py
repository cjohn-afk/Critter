from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import db_models
from db_models import db

# GET data methods
def getUserLoginInfoByID(id):
	return db.session.query(db_models.Users).filter(db_models.Users.id == id).first()

# Returns dictionary with user login info
def getUserLoginInfoByUsername(username):
	return db.session.query(db_models.Users).filter(db_models.Users.Username == username).first()
	
# Returns dictionary with user profile info		
def getUserProfileInfoByID(id):
	return db.session.query(db_models.User_Profiles).filter(db_models.User_Profiles.UserID == id).first()
	
# Returns dictionary with user profile info	
def getUserProfileInfoByUsername(username):
	return db.session.query(db_models.User_Profiles).filter(db_models.User_Profiles.Username == username).first()

# Returns a dictionary with post info
def getPostByPostID(id):
	return db.session.query(db_models.Posts).filter(db_models.Posts.PostID == id).first()

# Returns the *most recent* post by the user
def getPostByUserID(id):
	return db.session.query(db_models.Posts).filter(db_models.Posts.UserID == id).first()

# Returns a list of all posts by the user
def getPostsByUserID(id, n=50):
	return db.session.query(db_models.Posts).filter(db_models.Posts.uid == id).limit(n).all()

# Inserts a user into the database. NOTE: avater must be a bytes-like object.
def insertUser(username, email, password, gender, bio, avatar):
	user = db_models.Users(Username=username, Email=email)
	user.set_password(password)
	user_profile = db_models.User_Profiles(Username=username, Gender=gender, Bio=bio, Avatar=avatar)
	db.session.add(user)
	db.session.add(user_profile)
	db.session.commit()
	# TODO: HANDLE POTENTIAL ERRORS CAUSED BY SESSION.COMMIT()

# Inserts a post into the database.
def insertPost(userid, post_type, text, mediaid, post_time):
	post = db_models.Posts(UserID=userid, PostType=post_type, Text=text, MediaID=mediaid, PostTime=post_time)
	db.session.add(post)
	db.session.commit()
	# TODO: HANDLE POTENTIAL ERRORS CAUSED BY SESSION.COMMIT()