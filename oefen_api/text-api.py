from flask import Flask, json, request

app = Flask(__name__)

@app.route("/")
def schrijf_json():
    with open("text.json") as myfile:
        data = myfile.read()

    obj = json.loads(data)

    return str(obj)

if __name__ == "__main__":
    app.run(debug=True)