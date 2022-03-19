import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
#from flask_wtf import FlaskForm
#from flask_wtf.file import FileField
#from wtforms import SubmitField
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
   import env


app = Flask(__name__)



# Image Upload - Only accept requests that are up to 1MB in size:
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024

# Configure the list of approved file extensions:
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']

# Filenames that do not have one of the approved file extensions will respond with a 400 error.
#filename = uploaded_file.filename
#    if filename != '':
#       file_ext = os.path.splitext(filename)[1]
#       if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
#           abort(400)


#class MyForm(FlaskForm):
#    file = FileField('File')
#    submit = SubmitField('Submit')


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# MongoDB commands: https://www.mongodb.com/developer/quickstart/cheat-sheet/#crud
mongo = PyMongo(app)


# Get the recipes collection
recipes = mongo.db.recipes

# Call the built-in function to assist with debugging: https://realpython.com/lessons/print-and-breakpoint/
#breakpoint()


# Find recipe items that match a condition:
# soups = recipes.find({'category_name': 'Soups'})


# Home Page function

@app.route('/')
@app.route('/home')
def home():
    """Home page displaying background Image & About Section"""
    return render_template('home.html', title="Home")


# Scullery/Recipes Category Section Function

@app.route("/scullery")
def scullery():
    """Scullery page displaying the recipe categories"""
    scullery_categories = mongo.db.scullery_categories.find()
    return render_template("scullery.html")


# Soups Section Function
@app.route("/soups")
def get_soups():
    """Soups page displaying all soup recipes"""
    # Find all of the recipes in the DB that have attribute 'category_name: "Soups"'
    soups = recipes.find({'category_name': 'Soups'})
    return render_template("soups.html", soups=soups)


# Starters Section Function
@app.route("/starters")
def get_starters():
    """Starters page displaying all starter recipes"""
    # Find all of the recipes in the DB that have attribute 'category_name: "Starters"'
    starters = recipes.find({'category_name': 'Starters'})
    return render_template("starters.html", starters=starters)


# Mains Section Function
@app.route("/mains")
def get_mains():
    """Main meals page displaying all 'main' recipes"""
    # Find all of the recipes in the DB that have attribute 'category_name: "Mains"'
    mains = recipes.find({'category_name': 'Mains'})
    return render_template("mains.html", mains=mains)


# Puddings Section Function
@app.route("/puddings")
def get_puddings():
    """Puddings page displaying all pudding recipes"""
    # Find all of the recipes in the DB that have attribute 'category_name: "Puddings"'
    puddings = recipes.find({'category_name': 'Puddings'})
    return render_template("puddings.html", puddings=puddings)



# Add New Recipe Function

@app.route("/new_recipe", methods=["GET", "POST"])
def new_recipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "cooking_time": request.form.get("cooking_time"),
            "recipe_url": request.form.get("recipe_url"),
            "recipe_summary": request.form.get("recipe_summary"),
        }
        
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Added Successfully!")
        return redirect(url_for("scullery"))


    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("new_recipe.html", categories=categories)

# Image Upload New Function

@app.route("/upload_file", methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('new_recipe'))


# Edit Recipe Function

@app.route("/edit_recipe/<recipe_id>",methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)

    submit = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "recipe_method": request.form.get("recipe_method"),
            "cooking_time": request.form.get("cooking_time"),
            "recipe_url": request.form.get("recipe_url"),
            "recipe_summary": request.form.get("recipe_summary"),
            }

    if request.method == "POST":
            mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, {"$set": submit} )
            flash("Your recipe has been edited successfully :)")
    
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)

# VIEW RECIPE

@app.route("/view_recipe/<recipe_id>",methods=["GET"])
def view_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    return render_template("view_recipe.html", recipe=recipe)


# Delete Recipe Function

@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("scullery"))



# Registration Form Functionality - Credit to CI Task Manager project

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")

# Log In Form Functionality - Credit to CI Task Manager project

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
       # check if username exists in db
       existing_user = mongo.db.users.find_one(
           {"username": request.form.get("username").lower()})

       if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
               # invalid password match
               flash("Incorrect Username and/or Password")
               return redirect(url_for("login"))

       else:
           # username doesn't exist
           flash("Incorrect Username and/or Password")
           return redirect(url_for("login"))

    return render_template("login.html")

# Profile Functionality - Credit to CI Task Manager project

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get session user's username from MongoDB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# Log Out Functionality

@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
