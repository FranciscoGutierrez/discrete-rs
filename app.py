#coding: utf-8

from flask import Flask, render_template, jsonify
from durable.lang import *
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(
        username="rest api ready",
        email="rest api ready",
        id="rest api ready"
    )

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
