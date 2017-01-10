from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def hello_world():
    #return 'Hello World!'
    return render_template('index.html', name="Mike")

app.run(debug=True)

'''
Inside of your HTML file:
{{ some variable }} evaluate and output whatever you put inside of them (which you pass in the return render_template statement...ie name="Mike" above)
{% some expression %} is used for for loops, if statements, etc
'''
