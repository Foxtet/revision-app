from flask import Flask, jsonify

__version__ = "1.1.0"
app = Flask(__name__)


@app.get("/stats")
def stats():
    return jsonify(routes=4, version=__version__, uptime="ok")


@app.get("/")
def index():
    return jsonify(message="Usine logicielle", version=__version__)


@app.get("/health")
def health():
    return jsonify(status="ok"), 200


@app.get("/version")
def version():
    return jsonify(version=__version__)
