#!/usr/bin/env python
# coding=utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_world(name=None):
    return render_template('index.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User is %s' % username

if __name__ == '__main__':
    app.run()
