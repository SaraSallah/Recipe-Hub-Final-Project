import flask 
from flask import render_template , request,redirect, url_for
import json
import os

app = flask.Flask("main")

@app.route("/")
def home():
   with open("recipes.json", "r") as json_file:
       recipes_data = json.load(json_file)
   return render_template("index.html", recipes=recipes_data["recipes"])
 

@app.route("/signUp", methods=["POST", "GET"])
def signUp():
    validation_message = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        with open('users.json', 'r') as infile:
            data = json.load(infile)
            
        for user in data:
            if user['email'] == email:
                validation_message = 'Email already exists. Please use a different email address.'
                return render_template('signUp.html', validation_message=validation_message)

        new_user = {"email": email, "pass": password, "user": username}

        data.append(new_user)

        with open('users.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

        return redirect(url_for('login'))

    return render_template('signUp.html', validation_message=validation_message)


@app.route("/login", methods=["POST", "GET"])
def login():
    validation_message = None

    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        with open('users.json', 'r') as infile:
            data = json.load(infile)

        for user in data:
            if user['email'] == email and user['pass'] == password:
                return redirect('/') 

        validation_message = 'Invalid email or password. Please try again.'
        return render_template('login.html', validation_message=validation_message)

    return render_template('login.html', validation_message=validation_message)

@app.route("/category")
def category():
    with open("categories.json", "r") as json_file:
        categories_data = json.load(json_file)
    return flask.render_template("categories.html", categories=categories_data["categories"])