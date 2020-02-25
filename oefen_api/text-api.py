from flask import Flask, json, request

app = Flask(__name__)

@app.route("/")
def json_formatting():
    with open("text.json") as myfile:
        data = myfile.read()

    obj = json.loads(data)
    x = json.dumps(obj, sort_keys=False)
    return str(x["name"])

if __name__ == "__main__":
    app.run(debug=True)
