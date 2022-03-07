from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import db_models
from db_models import db

# GET data methods
def getUserLoginInfoByID(id):
	result = db.session.query(db_models.Users).filter(db_models.Users.id == id).first()

	if result is not None:
		info = {
			"id": result.id,
			"username": result.username,
			"email": result.email,
			"password_hash": result.password_hash
		}
		return info
	else:
		return None

# Returns dictionary with user login info
def getUserLoginInfoByUsername(username):
	result = db.session.query(db_models.Users).filter(db_models.Users.Username == username).first()
	
	if result is not None:
		info = {
			"id": result.id,
			"username": result.username,
			"email": result.email,
			"password_hash": result.password_hash
		}
		return info
	else:
		return None
	
# Returns dictionary with user profile info		
def getUserProfileInfoByID(id):
	result = db.session.query(db_models.User_Profiles).filter(db_models.User_Profiles.id == id).first()
	if result is not None:
		info = {
			"id": result.id,
			"username": result.username,
			"gender": result.gender,
			"bio": result.bio
			#"Avatar": result.Avatar
		}
		return info
	else:
		return None
	
# Returns dictionary with user profile info	
def getUserProfileInfoByUsername(username):
	result = db.session.query(db_models.User_Profiles).filter(db_models.User_Profiles.username == username).first()
	if result is not None:
		info = {
			"id": result.id,
			"username": result.username,
			"gender": result.gender,
			"bio": result.bio
			#"Avatar": result.Avatar
		}
		return info
	else:
		return None

# Returns a dictionary with post info
def getPostByPostID(id):
	result = db.session.query(db_models.Posts).filter(db_models.Posts.id == id).first()
	if result is not None:
		info = {
			"id": result.id,
			"uid": result.uid,
			"type": result.type,
			"text": result.text,
			"mid": result.mid,
			"time": result.time
		}
		return info
	else:
		return None

# Returns the *most recent* post by the user
def getPostByUserID(id):
	result = db.session.query(db_models.Posts).filter(db_models.Posts.uid == id).first()
	if result is not None:
		info = {
			"id": result.id,
			"uid": result.uid,
			"type": result.type,
			"text": result.text,
			"mid": result.mid,
			"time": result.time
		}
		return info
	else:
		return None

# Returns a list of all posts by the user
def getPostsByUserID(id):
	result = db.session.query(db_models.Posts).filter(db_models.Posts.uid == id).all()
	if result is not None:
		return result
	else:
		return None