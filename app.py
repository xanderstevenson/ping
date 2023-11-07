from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return send_from_directory('static', 'pong.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)