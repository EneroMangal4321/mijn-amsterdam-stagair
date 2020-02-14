from flask import Flask, request, json, jsonify

app = Flask(__name__)

@app.route('/calc/', methods = ['POST'])
def index():
    action = (request.json['action'])
    num = request.json['values']
    test = request.get_json()
    if action == "multiply":
        uitkomst = 1
        for x in num:
            uitkomst = x * uitkomst

        O = json.dumps({"result": uitkomst})
        return O

    if action == "subtract":
        uitkomst = 0
        for x in num:
            uitkomst = x - uitkomst

        O = json.dumps({"result": uitkomst})
        return O

    if action == "devide":
        uitkomst = 1
        for x in num:
            uitkomst = x / uitkomst

        O = json.dumps({"result": uitkomst})
        return O


if __name__ == '__name__':
    app.run(debug=True)