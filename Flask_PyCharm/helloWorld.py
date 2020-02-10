from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    names = ['anass', 'ayoub', 'aman', 'enero']
    return render_template('index.html', names=names)