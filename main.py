import flask 
import json 
from flask import render_template , jsonify

app = flask.Flask("main")

@app.route("/")
def home():
   return render_template("index.html")  

@app.route("/category")
def category():
    with open("categories.json", "r") as json_file:
        categories_data = json.load(json_file)
    return flask.render_template("categories.html", categories=categories_data["categories"])