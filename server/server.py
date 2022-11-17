from flask import Flask, request, jsonify 

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>IoT Flask Server</h1>"

@app.route("/api/send", methods=['POST'])
def api_send():
    post_data = request.json
    print(post_data)
    return jsonify({'result': 'data received'})
