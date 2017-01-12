from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "008c5926ca861023c1d2a36653fd88e2"


@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html', counter = session['counter'])

@app.route('/plus_two')
def plus_two():
    if 'counter' in session:
        session['counter'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    if 'counter' in session:
        session['counter'] = 0
    return redirect('/')
app.run(debug=True)
