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
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        existing_cptn = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_cptn:
            flash("Captain already exists")
            return redirect(url_for("signup"))

        create_account = {
            "profile_picture": request.form.get("profile_picture"),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(create_account)

        current_cptn["user"] = request.form.get("username").lower()
        flash("Welcome appord captain {current_cptn}")
    return render_template("signup.html")


@app.route("/get_citizens")
def get_citizens():
    citizens = mongo.db.citizens.find()
    return render_template(
        "citizens.html", citizens=citizens, page_title="citizens")


@app.route("/get_ships")
def get_ships():
    ships = mongo.db.ships.find()
    return render_template(
        "ships.html", ships=ships, page_title="ships")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
