from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager

db = SQLAlchemy()
login = LoginManager()

@login.user_loader
def load_user(id):
    return Users.query.get(int(id))

class Users(UserMixin, db.Model):

	__tablename__ = "Users"

	UserID = db.Column(db.Integer, primary_key = True)		#User ID
	Username = db.Column(db.String(), unique = True)	#Username
	Email = db.Column(db.String(), unique = True)		#Email
	Password = db.Column(db.String())				#Password Hash
	
	# Create the relationship between Users and User_Profiles
	user_profiles = db.relationship('User_Profiles', backref='users', uselist=False)

	#Creates a password hash from a given password.
	def set_password(self,password):
		self.Password = generate_password_hash(password)
     
	#Checks if the given password matches the existing password hash.
	def check_password(self,password):
		return check_password_hash(self.Password,password)
		
class User_Profiles(db.Model):

	__tablename__ = "User_Profiles"
	
	UserID = db.Column(db.Integer, db.ForeignKey('Users.UserID'), primary_key = True, autoincrement=True)	#User ID
	Username = db.Column(db.String)												#Username
	Gender = db.Column(db.String)												#Gender
	Bio = db.Column (db.String)													#Bio Text
	Avatar = db.Column(db.LargeBinary)											#Avater ID (Media ID)
	
	# Create relationships
	# posts = db.relationship('Posts', backref='user_profiles')
	# #follows = relationship('Follows', backref='user_profiles')
	# #likes = relationship('Likes', backref='user_profiles')

class Media(db.Model):
	
	__tablename__ = 'Media'
	
	MediaID = db.Column(db.Integer, primary_key = True)	#Media ID
	MediaURI = db.Column(db.String)						#Media URI
	
	# Create Relationships
	posts = db.relationship('Posts', backref='media')

class Post_Types(db.Model):

	__tablename__ = 'Post_Types'
	
	TypeID = db.Column(db.Integer, primary_key = True)	#Post Type ID
	PostType = db.Column(db.String)					#Post Type [ text | photo | video ]
	
	# Create relationships
	posts = db.relationship('Posts', backref='types')

class Posts(db.Model):
	
	__tablename__ = 'Posts'
	
	PostID = db.Column(db.Integer, primary_key = True)					#Post ID
	UserID = db.Column(db.Integer, db.ForeignKey(User_Profiles.UserID))	#Author ID
	PostType = db.Column(db.Integer, db.ForeignKey(Post_Types.PostType))	#Post Type (Type ID)
	Text = db.Column(db.String)										#Text-Content
	MediaID = db.Column(db.Integer, db.ForeignKey(Media.MediaID))			#Media ID
	PostTime = db.Column(db.DateTime)									#Date/time of post
	
	# Create relationships
	likes = db.relationship('Likes', backref='postslikes')

		
class Likes(db.Model):
	
	__tablename__ = 'Likes'
	
	LikeID = db.Column(db.Integer, primary_key = True)					#Like ID
	UserID = db.Column(db.Integer, db.ForeignKey(User_Profiles.UserID))	#Liker's ID
	PostID = db.Column (db.Integer, db.ForeignKey(Posts.PostID))			#Liked Post ID

		
class Follows(db.Model):

	__tablename__ = 'Follows'
	
	RelationshipID = db.Column(db.Integer, primary_key = True)					#Relationship ID
	UserID = db.Column(db.Integer, db.ForeignKey(User_Profiles.UserID))	#Follower's ID
	FollowingID = db.Column(db.Integer, db.ForeignKey(User_Profiles.UserID))	#Followed's ID