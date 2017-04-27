#!/usr/bin/python
# coding: utf-8
from flask import Flask

app = Flask(__name__)

@app.route('/')
def entry_point():
    return 'Hello Grumpy World!'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
