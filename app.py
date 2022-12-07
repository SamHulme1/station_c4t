import os
from forms import signUp, loginToAccount, createShip
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
        admin = mongo.db.admins.find_one(
            {"username": request.form["username"],
                "password": request.form["password"]})

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

        elif admin:
            # if user is admin log in as admin
            # store user in local storage
            session["user"] = request.form["username"]
            flash("Welcome admiral")
        else:
            flash("Unauthorized password/username")
            return redirect(url_for("login"))

    return render_template(
        "login.html",
        form=form,
    )


@app.route("/get_citizens", methods=["GET", "POST"])
def get_citizens():
    # get the citizens stored in the db
    citizens = mongo.db.citizens.find()
    form = createShip()
    if request.method == "POST":
        mongo.db.ships.insert_one({
            "captain": session["user"],
            "shipname": request.form["shipname"],
            "shipcolour": request.form["colour"],
            "ShipCrew": request.form["crew"].strip()
        })
        return redirect(url_for("get_ships"))
    return render_template(
        "citizens.html", citizens=citizens, form=form)


@app.route("/get_ships")
def get_ships():
    # get the ships stored in the db
    ships = mongo.db.ships.find()
    return render_template(
        "ships.html", ships=ships, page_title="ships")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
