import os
from forms import signup
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
    form = signup()
    # form signup form from forms
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
            password = request.form["password"]
            mongo.db.users.insert_one({
                "username": request.form["username"],
                "password": generate_password_hash(request.form["password"])
            })
    # if the user doesn't exist create
    #  a new user on the db using the form credentials

            session["user"] = request.form.get("username")
            flash("account created sucessfully")
            return redirect(url_for("index"))
    # store the user in local storage

    return render_template(
        "signup.html",
        form=form,
    )


@app.route("/get_citizens")
def get_citizens():
    # get the citizens stored in the db
    citizens = mongo.db.citizens.find()
    return render_template(
        "citizens.html", citizens=citizens, page_title="citizens")


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
