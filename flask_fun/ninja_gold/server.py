from flask import Flask, render_template, redirect, request, session, flash
import random
import datetime

app = Flask(__name__)
app.secret_key = "9cf8cf0715076c1324f38046a2ec75d4"

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activity_log' not in session:
        session['activity_log'] = []
    return render_template("index.html")

@app.route('/process_money', methods=["POST"])
def process_money():
    choice = request.form["choice"]
    timestamp = str(datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p"))
    if choice == 'farm':
        earnings = random.randrange(10,21)
        session['gold'] += earnings
        activity_log = 'Earned ' +  str(earnings) + ' pieces of gold from the farm! (' + timestamp + ')'
        session['activity_log'].append(activity_log)
    elif choice == 'cave':
        earnings = random.randrange(5,11)
        session['gold'] += earnings
        activity_log = 'Found ' + str(earnings) + ' pieces of gold in the cave! (' + timestamp + ')'
        session['activity_log'].append(activity_log)
    elif choice == 'house':
        earnings = random.randrange(2, 6)
        session['gold'] += earnings
        activity_log = 'Found ' + str(earnings) + ' pieces of gold in the couch cushions! (' + timestamp + ')'
        session['activity_log'].append(activity_log)
    else:
        if session['gold'] == 0:
            flash('You have no gold to risk at the casino! (' + timestamp + ')')
        else:
            results = random.randrange(-50,51)
            print "result is ", results
            if results < 0:
                if ((session['gold'] + results) <= 0):
                    activity_log = 'Lost all ' + str(session['gold']) + ' pieces of gold at the casino! :-(  (' + timestamp + ')'
                    session['gold'] = 0
                    session['activity_log'].append(activity_log)
                else:
                    session['gold'] += results
                    results *= -1
                    activity_log = 'Lost ' + str(results) + ' pieces of gold at the casino! :-(  (' + timestamp + ')'
                    session['activity_log'].append(activity_log)
            elif results > 0:
                session['gold'] += results
                activity_log = 'Won ' + str(results) + ' pieces of gold at the casino! Woot!  (' + timestamp + ')'
                session['activity_log'].append(activity_log)
            else:
                session['gold'] += 0
                activity_log = 'Came out even at the casino! Try again?  (' + timestamp + ')'
                session['activity_log'].append(activity_log)
    return redirect('/')

app.run(debug=True)
