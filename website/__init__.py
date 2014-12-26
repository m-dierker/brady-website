import sys
from flask import Flask, render_template, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask('website')

app.jinja_env.globals.update(url_for=url_for)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/brady/website/website/blog.db'
db = SQLAlchemy(app)


import website.views
import website.models
from website.spice import prettifySPICE


if __name__ == '__main__':
    app.run()
