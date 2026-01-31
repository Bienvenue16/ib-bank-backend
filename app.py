from flask import Flask, jsonify
from flask_cors import CORS
from routes.chat import chat_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(chat_bp)

@app.route("/")
def home():
    return jsonify({"status": "IB Bank AI backend running"})

if __name__ == "__main__":
    app.run(debug=True)
