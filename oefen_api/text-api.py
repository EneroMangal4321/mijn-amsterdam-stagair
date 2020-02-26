from flask import Flask, json, request

app = Flask(__name__)

@app.route("/")
def json_formatting():
    data = None
    with open("text.json") as myfile:
        try:
            data = json.load(myfile)
        except KeyError:
            return None
    #hier is ruimte om iets met de inhoud van text.json te doen
    return json.dumps(data, sort_keys=False)

if __name__ == "__main__":
    app.run(debug=True)
