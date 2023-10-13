#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

file = (open(r"files/file.txt", "r")).read()

@app.route("/")
def hello():
    # return "Hello World!"
    return file
