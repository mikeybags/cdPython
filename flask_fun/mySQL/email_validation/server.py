from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "e94f849828dfc7122c30106a8b42fb4c3"
mysql = MySQLConnector(app, 'emaildb')

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    if 'is_valid' in session:
        session.clear()
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    is_valid = True
    session['email'] = request.form['form_email']
    if len(session['email']) < 1:
        is_valid = False
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(session['email']):
        is_valid = False
        flash("Email is not valid. Please enter a valid email address.")
    if is_valid:
        session['is_valid'] = True
        query = "INSERT INTO emails (email_address, created_at) VALUES (:email_address, NOW())"
        data = {
            'email_address': session['email']
        }
        mysql.query_db(query, data)
        query = "SELECT * FROM emails"
        emails = mysql.query_db(query)
        flash("The email address you entered " + session['email'] + " is a VALID email address. Thank you!")
        return render_template('success.html', all_emails = emails)
    else:
        return redirect('/')

@app.route('/delete/<email_id>', methods=['POST'])
def delete(email_id):
    query = "SELECT email_address FROM emails WHERE id = :id"
    data = {'id': email_id}
    email_deleted = mysql.query_db(query, data)
    print email_deleted
    query = "DELETE FROM emails WHERE id = :id"
    data = {'id': email_id}
    mysql.query_db(query, data)
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)
    flash(email_deleted[0]['email_address'] + " was deleted successfully")
    return render_template('success.html', all_emails = emails)

app.run(debug=True)
