from queue import Empty
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import db_models
from db_models import db

from datetime import datetime
from time import time

# GET data methods
def getUserLoginInfoByID(id):
	return db.session.query(db_models.Users).filter(db_models.Users.id == id).first()

# Returns dictionary with user login info
def getUserLoginInfoByUsername(username):
	return db.session.query(db_models.Users).filter(db_models.Users.Username == username).first()

# Returns dictionary with user login info
def getUserLoginInfoByEmail(email):
	return db.session.query(db_models.Users).filter(db_models.Users.Email == email).first()

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
	return db.session.query(db_models.Posts).filter(db_models.Posts.UserID == id).order_by(db_models.Posts.PostTime.desc()).limit(n).all()

# Returns a list of all userIDs whom like a given post
def getLikesByPostID(id):
	return db.session.query(db_models.Likes).filter(db_models.Likes.PostID == id).all()

def getSpecificLike(userID, postID):
	return db.session.query(db_models.Likes).filter(db_models.Likes.UserID == userID, db_models.Likes.PostID == postID).first()

def insertFollow(userID, followingID):
	follow = db_models.Follows(UserID = userID, FollowingID = followingID)
	print(follow.__dict__)
	db.session.add(follow)
	db.session.commit()

# Inserts a like int the database.
def insertLike(userID, postID):
	if getSpecificLike(userID, postID) is None:
		like = db_models.Likes(UserID = userID, PostID = postID)
		db.session.add(like)
		db.session.commit()
		return like.LikeID
	return None

# Deletes a like from the database.
def deleteLike(userID, postID):
	likeQuery = db.session.query(db_models.Likes).filter(db_models.Likes.UserID == userID, db_models.Likes.PostID == postID)
	if likeQuery.all() is not None:
		likeID = likeQuery.first().LikeID
		likeQuery.delete()
		db.session.commit()
		return likeID
	return None

# Inserts a user into the database. NOTE: avatar must be a bytes-like object.
def insertUser(username, email, password, gender, bio, avatar):
	user = db_models.Users(Username=username, Email=email)
	user.set_password(password)
	user_profile = db_models.User_Profiles(Username=username, Gender=gender, Bio=bio, Avatar=avatar)
	db.session.add(user)
	db.session.add(user_profile)
	db.session.commit()
	# TODO: HANDLE POTENTIAL ERRORS CAUSED BY SESSION.COMMIT()

# Inserts a post into the database.
def insertPost(userid, post_type, text, mediaid):
	post = db_models.Posts(UserID=userid, PostType=post_type, Text=text, MediaID=mediaid, PostTime=datetime.fromtimestamp(time()))
	db.session.add(post)
	db.session.commit()
	# TODO: HANDLE POTENTIAL ERRORS CAUSED BY SESSION.COMMIT()

def deletePost(postID):
	post = db.session.query(db_models.Posts).filter(db_models.Posts.PostID == postID)
	likes = db.session.query(db_models.Likes).filter(db_models.Likes.PostID == postID)
	post.delete()
	likes.delete()
	db.session.commit()

def getFollowedIDs(userID):
	follows = db.session.query(db_models.Follows).filter(db_models.Follows.UserID == userID).all()
	result=[]
	for f in follows:
		result.append(f.FollowingID)
	return result

def getUsernamesByID(ids=[]):
	results = {}

	for id in ids:
		profile = getUserProfileInfoByID(id)
		if profile is not None:
			results[id] = { "username": profile.Username, "avatar": profile.Avatar }
	return results

def getFollowedPosts(userID, n=50):
	follows = getFollowedIDs(userID)
	post_list = []
	for follow in follows:
		new_posts = getPostsByUserID(follow)
		if new_posts is not None:
			post_list += new_posts
	
	post_list.sort(reverse=True, key=(lambda e : e.PostTime))
	print(post_list)
	return post_list[0:n-1]