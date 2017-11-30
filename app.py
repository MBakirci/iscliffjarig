"""
This file is part of the flask+d3 Hello World project.
"""
import json
import flask

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")
