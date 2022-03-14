from flask_login import login_required, login_user, logout_user
from test.model.User import  User
from test.model.Category import Category
import os

from test import app,db
from flask import request,render_template,flash,abort,url_for,redirect,session,Flask,g

@app.route('/')
@login_required
def show_entries():
    categorys = Category.query.all()
    return render_template('show_entries.html',entries=categorys)


@app.route('/add',methods=['POST'])
@login_required
def add_entry():
    # if not session.get('logged_in'):
    #     abort(401)
    title = request.form['title']
    content = request.form['text']
    category = Category(title,content)
    db.session.add(category)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        # passwd = User.query.filter_by(password=request.form['password'])
        print(user)
        # print(passwd)
        # passwd = User.query.filter_by(password=request.form['password']).first()
        #
        # if user is None:
        #     error = 'Invalid username'
        # elif passwd is None:
        #     error = 'Invalid password'
        # else:
        #     session['logged_in'] = True
        #     flash('You were logged in')
        #     return redirect(url_for('show_entries'))
        login_user(user)
        flash('Logged in successfully.')
        return redirect(url_for('show_entries'))

    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    # session.pop('logged_in', None)
    logout_user()
    # flash('You were logged out')
    return redirect(url_for('show_entries'))