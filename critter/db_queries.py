from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import backref

from critter import db
from critter import db_models as model




# GET data methods
def getUserLoginInfoByID(id):
	result = db.session.query(model.Users).filter(model.Users.UserID == id).first()
	if result is not None:
		return result.Username
	else:
		return "-1"

# Returns dictionary with user login info
def getUserLoginInfoByUsername(username):
	result = db.session.query(model.Users).filter(model.Users.Username == username).first()
	
	if result is not None:
		info = {
			"UserID": result.UserID,
			"Username": result.Username,
			"Email": result.Email,
			"Password": result.Password
		}
		return info
	else:
		return "-1"
	
# Returns dictionary with user profile info		
def getUserProfileInfoByID(id):
	result = db.session.query(model.User_Profiles).filter(model.User_Profiles.UserID == id).first()
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
		return "-1"
	
# Returns dictionary with user profile info	
def getUserProfileInfoByUsername(username):
	result = db.session.query(model.User_Profiles).filter(model.User_Profiles.Username == username).first()
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
		return "-1"

# Returns a dictionary with post info
def getPostByPostID(id):
	result = db.session.query(model.Posts).filter(model.Posts.PostID == id).first()
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
		info = {
			"PostID": "Not found",
			"UserID": "Not found",
			"PostType": "Not found",
			"Text": "Not found",
			"MediaID": "Not found",
			"PostTime": "Not found"
		}
		return info

# Returns the *most recent* post by the user
def getPostByUserID(id):
	result = db.session.query(model.Posts).filter(model.Posts.UserID == id).first()
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
		info = {
			"PostID": "Not found",
			"UserID": "Not found",
			"PostType": "Not found",
			"Text": "Not found",
			"MediaID": "Not found",
			"PostTime": "Not found"
		}
		return info

# Returns a list of all posts by the user
def getPostsByUserID(id):
	result = db.session.query(model.Posts).filter(model.Posts.UserID == id).all()
	if result is not None:
		return result
	else:
		info = {"None found"}
		return info