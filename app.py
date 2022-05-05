from flask import Flask, jsonify, render_template, request, url_for
from JSONParser import parser, eval
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/validatethisjson', methods=['POST'])
def validate():
    son = request.get_json(force=True)
    val = son['stri']
    send = {}
    try:
        parse = parser.parse(val)
        if parse:
            send["value"] = eval(parse, "", 0)
            send["isvalid"] = True
        else:
            send["isvalid"] = False
    except:
        send["isvalid"] = False
        send['error'] = "Error"

    return jsonify(send)

if __name__ == '__main__':
    app.run(debug=True)