import flask 
from flask import render_template , request, url_for
import json
import os

app = flask.Flask("main")

@app.route("/")
def home():
   return render_template("index.html") 


# @app.route("/login")
# def login():
#     return render_template("login.html") 

@app.route("/signUp", methods=["POST", "GET"])
def register():
    validation_message = None

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Load existing users data from JSON file
        with open('users.json', 'r') as infile:
            data = json.load(infile)

        # Check if the email already exists
        for user in data:
            if user['email'] == email:
                validation_message = 'Email already exists. Please use a different email address.'
                break

        # If no validation message, add the new user
        if validation_message is None:
            # Create a new dictionary for the new user
            new_user = {"email": email, "pass": password, "user": username}

            # Append the new user dictionary to the list of users
            data.append(new_user)

            # Write the updated data back to the JSON file
            with open('users.json', 'w') as outfile:
                json.dump(data, outfile, indent=4)
        else:
            # If there's a validation message, render the signUp.html template with the message
            return render_template('signUp.html', validation_message=validation_message)

    # Render the login.html template
    return render_template('login.html', validation_message=validation_message)


@app.route("/login", methods=["POST", "GET"])
def login():
    validation_message = None

    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        # Load existing users data from JSON file
        with open('users.json', 'r') as infile:
            data = json.load(infile)

        # Check if the provided email and password match any user
        for user in data:
            if user['email'] == email and user['pass'] == password:
                # If match found, redirect to home page
                return render_template('index.html', validation_message=validation_message)

        # If no match found, show validation message
        validation_message = 'Invalid email or password. Please try again.'
        return render_template('login.html', validation_message=validation_message)

    # Render the login.html template with validation message
    return render_template('index.html', validation_message=validation_message)

@app.route("/category")
def category():
    with open("categories.json", "r") as json_file:
        categories_data = json.load(json_file)
    return flask.render_template("categories.html", categories=categories_data["categories"])