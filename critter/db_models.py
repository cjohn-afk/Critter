from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager

db = SQLAlchemy()
login = LoginManager()

class Users(UserMixin, db.Model):

	__tablename__ = "Users"

	id = db.Column(db.Integer, primary_key = True)		#User ID
	username = db.Column(db.String(), unique = True)	#Username
	email = db.Column(db.String(), unique = True)		#Email
	password_hash = db.Column(db.String())				#Password Hash
	
	# Create the relationship between Users and User_Profiles
	user_profiles = db.relationship('User_Profiles', backref='users', uselist=False)

	#Creates a password hash from a given password.
	def set_password(self,password):
		self.password_hash = generate_password_hash(password)
     
	#Checks if the given password matches the existing password hash.
	def check_password(self,password):
		return check_password_hash(self.password_hash,password)
		
		
class User_Profiles(db.Model):

	__tablename__ = "User_Profiles"
	
	id = db.Column(db.Integer, db.ForeignKey('Users.id'), primary_key = True)	#User ID
	username = db.Column(db.String)												#Username
	gender = db.Column(db.String)												#Gender
	bio = db.Column (db.String)													#Bio Text
	avatar = db.Column(db.LargeBinary)											#Avater ID (Media ID)
	
	# Create relationships
	# posts = db.relationship('Posts', backref='user_profiles')
	# #follows = relationship('Follows', backref='user_profiles')
	# #likes = relationship('Likes', backref='user_profiles')

class Media(db.Model):
	
	__tablename__ = 'Media'
	
	id = db.Column(db.Integer, primary_key = True)	#Media ID
	uri = db.Column(db.String)						#Media URI
	
	# Create Relationships
	posts = db.relationship('Posts', backref='media')

class Post_Types(db.Model):

	__tablename__ = 'Post_Types'
	
	id = db.Column(db.Integer, primary_key = True)	#Post Type ID
	type = db.Column(db.String)						#Post Type [ text | photo | video ]
	
	# Create relationships
	posts = db.relationship('Posts', backref='types')

class Posts(db.Model):
	
	__tablename__ = 'Posts'
	
	id = db.Column(db.Integer, primary_key = True)					#Post ID
	uid = db.Column(db.Integer, db.ForeignKey(User_Profiles.id))	#Author ID
	type = db.Column(db.Integer, db.ForeignKey(Post_Types.type))	#Post Type (Type ID)
	text = db.Column(db.String)										#Text-Content
	mid = db.Column(db.Integer, db.ForeignKey(Media.id))			#Media ID
	time = db.Column(db.DateTime)									#Date/time of post
	
	# Create relationships
	likes = db.relationship('Likes', backref='postslikes')

		
class Likes(db.Model):
	
	__tablename__ = 'Likes'
	
	id = db.Column(db.Integer, primary_key = True)					#Like ID
	uid = db.Column(db.Integer, db.ForeignKey(User_Profiles.id))	#Liker's ID
	pid = db.Column (db.Integer, db.ForeignKey(Posts.id))			#Liked Post ID

		
class Follows(db.Model):

	__tablename__ = 'Follows'
	
	id = db.Column(db.Integer, primary_key = True)					#Relationship ID
	uid = db.Column(db.Integer, db.ForeignKey(User_Profiles.id))	#Follower's ID
	fid = db.Column(db.Integer, db.ForeignKey(User_Profiles.id))	#Followed's ID




