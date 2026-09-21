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

@app.route("/sum/<int:a>/<int:b>")
def sum_numbers(a, b):
    return jsonify({"result": a + b})

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)