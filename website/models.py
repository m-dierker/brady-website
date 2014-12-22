from website import app, db
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

class Post(db.Model):
	# Actual post on blog
	
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(80))
	body = db.Column(db.Text)
	pub_date = db.Column(db.DateTime)

	category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
	category = db.relationship('Category', backref=db.backref('posts', lazy='dynamic'))

	def __init__(self, title, body, category, pub_date=None):
		self.title = title
		self.body = body
		if pub_date is None:
			pub_date = datetime.now()

		self.pub_date = pub_date
		self.category = category

	def __repr__(self):
		return '<Post %r>' % self.title

class Category(db.Model):
	# Categories tied to each post
	# Available items:
	# passive, active, rf, mixed signal, power, digital

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50))

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return '<Category %r>' % self.name

class Comment(db.Model):
	# Comments tied to each post
	id = db.Column(db.Integer, primary_key=True)
	commentary = db.Column(db.Text)
	name = db.Column(db.String(50))
	comment_date = db.Column(db.DateTime)

	post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
	post = db.relationship('Post', backref=db.backref('comments', lazy='dynamic'))

	def __init__(self, commentary, name, post, time=None):
		self.commentary = commentary
		self.name = name
		if time is None:
			time = datetime.utcnow()
		comment_date = time
		self.post = post

	def __repr__(self):
		return '<Comment %r at %r>' % (self.title, self.comment_date)

