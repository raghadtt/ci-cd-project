from flask import Flask, request, jsonify
import os

app = Flask (__name__)

@app.route("/")
def home():
    return "Hello CI/CD"

@app.route("/add")
def add():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": a + b})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)