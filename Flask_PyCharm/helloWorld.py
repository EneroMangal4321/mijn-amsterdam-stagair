from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    i = 1
    return render_template('index.html', i = i)