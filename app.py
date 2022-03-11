import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
   import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


# MongoDB commands: https://www.mongodb.com/developer/quickstart/cheat-sheet/#crud
mongo = PyMongo(app)


# Get the recipes collection
recipes = mongo.db.recipes

# Call the built-in function to assist with debugging: https://realpython.com/lessons/print-and-breakpoint/
#breakpoint()


# Find recipe items that match a condition
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
    scullery_categories = mongo.db.scullery_categories.find()
    return render_template("scullery.html")


# Soups Section Function
@app.route("/soups")
def get_soups():
    # Find all of the recipes in the DB that have attribute 'category_name: "Soups"'
    soups = recipes.find({'category_name': 'Soups'})
    return render_template("soups.html", soups=soups)


# Starters Section Function
@app.route("/starters")
def get_starters():
    # Find all of the recipes in the DB that have attribute 'category_name: "Starters"'
    starters = recipes.find({'category_name': 'Starters'})
    return render_template("starters.html", starters=starters)


# Mains Section Function
@app.route("/mains")
def get_mains():
    # Find all of the recipes in the DB that have attribute 'category_name: "Mains"'
    mains = recipes.find({'category_name': 'Mains'})
    return render_template("mains.html", mains=mains)


# Puddings Section Function
@app.route("/puddings")
def get_puddings():
    # Find all of the recipes in the DB that have attribute 'category_name: "Puddings"'
    puddings = recipes.find({'category_name': 'Puddings'})
    return render_template("puddings.html", puddings=puddings)


###################################################################################

# Add New Recipe Function

@app.route("/new_recipe")
def new_recipe():
    return render_template("new_recipe.html", page_title="new_recipe")

###################################################################################

# Edit Recipe Function




###################################################################################

# Delete Recipe Function




###################################################################################

# Manage Scullery/Admin Only Function




###################################################################################


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
