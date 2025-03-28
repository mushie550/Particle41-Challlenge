from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def get_time():
    response = {
        "timestamp": datetime.utcnow().isoformat(),
        "ip": request.remote_addr
    }
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

