from flask import Flask, json, request

app = Flask(__name__)

@app.route("/")
def json_formatting():
    data = None
    with open("text.json") as myfile:
        try:
            data = myfile.read()
        except KeyError:
            return None
    obj = json.loads(data)
    #hier is ruimte om iets met de inhoud van text.json te doen
    #text = json.dumps(obj, sort_keys=False)
    return json.dumps(obj["name"], sort_keys=False)

if __name__ == "__main__":
    app.run(debug=True)
