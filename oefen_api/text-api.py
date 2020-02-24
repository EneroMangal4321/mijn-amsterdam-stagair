from flask import Flask, json, request

app = Flask(__name__)

@app.route("/", method="GET")
def schrijf_json():
    x = '{ "name": "Enero", "age": 18, "friends": ["Anass", "Aman", "Ayoub"] }' 
    text = json.loads(x)
    return text["name"]

if __name__ == "__main__":
    app.run()