import flask 
from flask import render_template , request,redirect, url_for ,session,jsonify,abort
import json
from pythonfile.user import User


app = flask.Flask("main")

app.secret_key = 'Sara'

#routing to signUp page
@app.route("/signUp", methods=["POST", "GET"])
def sign_up():
    validation_message = None
    session.pop('email', None)
    
    # Handle POST request when user submits sign-up form
    if request.method == "POST":
        # Retrieve data from the form
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        # Add user to the database
        error_message = User('users.json', email).add_user(password, username)
        
        # If there's  error message, render the sign-up page with the error message
        if error_message:
            return render_template('signUp.html', validation_message=error_message)
        
                

        # Clear the session
        session.clear()
        
        # Redirect to the login page after successful sign-up
        return redirect(url_for('login'))

    return render_template('signUp.html', validation_message=validation_message)


#=============================================================================================#


@app.route("/deleteAccount", methods=["POST", "GET"])
def deleteAccount():

    # Check if email exists in the session
    email = session.get('email') 
    if email:
        # Delete user from the database
        User('users.json', email).delete_user()
        
        # Remove email from the session
        session.pop('email', None)        
        # Clear the session
        session.clear()
    
    return redirect(url_for('signUp'))


#=============================================================================================#

#routing to login page
@app.route("/", methods=["POST", "GET"])
def login():
    validation_message = None

    # If user is already logged in, go the home page
    if 'email' in session:
        return redirect(url_for('home'))

    # Handle login form submission
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        # Read user data from the JSON file
        with open('users.json', 'r') as infile:
            data = json.load(infile)

        # Check if the provided email and password match any user in the data
        for user in data:
            if user['email'] == email and user['pass'] == password:
                # If match is found, set the email in the session and redirect to the home page
                session['email'] = email
                return redirect(url_for('home'))

        # If no match is found, display validation message
        validation_message = 'Invalid email or password. Please try again.'

    return render_template('login.html', validation_message=validation_message)


# #=============================================================================================#

#routing to login page
@app.route("/home")
def home():
    # Check  user if not logged in redirect to the login page
    if 'email' not in session:
        return redirect('/')  
    
    else:
        # Read recipes data from the JSON file
        with open("recipes.json", "r") as json_file:
            recipes_data = json.load(json_file)
            
            return render_template("index.html", recipes=recipes_data["recipes"])

        
#=============================================================================================#

#routing to all category page
@app.route("/category")
def category():
    # Open and read the categories  from the JSON file
    with open("categories.json", "r") as json_file:
        categories_data = json.load(json_file)
    
    return flask.render_template("categories.html", categories=categories_data["categories"])

#=============================================================================================#
#routing to categoty page
@app.route("/category/<category_name>")
def category_name(category_name):

    # Open and read the recipes data from the JSON file
    with open("recipes.json", "r") as json_file:
        recipes_data = json.load(json_file)
    
    filtered_recipes = []
    
    # Iterate over each recipe in the recipes data
    for recipe in recipes_data["recipes"]:
        # Check if the category of the recipe matches the provided category name
        if recipe["strCategory"] == category_name:
            filtered_recipes.append(recipe)
    
    return render_template("categoryDetails.html", recipes=filtered_recipes)

#=============================================================================================#
@app.route("/recipe-details/<id>")
def recipe_details(id):
    # load the recipes  
    with open("recipes.json", "r") as json_file:
        recipes_data = json.load(json_file)
    
        recipe = None
    
    # Iterate recipe in the recipes data
    for r in recipes_data["recipes"]:
        # Check if the ID of the recipe matches the provided ID
        if r["idMeal"] == id:
            recipe = r
            break
    
    # get the user's email from the session
    user_email = session.get('email')
    
    is_favorite = False
    
    # Check if the user is logged in
    if user_email:
        # Open and read the users data from the JSON file
        with open("users.json", "r") as users_file:
            users_data = json.load(users_file)
        
        # Iterate  each user in the users data
        user_found = False
        for user in users_data:
            # Check if the email of the user matches the user's email in the session
            if user["email"] == user_email:
                user_found = True
                break
        
        # If the user is found
        if user_found:
            # Retrieve the list of favorite recipe IDs for the user
            favorites = [fav["idMeal"] for fav in user.get("favorites", [])]
            
            # Check if the ID of the current recipe is in the list of favorites
            is_favorite = recipe["idMeal"] in favorites
    
    return render_template("recipeDetails.html", data=recipe, is_favorite=is_favorite)


#=============================================================================================#


@app.route("/add-to-fav/<recipe_id>", methods=["POST"])
def add_to_fav(recipe_id):
    # Load recipes data
    with open("recipes.json", "r") as json_file:
        recipes_data = json.load(json_file)
    
    # Find the recipe by recipe_id
    recipe = None
    for r in recipes_data["recipes"]:
        if r["idMeal"] == recipe_id:
            recipe = r
            break
    
    # get user's email from session
    user_email = session.get('email')
    
    # Check if user is logged in
    if not user_email:
        return jsonify({"success": False, "message": "User not logged in"})
    
    # Load users data
    with open("users.json", "r") as users_file:
        users_data = json.load(users_file)
    
    # Find the user by email
    user = None
    for u in users_data:
        if u["email"] == user_email:
            user = u
            break
    
    # If user not found, return error
    if not user:
        return jsonify({"success": False, "message": "User not found"})
    
    # Get user's favorites and their IDs
    favorites = user.get("favorites", [])
    fav_ids = [fav["idMeal"] for fav in favorites]
    
    # If recipe is already in favorites, remove it, otherwise add it
    if recipe_id in fav_ids:
        favorites = [fav for fav in favorites if fav["idMeal"] != recipe_id]
        recipe["isFav"] = False
    else:
        favorites.append(recipe)
        recipe["isFav"] = True
    
    # Update user's favorites
    user["favorites"] = favorites
    
    # Write updated users data back to the file
    with open("users.json", "w") as users_file:
        json.dump(users_data, users_file, indent=4)
    
    return jsonify({"success": True, "recipe_id": recipe_id})

#=============================================================================================#

@app.route("/fav-recipe")
def fav_list():
    # Check if user is logged in
    user_email = session.get('email')
    if not user_email:
        return redirect(url_for('login'))
    
    # Load users data
    with open("users.json", "r") as users_file:
        users_data = json.load(users_file)
    
    # Find the user by email
    user = next((u for u in users_data if u["email"] == user_email), None)
    
    # Get user's favorites
    favorites = user.get("favorites", [])
    
    return render_template("favList.html", favorites=favorites)


#=============================================================================================#

@app.route("/logout", methods=["GET", "POST"])
def logout():
    # Check if user is logged in
    if 'email' in session:
        # Remove email from session
        session.pop('email')
    
    return redirect(url_for('login'))


#=============================================================================================#

    
