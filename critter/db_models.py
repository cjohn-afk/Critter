from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import backref

from critter import db

# Manage tables

class Users(db.Model):

	__tablename__ = "Users"

	UserID = db.Column(db.Integer, primary_key = True)
	Username = db.Column(db.String)
	Email = db.Column(db.String)
	Password = db.Column(db.String)
	
	# Create the relationship between Users and User_Profiles
	user_profiles = db.relationship('User_Profiles', backref='users', uselist=False)

	
	def __init__(self, UserID, Username, Email, Password):
		self.UserID = UserID
		self.Username = Username
		self.Email = Email
		self.Password = Password
		
class User_Profiles(db.Model):

	__tablename__ = "User_Profiles"
	
	UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'), primary_key = True)
	Username = db.Column(db.String)
	Gender = db.Column(db.String)
	Bio = db.Column (db.String)
	Avatar = db.Column(db.LargeBinary)
	
	# Create relationships
	#posts = db.relationship('Posts', backref='user_profiles')
	# #follows = relationship('Follows', backref='user_profiles')
	# #likes = relationship('Likes', backref='user_profiles')
	
	def __init__(self, UserID, Username, Gender, Bio, Avatar):
		self.UserID = UserID
		self.Username = Username
		Self.Gender = Gender
		self.Bio = Bio
		self.Avatar = Avatar

class Media(db.Model):
	
	__tablename__ = 'Media'
	
	MediaID = db.Column(db.Integer, primary_key = True)
	URI = db.Column(db.String)
	
	# Create Relationships
	posts = db.relationship('Posts', backref='media')
	
	def __init__(self, MediaID, URI):
		self.MediaID = MediaID
		self.URI = URI

class Post_Types(db.Model):

	__tablename__ = 'Post_Types'
	
	TypeID = db.Column(db.Integer, primary_key = True)
	URI = db.Column(db.String)
	
	# Create relationships
	posts = db.relationship('Posts', backref='types')
	
	def __init__(self, TypeID, URI):
		self.TypeID = TypeID
		self.URI = URI

class Posts(db.Model):
	
	__tablename__ = 'Posts'
	
	PostID = db.Column(db.Integer, primary_key = True)
	UserID = db.Column(db.Integer, db.ForeignKey(User_Profiles.UserID))
	PostType = db.Column(db.Integer, db.ForeignKey(Post_Types.TypeID))
	Text = db.Column(db.String)
	MediaID = db.Column(db.Integer, db.ForeignKey(Media.MediaID))
	PostTime = db.Column(db.DateTime)
	
	# Create relationships
	likes = db.relationship('Likes', backref='postslikes')
	
	def __init__(self, PostID, UserID, PostType, Text, MediaID, PostTime):
		self.PostID = PostID
		self.UserID = UserID
		self.PostType = PostType
		self.Text = Text
		self.MediaID = MediaID
		self.PostTime = PostTime
		
class Likes(db.Model):
	
	__tablename__ = 'Likes'
	
	LikeID = db.Column(db.Integer, primary_key = True)
	UserID = db.Column(db.Integer, db.ForeignKey(User_Profiles.UserID))
	PostID = db.Column (db.Integer, db.ForeignKey(Posts.PostID))
	
	def __init__(self, LikeID, UserID, PostID):
		self.LikeID = LikeID
		self.UserID = UserID
		self.PostID = PostID
		
class Follows(db.Model):

	__tablename__ = 'Follows'
	
	RelationshipID = db.Column(db.Integer, primary_key = True)
	UserID = db.Column(db.Integer, db.ForeignKey(User_Profiles.UserID))
	FollowingID = Column(db.Integer, db.ForeignKey(User_Profiles.UserID))
	
	def __init__(self, RelationshipID, UserID, FollowingID):
		self.RelationshipID = RelationshipID
		self.UserID = UserID
		self.FollowingID = FollowingID



