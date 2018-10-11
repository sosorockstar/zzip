# coding: utf-8

from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Index Page'


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return 'Hello, Post way'
    else:
        return 'Hello, World'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % subpath


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'