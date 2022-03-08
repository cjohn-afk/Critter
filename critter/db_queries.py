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
	result = db.session.query(db_models.User_Profiles).filter(db_models.User_Profiles.UserID == id).first()
	if result is not None:
		info = {
			"UserID": result.UserID,
			"Username": result.Username,
			"Gender": result.Gender,
			"Bio": result.Bio
			#"Avatar": result.Avatar
		}
		return info
	else:
		return None
	
# Returns dictionary with user profile info	
def getUserProfileInfoByUsername(username):
	result = db.session.query(db_models.User_Profiles).filter(db_models.User_Profiles.Username == username).first()
	if result is not None:
		info = {
			"UserID": result.UserID,
			"Username": result.Username,
			"Gender": result.Gender,
			"Bio": result.Bio
			#"Avatar": result.Avatar
		}
		return info
	else:
		return None

# Returns a dictionary with post info
def getPostByPostID(id):
	result = db.session.query(db_models.Posts).filter(db_models.Posts.PostID == id).first()
	if result is not None:
		info = {
			"PostID": result.PostID,
			"UserID": result.UserID,
			"PostType": result.PostType,
			"Text": result.Text,
			"MediaID": result.MediaID,
			"PostTime": result.PostTime
		}
		return info
	else:
		return None

# Returns the *most recent* post by the user
def getPostByUserID(id):
	result = db.session.query(db_models.Posts).filter(db_models.Posts.UserID == id).first()
	if result is not None:
		info = {
			"PostID": result.PostID,
			"UserID": result.UserID,
			"PostType": result.PostType,
			"Text": result.Text,
			"MediaID": result.MediaID,
			"PostTime": result.PostTime
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
		
def insertUser(username, email, password_hash, gender, bio, avatar):
	user = db_models.Users(Username=username, Email=email, Password=password_hash)
	user_profile = db_models.User_Profiles(Username=username, Gender=gender, Bio=bio, Avatar=avatar)
	db.session.add(user)
	db.session.add(user_profile)
	db.session.commit()
	
	return username
	
def insertPost(userid, post_type, text, mediaid, post_time):
	post = db_models.Posts(UserID=userid, PostType=post_type, Text=text, MediaID=mediaid, PostTime=post_time)
	db.session.add(post)
	db.session.commit()
	
	return text