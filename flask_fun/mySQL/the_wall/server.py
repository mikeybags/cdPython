from flask import Flask, render_template, redirect, session, flash, request, Markup
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
mysql = MySQLConnector(app, 'walldb')
app.secret_key = "e94f849828dfc7122c30106a8b42fb4c3"
bcrypt = Bcrypt(app)

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def validate_registration(first_name, last_name, email, password, password_confirm):
    is_valid = True
    if len(first_name) < 2:
        is_valid = False
        flash(u'First name must be at least 2 characters', 'first_name_error')
    if len(last_name) < 2:
        is_valid = False
        flash(u'Last name must be at least 2 characters', 'last_name_error')
    if not EMAIL_REGEX.match(session['email']):
        is_valid = False
        flash(u'Please enter a valid email address.', 'email_error')
    if len(password) < 8:
        is_valid = False
        flash(u'Password must be at least 8 characters', 'pw_error')
    elif password != password_confirm:
        is_valid = False
        flash(u'Passwords do not match. Please re-enter your password.', 'pw_confirm_error')
    return is_valid

@app.route('/')
def index():
    if 'user_id' in session:
        session.clear()
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    session['email'] = request.form['email']
    password = request.form['password']
    query = "SELECT * from users WHERE email = :email"
    data = {'email': session['email']}
    valid_user = mysql.query_db(query, data)
    if valid_user:
        if session['email'] == valid_user[0]['email']:
            if bcrypt.check_password_hash(valid_user[0]['pw_hash'], password):
                session['user_id'] = valid_user[0]['id']
                session['first_name'] = valid_user[0]['first_name']
                return redirect('/wall')
            else:
                flash(u'Incorrect password. Please try again.', 'wrong_pw')
                return redirect('/')
    else:
        flash(u'Email does not exist in the database. Please register.', 'invalid_user')
        return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    password = request.form['password']
    password_confirm = request.form['password_confirm']
    if validate_registration(session['first_name'], session['last_name'], session['email'], password, password_confirm):
        query = "SELECT * FROM users WHERE email = :specific_email"
        data = {'specific_email': session['email']}
        email_taken = mysql.query_db(query, data)
        if email_taken:
            flash(u'Email address already registered. Please log in or register another email address.', 'email_error')
            return redirect('/')
        else:
            pw_hash = bcrypt.generate_password_hash(password)
            add_query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email , :pw_hash, NOW(), NOW())"
            add_data = {'first_name': session['first_name'],
                        'last_name': session['last_name'],
                        'email': session['email'],
                        'pw_hash': pw_hash
                        }
            mysql.query_db(add_query, add_data)
            login_query = "SELECT * FROM users WHERE email = :specific_email"
            login_data = {'specific_email': session['email']}
            active_user = mysql.query_db(login_query, login_data)
            session['user_id'] = active_user[0]['id']
            session['first_name'] = active_user[0]['first_name']
            return redirect('/wall')
    else:
        return redirect('/')

@app.route('/wall')
def wall():
    message_query = "SELECT first_name, last_name, message, messages.created_at, messages.id, messages.user_id FROM messages JOIN users ON messages.user_id = users.id ORDER BY messages.created_at DESC"
    messages = mysql.query_db(message_query)
    comment_query = "SELECT first_name, last_name, comment, comments.created_at, message_id, comments.user_id, comments.id FROM comments JOIN users ON comments.user_id = users.id ORDER BY comments.created_at ASC"
    comments = mysql.query_db(comment_query)
    print "comment", comments, "session user id is", session['user_id']
    return render_template('wall.html', all_messages=messages, message_comments=comments)

@app.route('/new_message', methods=['POST'])
def new_message():
    query = "INSERT INTO messages (message, created_at, updated_at, user_id) VALUES (:message, NOW(), NOW(), :id)"
    data = {'message': request.form['message'],
            'id': session['user_id']
            }
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/new_comment/<message_id>', methods=['POST'])
def new_comment(message_id):
    query = "INSERT INTO comments (comment, created_at, updated_at, user_id, message_id) VALUES (:comment, NOW(), NOW(), :user_id, :msg_id)"
    comment = Markup(request.form['comment'])
    data = {'comment': comment,
            'user_id': session['user_id'],
            'msg_id': message_id}
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/messages/<message_id>/delete', methods=['POST'])
def delete_message(message_id):
    query = "DELETE FROM messages WHERE id = :specific_id"
    data = {'specific_id': message_id}
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/comments/<comment_id>/delete', methods=['POST'])
def delete_comment(comment_id):
    query = "DELETE FROM comments WHERE id = :specific_id"
    data = {'specific_id': comment_id}
    mysql.query_db(query, data)
    return redirect('/wall')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True)
