# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2010 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import with_statement
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
    return top.sqlite_db


@app.teardown_appcontext
def close_db_connection(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()


@app.route('/test')
def test():
    db = get_db()
    cur = db.execute('SELECT * FROM users WHERE username = "cs350"')
    users = ' '
    for row in cur.fetchall():
        users += row[0]
    return users

@app.route('/newtable')
def newtable():
    db = get_db()
    cur = db.execute('INSERT INTO studio (name, address)'
                     ' VALUES(?, ?)', 
                     ['MGM', '500 HollyWood Blvd.'])
    db.commit()
    return 'studio added'

@app.route('/movies')
def movies():
    db = get_db()
    cur = db.execute('SELECT * FROM movies ORDER BY year')
    movies = ''
    for row in cur.fetchall():
        movies += row [0] + ': ' + str(row [1]) + ', ' + row [2] + ', ' + row [3] + '<br>'
    return movies
    
    

@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text, author from entries order by id desc')
    entries = [dict(title=row[0], text=row[1], author=row[2])
               for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text, author) values (?, ?, ?)',
                 [request.form['title'], request.form['text'], app.g])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        db = get_db()
        cur = db.execute('select password from users where username=?',
                         [request.form['username']])
        passwords = cur.fetchall()
        if len(passwords):
            if passwords[0][0] == request.form['password']:
                app.g = request.form['username']
                session['logged_in'] = True
                flash('You were logged in as '+app.g)
                return redirect(url_for('show_entries'))
            else:
                error = 'Invalid password'
        else:
            error = 'Invalid username'
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
