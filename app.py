import os
from forms import (
    SignUp, LoginToAccount, CreateShip,
    DeleteAccount, ChangePassword)
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


@app.route("/myaccount")
def myaccount():
    return render_template("myaccount.html")


@app.route("/signup", methods=["GET", "POST"])
def create_account():
    """Signup form"""
    form = SignUp()
    if request.method == "POST" and form.validate:
        existing_captain = mongo.db.users.find_one(
            {"username": request.form["username"]})
    # if method is post search db to see if a
    # name is already on the db with the same name
        if existing_captain:
            flash("User already exists, please try a differnet username")
            return redirect(url_for("create_account"))
        # if name already exists return the users
        # to the create account page to try again
        else:
            mongo.db.users.insert_one({
                "username": request.form["username"],
                "password": generate_password_hash(request.form["password"])
            })
        # if the user doesn't exist create
        # a new user on the db using the form credentials
            session["user"] = request.form["username"]
            flash("Account created sucessfully")
            return redirect(url_for("index"))
            # store the user in local storage

    return render_template(
        "signup.html",
        form=form,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    """login form"""
    form = LoginToAccount()
    if request.method == "POST" and form.validate:
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
                return redirect(url_for("index"))
            else:
                flash(
                    "Unauthorized password/username, please try again.")
            # if user password or username isn't correct tell them
                return redirect(url_for("login"))
        else:
            flash("Captain doesn't exist, please create an account")
        # if user isn't in database tell them to create an account
            return redirect(url_for("login"))

    return render_template(
        "login.html",
        form=form,
    )


@app.route("/logout")
def logout():
    if is_user_logged_in():
        flash("You have been logged out farewell")
        # tell the user they have been logged out
        logout_user()
        # call the logout method
        return redirect(url_for("index"))


def is_user_logged_in():
    return session.get("user")


def logout_user():
    return session.pop("user", None)


@app.route("/change_password", methods=["GET", "POST"])
def change_password():
    """change password form"""
    form = ChangePassword()
    if request.method == "POST" and form.validate:
        existing_captain = mongo.db.users.find_one(
            {"username": request.form["username"]})
        # search the database a captain with the credentials entered by the
        # user
        if existing_captain:
            if check_password_hash(
                    existing_captain["password"], request.form["password"]):
                # check the users password
                new_password = {
                    "$set": {"password": generate_password_hash(
                        request.form["newpassword"])}}
                # create a newpassword from the data entered
                mongo.db.users.update_one(existing_captain, new_password)
                # update the users password in the database
                flash("Password changed sucessfully please login.")
                # tell the user that their password was changed
                logout_user()
                # log the user out so that they have to enter their new
                # password
                return redirect(url_for("login"))
            else:
                flash("Entered username or password is incorrect.")
            # if the user enters the wrong password tell them that
            # they entered the wrong username or password
        else:
            flask("User doesn't exist please try again.")
        # if the user doesnt exist tell the user
    return render_template("changepassword.html", form=form)


@app.route("/build_ship", methods=["GET", "POST"])
def build_ship():
    citizens = mongo.db.citizens.find()
    """create ship form"""
    form = CreateShip()
    if request.method == "POST" and form.validate:
        existing_ship = mongo.db.ships.find_one(
            {"shipname": request.form["shipname"]})
        # check for existing ships on the database with the same name
        if existing_ship:
            flash(
                "This ship already exists on the station")
            # if the ship exists, tell the user
            return redirect(url_for("build_ship"))
        else:
            shipCrew = request.form["crew"]
            mongo.db.ships.insert_one({
                "captain": session["user"],
                "shipname": request.form["shipname"],
                "shipcolour": request.form["colour"],
                "ShipCrew": json.loads(shipCrew)
            })
            # if the ship doesnt exist create one
            # the data for the ship crew is converted from
            # a string to an array of objects
        return redirect(url_for("get_ships"))
    return render_template(
        "citizens.html", citizens=citizens, form=form)


@app.route("/get_ships")
def get_ships():
    # get the ships stored in the db for the current
    # user based off the session data
    userShips = mongo.db.ships.find({"captain": session["user"]})
    return render_template(
        "ships.html", userShips=userShips, page_title="ships")


@app.route("/delete_account", methods=["GET", "POST"])
def delete_account():
    """delete account form"""
    form = DeleteAccount()
    if request.method == "POST" and form.validate:
        if is_user_logged_in():
            # check if the user is logged in
            existing_captain = mongo.db.users.find_one(
                {"username": request.form["username"]})
            # get data on the current captain based off of entered form data
            if existing_captain:
                if check_password_hash(
                        existing_captain["password"],
                        request.form["password"]):
                    # check the users password
                    flash("user deleted sucessfully")
                    # if the user entered the correct password
                    logout_user()
                    # log the userout of session
                    mongo.db.users.delete_one(
                        {"username": request.form["username"]})
                    # delete the user from the database
                    mongo.db.ships.delete_many(
                        {"captain": request.form["username"]})
                    # delete all the ships the user created
                    return redirect(url_for("index"))
                else:
                    flash(
                        "Incorrect username/password, could not delete.")
                    # if the password is incorrect tell the user
            else:
                return redirect(url_for("delete_account"))
        else:
            flash("Delete unsuccessful, no user currently logged in.")
            # if no user is logged in tell the user
            return redirect(url_for("index"))
    return render_template("delete-account.html", form=form)


# route for error 404
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
