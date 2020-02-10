from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    names = ['a', 'b', 'c', 'd']
    string = 'Hallo wereld'
    return render_template('index.html', names=names)