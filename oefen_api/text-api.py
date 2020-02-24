from flask import Flask, json, request

app = Flask(__name__)

@app.route("/")
def schrijf_json():
    '''x = '{ "name": "Enero", "age": 18, "friends": ["Anass", "Aman", "Ayoub"] }' 
    text = json.loads(x)'''

    with open("text.json") as myfile:
        data = myfile.read()

    obj = json.loads(data)

    return obj["name"]

if __name__ == "__main__":
    app.run(debug=True)