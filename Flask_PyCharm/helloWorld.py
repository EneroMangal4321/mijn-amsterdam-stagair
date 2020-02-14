from flask import Flask, request, json, jsonify

app = Flask(__name__)

@app.route('/calc/', methods = ['POST'])
def index():
    result = (request.json['action'])
    num = request.json['values']
    uitkomst = 1
    test = request.get_json()
    if result == "multiply":
        for x in num:
            uitkomst = x * uitkomst


    #U = format(uitkomst)
    O = json.dumps({"result": uitkomst})
    return O

if __name__ == '__name__':
    app.run(debug=True)