from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello, DevOps!"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/info")
def info():
    return jsonify({
        "project": "somativa-devops",
        "version": "1.0.0",
        "author": "Diego Reis"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)