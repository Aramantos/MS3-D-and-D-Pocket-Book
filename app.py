import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, abort)
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
                    existing_user["password"], request.form.get(
                        "log-password")):
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

    classes = {}
    for character in characters:
        if session["user"].lower() == character["created_by"].lower():
            if not character["class"] in classes:
                classes[character["class"]] = []
            classes[character["class"]].append(character)

    if session["user"]:
        return render_template(
            "profile.html", username=username, games=games, classes=classes
        )

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "user" not in session:
        flash(' - There is no user currently logged in - ')
        return render_template("login-register.html")
    # remove user from session cookie
    flash(" - You have been logged out - ")
    # session.clear()
    session.pop("user")
    return render_template("login-register.html")


@app.route("/game_add", methods=["GET", "POST"])
def game_add():
    if request.method == "POST":
        game = {
            "game_name": request.form.get("game_name"),
            "created_by": session["user"]
        }
        mongo.db.games.insert_one(game)
        flash(" - Game Successfully Added - ")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("profile.html")


@app.route("/char_add", methods=["GET", "POST"])
def char_add():
    if request.method == "POST":
        char = {
            "character_name": request.form.get("character_name"),
            "class": request.form.get("class"),
            "profile_backstory": "",
            "player_notes": "",
            "combat_spells": "",
            "character_development": "",
            "created_by": session["user"]
        }
        mongo.db.characters.insert_one(char)
        flash(" - Character Successfully Added - ")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("profile.html")


@app.route("/delete_game/<game_id>")
def delete_game(game_id):
    mongo.db.games.remove({"_id": ObjectId(game_id)})
    flash(" - Game Successfully Deleted - ")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/delete_character/<character_id>")
def delete_character(character_id):
    mongo.db.characters.remove({"_id": ObjectId(character_id)})
    flash(" - Character Successfully Deleted - ")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/edit_game/<game_id>", methods=["GET", "POST"])
def edit_game(game_id):
    game = mongo.db.games.find_one_or_404(
        {"_id": ObjectId(game_id)})
    current_name = game["game_name"]

    items = list(mongo.db.items.find())

    return render_template(
        "game.html", current_name=current_name,
        items=items, game_id=game_id)


# @app.route(
#     "/update_session/<session_id>/<game_id>", methods=["GET", "POST"])
# def update_session(session_id, game_id):
#     session = mongo.db.sessions.find_one_or_404(
#         {"_id": ObjectId(session_id)})
#     session_num = session["session_num"]
#     session_desc = session["session_desc"]
#     session_game_name = session["game_name"]
#     created_by = session["created_by"]

#     game = mongo.db.games.find_one_or_404(
#         {"_id": ObjectId(game_id)})
#     game_name = game["game_name"]

#     items = list(mongo.db.items.find())

#     if request.method == "POST":
#         submit = {
#             "session_num": session_num,
#             "session_desc": request.form.get("session-desc-text"),
#             "session_game_name": session_game_name,
#             "created_by": created_by
#         }
#         mongo.db.sessions.update({"_id": ObjectId(session_id)}, submit)
#         flash("Game Session Successfully Updated")

#         return render_template(
#             "game.html", session=session, session_num=session_num,
#             session_desc=session_desc, session_game_name=session_game_name,
#             created_by=created_by, current_name=current_name,
#             game_name=game_name, items=items, game_id=game_id
#         )


@app.route("/item_add/<game_id>", methods=["GET", "POST"])
def item_add(game_id):
    game_name = mongo.db.games.find_one_or_404(
        {"_id": ObjectId(game_id)})["game_name"]
    if request.method == "POST":
        item = {
            "item_name": request.form.get("item_name"),
            "game_name": game_name,
            "created_by": session["user"]
        }
        mongo.db.items.insert_one(item)
        flash(" - Item Successfully Added - ")

        return redirect(url_for("edit_game", game_id=game_id))

    return render_template("profile.html")


@app.route("/delete_item/<item_id>/<game_id>")
def delete_item(item_id, game_id):
    mongo.db.items.remove({"_id": ObjectId(item_id)})
    flash(" - Item Successfully Deleted - ")
    return redirect(url_for("edit_game", game_id=game_id))


@app.route("/edit_character/<character_id>", methods=["GET", "POST"])
def edit_character(character_id):
    character = mongo.db.characters.find_one_or_404(
        {"_id": ObjectId(character_id)})
    character_name = character["character_name"]
    character_class = character["class"]

    return render_template(
        "character.html", character=character,
        character_name=character_name, character_class=character_class)


@app.route("/update_character/<character_id>", methods=["GET", "POST"])
def update_character(character_id):
    character = mongo.db.characters.find_one_or_404(
        {"_id": ObjectId(character_id)})
    character_name = character["character_name"]
    character_class = character["class"]

    if request.method == "POST":
        submit = {
            "character_name": character_name,
            "class": character_class,
            "profile_backstory": request.form.get("char-box-1-text"),
            "player_notes": request.form.get("char-box-2-text"),
            "combat_spells": request.form.get("char-box-3-text"),
            "character_development": request.form.get("char-box-4-text"),
            "created_by": session["user"]
        }
        mongo.db.characters.update({"_id": ObjectId(character_id)}, submit)
        flash("Character Successfully Updated")

    character = mongo.db.characters.find_one({"_id": ObjectId(character_id)})
    return render_template(
        "character.html", character=character,
        character_name=character_name, character_class=character_class)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)