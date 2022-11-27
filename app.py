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


@app.route("/signup")
def create_account():
    """Signup form"""
    form = signup()
    if form.validate_on_submit():
        return redirect(url_for("successful"))
    return render_template(
        "signup.html",
        form=form,
    )


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
