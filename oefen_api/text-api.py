from flask import Flask, json
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask"

def schrijf_json():
    text1 = (request.json["key"])
    text2 = (request.json["value"])

if __name__ == "__main__":
    app.run(debug=True)