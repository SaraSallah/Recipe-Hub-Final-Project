import flask 
import json 
from flask import render_template , jsonify

app = flask.Flask("main")

@app.route("/")
def home():
   return render_template("index.html")  