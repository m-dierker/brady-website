import sys
import os
import json
from website import app
from flask import Flask, render_template, url_for, render_template_string
from models import *
from prettifySPICE import *


# don't use models.Post, use Post
# don't forget to check permissions

@app.route('/index.html')
@app.route('/home')
@app.route('/')
def home():
    return render_template('aboutme.html', title='About')

@app.route('/about')
def about():
	return render_template('aboutme.html', title='About')

@app.route('/post')
def post():
	cat = Category.query.all()
	cat = cat[0]
	bodypath = ("/home/brady/website/website/posts/resistor-divider.html")
	postbody = open(bodypath, 'r').read()
	testPost = Post(title='Resistor Divider', body=postbody, category=cat)
	postbody = render_template_string(postbody)
	return render_template('post.html', post=testPost, body=postbody, title=testPost.title)

@app.route('/shivani')
def shivani():
	return render_template('aboutugly.html', title='Ugly')

@app.route('/resume')
def resume():
	return render_template('resume.html')

@app.route('/blogtest')
def blogex():
    return render_template('index.html')

@app.route('/svgtest')
def svg():
	return render_template('svgtest.html')

@app.route('/code')
def codesample():
	scriptPath = os.path.dirname(__file__)
	filePath = 'spice/rc-filter.net'
	codeTest = prettifySPICE(os.path.join(scriptPath, filePath))
	return render_template('codesample.html', data=codeTest)

@app.route('/rand')
def plotsample():
	scriptPath = os.path.dirname(__file__)
	plotPath = 'plots/testscript.html'
	plotTest = os.path.join(scriptPath, plotPath)
	plotTest = open(plotTest, 'r').read()
	return render_template('codesample.html', data=plotTest)

@app.route('/post/<post>')
def anyPost(post):
	validPath = os.path.dirname(__file__)
	relPath = 'posts'
	validPath = os.path.join(validPath, relPath)

	validPosts = [ f for f in os.listdir(validPath) if os.path.isfile(os.path.join(validPath, f)) ]
	validPosts = [ p.rsplit('.')[0] for p in validPosts ]

	if post in validPosts:
		validFile = os.path.join(validPath, post + '.json')
		jsonData = open(validFile, 'r')
		jsonData = json.load(jsonData, strict=False)
		rBody = render_template_string(jsonData['body'])
		return render_template('post.html', title=jsonData['title'], date=jsonData['date'],
								category=jsonData['category'], body=rBody)


	#return ' '.join(validPosts)




