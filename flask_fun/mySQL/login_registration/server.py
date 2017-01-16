from flask import Flask, render_template, session, request, redirect, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "e94f849828dfc7122c30106a8b42fb4c3"
mysql = MySQLConnector(app, 'userdb')
bcrypt = Bcrypt(app)

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route('/')
def index():
    if 'is_valid' in session:
        session.clear()
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    is_valid = True
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    password = request.form['password']
    password_confirm = request.form['password_confirm']

    if len(session['first_name']) < 2:
        is_valid = False
        flash(u'First name must be at least 2 characters.', 'first_name_error')
    if len(session['last_name']) < 2:
        is_valid = False
        flash(u'Last name must be at least 2 characters.', 'last_name_error')
    if not EMAIL_REGEX.match(session['email']):
        is_valid = False
        flash(u'Please enter a valid email address.', 'email_error')
    if len(password) < 8:
        is_valid = False
        flash(u'Password must be at least 8 characters', 'pw_error')
    elif password != password_confirm:
        is_valid = False
        flash(u'Password does not match. Please re-enter your password.', 'confirm_pw_error')
    if is_valid:
        query = "SELECT email_address FROM users WHERE email_address = :specific_email"
        data = {'specific_email': session['email']}
        register_email = mysql.query_db(query, data)
        if register_email:
            flash(u'Email address already registered. Please log in.', 'email_error')
            return redirect('/')
        else:
            pw_hash = bcrypt.generate_password_hash(password)
            insert_query = "INSERT INTO users (first_name, last_name, email_address, pw_hash, created_at) VALUES (:first_name, :last_name, :email_address, :pw_hash, NOW())"
            query_data = { 'first_name': session['first_name'],
                           'last_name': session['last_name'],
                           'email_address': session['email'],
                           'pw_hash': pw_hash
                           }
            mysql.query_db(insert_query, query_data)
            query = "SELECT * FROM users WHERE email_address = :specific_email"
            data = {'specific_email': session['email']}
            user = mysql.query_db(query, data)
        return render_template('userpage.html', user=user[0])
    else:
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    session['email'] = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE email_address = :email LIMIT 1"
    user_data = {'email': session['email']}
    user = mysql.query_db(user_query, user_data)
    if user:
        if session['email'] == user[0]['email_address']:
            if bcrypt.check_password_hash(user[0]['pw_hash'], password):
                return render_template('userpage.html', user=user[0])
            else:
                flash(u'Incorrect password. Please try again.', 'wrong_pw')
                return redirect('/')
    else:
        flash(u'Email does not exist in the database. Please register.', 'no_user')
        return redirect('/')

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')
    
app.run(debug=True)
