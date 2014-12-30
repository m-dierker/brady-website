import sys
import os
import json
from website import app
from flask import Flask, render_template, url_for, render_template_string
from models import *
from prettifySPICE import *
from operator import itemgetter

# don't use models.Post, use Post
# don't forget to check permissions

@app.route('/index')
@app.route('/index.html')
@app.route('/home')
@app.route('/')
def home():
	jsonPosts = getPostsJSON()
	
	jsonPosts = sorted(jsonPosts, key=itemgetter('date'))
	jsonPosts = jsonPosts[::-1][:3] # apparently it reverses a list

	#return ' '.join(urls)
	return render_template('home.html', title='Home',  posts=jsonPosts)


@app.route('/post/<post>')
def anyPost(post):
	validPosts, validPath = getValidPosts()

	if post in validPosts:
		validFile = os.path.join(validPath, post + '.json')
		jsonFile = open(validFile, 'r')
		jsonData = json.load(jsonFile, strict=False)
		jsonFile.close()
		rBody = render_template_string(jsonData['body'])
		return render_template('post.html', title=jsonData['title'], date=jsonData['date'],
								category=jsonData['category'], body=rBody)
	else:
		return pageNotFound(404)


@app.route('/category/<cat>')
def anyCategory(cat):
	jsonPosts = getPostsJSON()
	validCat = ['passive', 'analog', 'power', 'digital', 'mixed-signal', 'rf']

	if cat in validCat:
		# yes dierker shut up i'll one line this later (lol no i won't)
		dates = [d['date'] for d in jsonPosts if d['category'] == cat]
		titles = [t['title'] for t in jsonPosts if t['category'] == cat]
		urls = [u['url'] for u in jsonPosts if u['category'] == cat]
		return render_template('categories.html', title=cat.title(), dates=dates, titles=titles, 
								urls=urls, zip=zip)
	else:
		return pageNotFound(404)		


@app.route('/topics')
def topics():
	jsonPosts = getPostsJSON()
	
	jsonPosts = sorted(jsonPosts, key=itemgetter('date'))
	jsonPosts = jsonPosts[::-1] # apparently it reverses a list

	dates = [d['date'] for d in jsonPosts]
	titles = [t['title'] for t in jsonPosts]
	urls = [u['url'] for u in jsonPosts]

 	return render_template('topics.html', title='Topics', titles=titles, dates=dates, urls=urls, zip=zip)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/resume')
def resume():
	return render_template('resume.html')


@app.errorhandler(404)
def pageNotFound(e):
	return render_template('error.html', title='404', errmsg='Page Not Found'), 404


@app.route('/contact')
def contact():
	return render_template('contact.html', title="Contact")

	
@app.route('/thanks')
def thanks():
	return render_template('thanks.html', title='Acknowledgements')

def getValidPosts():
	validPath = os.path.dirname(__file__)
	relPath = 'posts'
	validPath = os.path.join(validPath, relPath)

	validPosts = [ f for f in os.listdir(validPath) if os.path.isfile(os.path.join(validPath, f)) ]
	validPosts = [ p.rsplit('.')[0] for p in validPosts ]
	return validPosts, validPath


def getPostsJSON():
	validPosts, validPath = getValidPosts()
	
	jsonPosts = []
	for post in validPosts:
		validFile = os.path.join(validPath, post + '.json')
		jsonFile = open(validFile, 'r')
		jsonData = json.load(jsonFile, strict=False)
		jsonPosts.append(jsonData)
		jsonFile.close()

	return jsonPosts