# -*- coding: utf-8 -*-
__author__ = 'venking'
from flask import flash, redirect, render_template,request, url_for,Blueprint

loginctrl=Blueprint('login',__name__)



@loginctrl.route('/coming')
def index():
    print 'I am coming..........'
    return render_template('index.html')


@loginctrl.route('/', methods=['GET', 'POST'])
def login():
    print 'I am coming,too..........'
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'secret':
            error = 'Invalid credentials'
            print error
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    data={
        'error':error
    }
    print data
    return render_template('login.html', **data)

