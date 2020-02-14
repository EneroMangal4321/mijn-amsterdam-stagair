from flask import Flask, request, json

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
        global U


    if action == "subtract":
        uitkomst = 0
        for index, x in enumerate(num):
            if index == 0:
                uitkomst = x
            else:
                uitkomst = uitkomst - x


    if action == "divide":
        uitkomst = 0
        for index, x in enumerate(num):
            if index == 0:
                uitkomst = x
            else:
                uitkomst = uitkomst / x

        uitkomstInt = int(uitkomst)
        if uitkomst == uitkomstInt:
            uitkomst = uitkomstInt


    if action == "add":
        uitkomst = 0
        for x in num:
            uitkomst = uitkomst + x


    U = json.dumps({"result": uitkomst})
    return U


if __name__ == '__name__':
    app.run(debug=True)