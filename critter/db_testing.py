from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:password@localhost:1433/Critter'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



@app.route("/")
def testoutput():
	return "<p>" + db_queries.getUserLoginInfoByID(1) + "</p>"