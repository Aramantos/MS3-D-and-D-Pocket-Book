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

mongo = PyMongo(app)


@app.route("/")
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("reg-username").lower()})
        if existing_user:
            flash(" - Username already exists - ")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("reg-username").lower(),
            "password": generate_password_hash(request.form.get("reg-password"))
        }
        mongo.db.users.insert_one(register)

        # put new user into 'session cookie'
        session["user"] = request.form.get("reg-username").lower()
        flash(" - Registration successful - ")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("login-register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # checks if username exists in DB
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("log-username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("log-password")):
                session["user"] = request.form.get("log-username").lower()
                flash(" - Welcome, {} - ".format(
                            request.form.get("log-username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash(" - Incorrect Username and/or Password - ")
                return redirect(url_for("login"))
        else:
            # username doesnt exist
            flash(" - Incorrect Username and/or Password - ")
            return redirect(url_for("login"))

    return render_template("login-register.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the DB
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    games = list(mongo.db.games.find())
    characters = list(mongo.db.characters.find())

    if session["user"]:
        return render_template("profile.html", username=username, games=games, 
        characters=characters)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "user" not in session:
        flash(' - There is no user currently logged in - ')
        return render_template("login-register.html")
    if session['user']:
        # remove user from session cookie
        flash(" - You have been logged out - ")
        # session.clear()
        session.pop("user")
        return render_template("login-register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)