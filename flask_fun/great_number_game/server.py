from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "008c5926ca861023c1d2a36653fc88e2"

@app.route('/')
def index():
    import random
    if 'number' not in session:
        session['number'] = random.randrange(0, 101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    try:
        guess = int(request.form['guess'])
        if guess == session['number']:
            session['result'] = 'correct'
        elif guess > session['number']:
            session['result'] = 'tooHigh'
        elif guess < session['number']:
            session['result'] = 'tooLow'
    except:
        session['result'] = 'error'
    return redirect('/')

@app.route('/new')
def new():
    session.pop('number')
    session.pop('result')
    return redirect('/')
app.run(debug=True)
