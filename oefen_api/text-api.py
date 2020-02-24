from flask import Flask, json, request

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def schrijf_json():
    x = open("text.json")
    text = json.loads(x)
    return text

if __name__ == "__main__":
    app.run()