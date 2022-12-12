import os
from forms import signUp, loginToAccount, createShip, deleteAccount
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import json
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def create_account():
    """Signup form"""
    form = signUp()
    if request.method == "POST":
        existing_captain = mongo.db.users.find_one(
            {"username": request.form["username"]})
    # if method is post search db to see if a
    # name is already on the db with the same name
        if existing_captain:
            flash(f"The user:{existing_captain} already exists")
            return redirect(url_for("create_account"))
    # if name already exists return the users
    #  to the create account page to try again
        if existing_captain is None:
            mongo.db.users.insert_one({
                "username": request.form["username"],
                "password": generate_password_hash(request.form["password"])
            })
    # if the user doesn't exist create
    #  a new user on the db using the form credentials
            session["user"] = request.form["username"]
            flash("account created sucessfully")
            return redirect(url_for("index"))
    # store the user in local storage

    return render_template(
        "signup.html",
        form=form,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    form = loginToAccount()
    if request.method == "POST":
        existing_captain = mongo.db.users.find_one(
            {"username": request.form["username"]})
    # if method is post search db to see if a
    # name is already on the db with the same name
        if existing_captain:
            # check if existinging captin has the correct password to login
            if check_password_hash(
                    existing_captain["password"], request.form["password"]):
                # store user in local storage
                # display message to user after login
                session["user"] = request.form["username"]
                flash(f"Welcome back captain")
            else:
                flash(
                    "Unauthorized password/username, please try again")
                # if user isn't in database tell the user they're unathorized
                return redirect(url_for("login"))
        else:
            flash("Unauthorized password/username")
            return redirect(url_for("login"))

    return render_template(
        "login.html",
        form=form,
    )


@app.route("/logout")
def logout():
    Flask("You have been logged out goodbye")
    session["user"] = ""
    return redirect(url_for("index"))


@app.route("/get_citizens", methods=["GET", "POST"])
def get_citizens():
    citizens = mongo.db.citizens.find()
    form = createShip()
    if request.method == "POST":
        existing_ship = mongo.db.ships.find_one(
            {"shipname": request.form["shipname"]})
        if existing_ship:
            flash(
                "This ship already exists please try naming it something else")
            return redirect(url_for("get_citizens"))
        if existing_ship is None:
            shipCrew = request.form["crew"]
            mongo.db.ships.insert_one({
                "captain": session["user"],
                "shipname": request.form["shipname"],
                "shipcolour": request.form["colour"],
                "ShipCrew": json.loads(shipCrew)
            })
        return redirect(url_for("get_ships"))
    return render_template(
        "citizens.html", citizens=citizens, form=form)


@app.route("/get_ships")
def get_ships():
    # get the ships stored in the db
    userShips = mongo.db.ships.find({"captain": session["user"]})
    allShips = mongo.db.ships.find()
    return render_template(
        "ships.html", userShips=userShips,
        allShips=allShips, page_title="ships")


@app.route("/delete_account", methods=["GET", "POST"])
def delete_account():
    form = deleteAccount()
    if request.method == "POST":
        existing_captain = mongo.db.users.find_one(
            {"username": request.form["username"]})
        if existing_captain:
            if check_password_hash(
                    existing_captain["password"], request.form["password"]):
                flash("user deleted")
                session["user"] = ""
                mongo.db.users.delete_one(
                    {"username": request.form["username"]})
            return redirect(url_for("index"))
        else:
            return redirect(url_for("delete_account"))
    return render_template("delete-account.html", form=form)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
