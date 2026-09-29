import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/version")
def version():
    ver = os.getenv("APP_VERSION", "0.0.0")
    return jsonify(
        service="version-api",
        version=ver
    )

@app.get("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)