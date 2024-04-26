import flask 
from flask import render_template , request,redirect, url_for ,session,jsonify,abort
import json
from pythonfile.user import User
app = flask.Flask("main")
app.secret_key = 'Sara'


@app.route("/signUp", methods=["POST", "GET"])
def sign_up():
    validation_message = None
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        error_message = User('users.json').add_user(email, password, username)
        if error_message:
            return render_template('signUp.html', validation_message=error_message)

        return redirect('/')

    return render_template('signUp.html', validation_message=validation_message)

@app.route("/deleteAccount", methods=["POST", "GET"])
def deleteAccount():
    if 'email' in session:
        email = session['email']
        User('users.json').delete_user(email)
        session.pop('email', None)
        return redirect(url_for('signUp'))
    return redirect(url_for('signUp'))
#=============================================================================================#

@app.route("/", methods=["POST", "GET"])
def login():
    validation_message = None

    if 'email' in session:
        return redirect(url_for('home'))

    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        with open('users.json', 'r') as infile:
            data = json.load(infile)

        for user in data:
            if user['email'] == email and user['pass'] == password:
                session['email'] = email
                return redirect(url_for('home'))

        validation_message = 'Invalid email or password. Please try again.'
        return render_template('login.html', validation_message=validation_message)

    return render_template('login.html', validation_message=validation_message)
# #=============================================================================================#

@app.route("/home")
def home():
    if 'email' not in session:
        return redirect('/')  
    else:
        with open("recipes.json", "r") as json_file:
            recipes_data = json.load(json_file)
            return render_template("index.html", recipes=recipes_data["recipes"])
        
#=============================================================================================#

@app.route("/category")
def category():
    with open("categories.json", "r") as json_file:
        categories_data = json.load(json_file)
    return flask.render_template("categories.html", categories=categories_data["categories"])
#=============================================================================================#

@app.route("/recipe-details/<id>")
def recipe_details(id):
    # Load recipes data
    with open("recipes.json", "r") as json_file:
        recipes_data = json.load(json_file)
    
    recipe = None
    for r in recipes_data["recipes"]:
        if r["idMeal"] == id:
            recipe = r
            break
    
    user_email = session.get('email')
    
    is_favorite = False
    
    if user_email:
        with open("users.json", "r") as users_file:
            users_data = json.load(users_file)
        
        user_found = False
        for user in users_data:
            if user["email"] == user_email:
                user_found = True
                break
        
        if user_found:
            favorites = [fav["idMeal"] for fav in user.get("favorites", [])]
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
    
    user_email = session.get('email')
    if not user_email:
        return jsonify({"success": False, "message": "User not logged in"})
    
    with open("users.json", "r") as users_file:
        users_data = json.load(users_file)
    
    user = None
    for u in users_data:
        if u["email"] == user_email:
            user = u
            break
    
    if not user:
        return jsonify({"success": False, "message": "User not found"})
    
    favorites = user.get("favorites", [])
    fav_ids = [fav["idMeal"] for fav in favorites]
    if recipe_id in fav_ids:
        favorites = [fav for fav in favorites if fav["idMeal"] != recipe_id]
        recipe["isFav"] = False
    else:
        favorites.append(recipe)
        recipe["isFav"] = True
    user["favorites"] = favorites
    
    with open("users.json", "w") as users_file:
        json.dump(users_data, users_file, indent=4)
    
    return jsonify({"success": True, "recipe_id": recipe_id})
#=============================================================================================#

@app.route("/fav-recipe")
def fav_list():
    user_email = session.get('email')
    if not user_email:
        return redirect(url_for('login'))
    
    with open("users.json", "r") as users_file:
        users_data = json.load(users_file)
    
    user = None
    for u in users_data:
        if u["email"] == user_email:
            user = u
            break
    
    favorites = user.get("favorites", [])
    
    return render_template("favList.html", favorites=favorites)


#=============================================================================================#

@app.route("/logout", methods=["GET", "POST"])
def logout():
    if 'email' in session:
        session.pop('email')
    return redirect(url_for('login'))

#=============================================================================================#

    
