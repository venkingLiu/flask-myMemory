# -*- coding: utf-8 -*-
__author__ = 'venking'

from flask import Flask
from web import loginctrl
from module.util import fromtimestamp

app = Flask(__name__)
app.register_blueprint(loginctrl,url_prefix='/login')

app.add_template_filter(fromtimestamp)
app.secret_key = 'zoupan19940907'

# @app.route('/')
# def index():
#     return 'Index Page!'
#
#
# @app.route('/hello')
# def hello_world():
#     return 'Hello World!'
#
#
# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     flash('你好，%s'%(username))
#     return 'User %s' % username
#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8181,debug=True)


