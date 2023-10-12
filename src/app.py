#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

file = (open(r"file.txt", "r")).read()

@app.route("/")
def hello():
    # return "Hello World! v1.0.0.0"
    return file
