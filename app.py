import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, abort)
from datetime import date
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ['MONGO_DBNAME']
app.config["MONGO_URI"] = os.environ['MONGO_URI']
app.secret_key = os.environ['SECRET_KEY']

mongo = PyMongo(app)


@app.route("/")
@app.route("/homepage", methods=["GET", "POST"])
def homepage():
    if is_authenticated():

        # grab the session user's username from the DB
        username = mongo.db.users.find_one_or_404(
            {"username": session["user"]})["username"]

        games = list(mongo.db.games.find())
        characters = list(mongo.db.characters.find())

        classes = {}
        for character in characters:
            if session["user"].lower() == character["created_by"].lower():
                if not character["class"] in classes:
                    classes[character["class"]] = []
                classes[character["class"]].append(character)

        return render_template(
            "profile.html", username=username, games=games, classes=classes
        )

    return render_template("login-register.html")


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
            "password": generate_password_hash(
                request.form.get("reg-password"))
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
        existing_user = mongo.db.users.find_one_or_404(
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
    if not is_authenticated():
        flash(' - There is no user currently logged in - ')
        return render_template("login-register.html")

    # grab the session user's username from the DB
    username = mongo.db.users.find_one_or_404(
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
    if not is_authenticated():
        flash(' - There is no user currently logged in - ')
        return render_template("login-register.html")

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
    if not is_authenticated():
        flash(' - There is no user currently logged in - ')
        return render_template("login-register.html")

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
    if not is_authenticated():
        flash(' - There is no user currently logged in - ')
        return render_template("login-register.html")

    if not is_object_id_valid(game_id):
        abort(404)

    result = mongo.db.games.remove({"_id": ObjectId(game_id)})
    if result['n'] > 0:
        flash(" - Game Successfully Deleted - ")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/delete_character/<character_id>")
def delete_character(character_id):
    if not is_authenticated():
        flash(' - There is no user currently logged in - ')
        return render_template("login-register.html")

    if not is_object_id_valid(character_id):
        abort(404)

    result = mongo.db.characters.remove({"_id": ObjectId(character_id)})
    if result['n'] > 0:
        flash(" - Character Successfully Deleted - ")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/edit_game/<game_id>", methods=["GET", "POST"])
def edit_game(game_id):
    if not is_authenticated():
        flash(' - There is no user currently logged in - ')
        return render_template("login-register.html")

    if not is_object_id_valid(game_id):
        abort(404)

    game = mongo.db.games.find_one_or_404(
        {"_id": ObjectId(game_id)})
    current_name = game["game_name"]

    sessions = list(mongo.db.sessions.find())
    session_id = request.args.get('session_id')
    game_session = None
    if is_object_id_valid(session_id):
        game_session = mongo.db.sessions.find_one_or_404(
            {"_id": ObjectId(session_id)}
        )

    items = list(mongo.db.items.find())
    item_id = request.args.get('item_id')
    item = None
    if is_object_id_valid(item_id):
        item = mongo.db.items.find_one_or_404({"_id": ObjectId(item_id)})

    return render_template(
        "game.html", current_name=current_name,
        items=items, game_id=game_id, sessions=sessions,
        item=item, game_session=game_session, game=game)


@app.route("/add_session/<game_id>", methods=["GET", "POST"])
def add_session(game_id):
    today = date.today()
    sess_date = today.strftime("%d/%m/%Y")
    if request.method == "POST":
        submit = {
            "session_num": request.form.get("session_num"),
            "session_name": request.form.get("new-session-name"),
            "session_date": sess_date,
            "session_desc": "",
            "game_name": request.form.get("game_name"),
            "created_by": session["user"]
        }
        mongo.db.sessions.insert_one(submit)
        flash(" - Session Successfully Added - ")

        return redirect(url_for("edit_game", game_id=game_id))
    return redirect(request.url)


@app.route("/update_session/<game_id>", methods=["GET", "POST"])
def update_session(game_id):
    if request.method == "POST":
        session_id = request.form.get("session-id-hidden")
        sess = mongo.db.sessions.find_one({"_id": ObjectId(session_id)})
        submit = {
            "session_num": sess["session_num"],
            "session_name": sess["session_name"],
            "session_date": sess["session_date"],
            "session_desc": request.form.get("session-desc-text"),
            "game_name": sess["game_name"],
            "created_by": session["user"]
        }
        mongo.db.sessions.update({"_id": ObjectId(session_id)}, submit)
        flash(" - Session Successfully Updated - ")

        return redirect(url_for("edit_game", game_id=game_id))
    return redirect(request.url)


@app.route("/item_add/<game_id>", methods=["GET", "POST"])
def item_add(game_id):
    if not is_authenticated():
        flash(' - There is no user currently logged in - ')
        return render_template("login-register.html")

    if not is_object_id_valid(game_id):
        abort(404)

    game_name = mongo.db.games.find_one_or_404(
        {"_id": ObjectId(game_id)})["game_name"]

    if request.method == "POST":
        item = {
            "item_name": request.form.get("item_name"),
            "item_desc": "",
            "game_name": game_name,
            "created_by": session["user"]
        }
        mongo.db.items.insert_one(item)
        flash(" - Item Successfully Added - ")

        return redirect(url_for("edit_game", game_id=game_id))

    return render_template("profile.html")


@app.route("/update_item/<game_id>", methods=["GET", "POST"])
def update_item(game_id):
    print("test")
    if request.method == "POST":
        item_id = request.form.get("item-id-hidden")
        item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
        submit = {
            "item_name": item["item_name"],
            "item_desc": request.form.get("item-overview-text"),
            "game_name": item["game_name"],
            "created_by": session["user"]
        }
        mongo.db.items.update({"_id": ObjectId(item_id)}, submit)
        flash(" - Item Successfully Updated - ")

        return redirect(url_for("edit_game", game_id=game_id))
    return redirect(request.url)


@app.route("/delete_item/<item_id>/<game_id>")
def delete_item(item_id, game_id):
    result = mongo.db.items.remove({"_id": ObjectId(item_id)})
    if result['n'] > 0:
        flash(" - Item Successfully Deleted - ")
    return redirect(url_for("edit_game", game_id=game_id))


@app.route("/edit_character/<character_id>", methods=["GET", "POST"])
def edit_character(character_id):
    if not is_authenticated():
        flash(' - There is no user currently logged in - ')
        return render_template("login-register.html")

    if not is_object_id_valid(character_id):
        abort(404)

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
        flash(" - Character Successfully Updated - ")

    return render_template(
        "character.html", character=character,
        character_name=character_name, character_class=character_class)


@app.route("/get_items")
def get_items():
    if not is_authenticated():
        flash(' - There is no user currently logged in - ')
        return render_template("login-register.html")

    items = list(mongo.db.items.find())
    return render_template("items.html", items=items)


@app.route("/search_items", methods=["GET", "POST"])
def search_items():
    query = request.form.get("query")
    items = list(mongo.db.items.find({"$text": {"$search": query}}))
    return render_template("items.html", items=items)


@app.route("/edit_item/<item_id>", methods=["GET", "POST"])
def edit_item(item_id):
    if not is_authenticated():
        flash(' - There is no user currently logged in - ')
        return render_template("login-register.html")

    if not is_object_id_valid(item_id):
        abort(404)

    if request.method == "POST":
        submit = {
            "item_name": request.form.get("item_name_edit"),
            "item_desc": request.form.get("item_overview_edit"),
            "game_name": request.form.get("game_name_edit"),
            "created_by": session["user"]
        }
        mongo.db.items.update({"_id": ObjectId(item_id)}, submit)
        flash(" - Item Successfully Updated - ")
        items = list(mongo.db.items.find())
        return render_template("items.html", items=items)

    item = mongo.db.items.find_one({"_id": ObjectId(item_id)})
    return render_template("edit-item.html", item=item)


@app.route("/get_sessions")
def get_sessions():
    if not is_authenticated():
        flash(' - There is no user currently logged in - ')
        return render_template("login-register.html")

    sessions = list(mongo.db.sessions.find())
    return render_template("sessions.html", sessions=sessions)


@app.route("/search_sessions", methods=["GET", "POST"])
def search_sessions():
    query = request.form.get("query")
    sessions = list(mongo.db.sessions.find({"$text": {"$search": query}}))
    return render_template("sessions.html", sessions=sessions)


@app.route("/edit_session/<session_id>", methods=["GET", "POST"])
def edit_session(session_id):
    if not is_authenticated():
        flash(' - There is no user currently logged in - ')
        return render_template("login-register.html")

    if not is_object_id_valid(session_id):
        abort(404)

    if request.method == "POST":
        submit = {
            "session_num": request.form.get("session_num_edit"),
            "session_name": request.form.get("session_name_edit"),
            "session_date": request.form.get("session_date_edit"),
            "session_desc": request.form.get("session_desc_edit"),
            "game_name": request.form.get("game_name_edit"),
            "created_by": session["user"]
        }
        mongo.db.sessions.update({"_id": ObjectId(session_id)}, submit)
        flash(" - Session Successfully Updated - ")
        sessions = list(mongo.db.sessions.find())
        return render_template("sessions.html", sessions=sessions)

    sess = mongo.db.sessions.find_one({"_id": ObjectId(session_id)})
    return render_template("edit-session.html", sess=sess)


def is_object_id_valid(id_value):
    """ Validate is the id_value is a valid ObjectId
    """
    return id_value != "" and ObjectId.is_valid(id_value)


def is_authenticated():
    """ Ensure that user is authenticated
    """
    return 'user' in session


# Custom Error Handling
# 404 Error Page not found
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# 500 Error Server Error
@app.errorhandler(500)
def internal_server(error):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
