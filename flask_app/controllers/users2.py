from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.users import User


@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("display.html", users=users)

@app.route("/add_user", methods=["POST", "GET"])
def add_user():
    if request.method == "POST":
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"]
        }
        User.save(data)
        return redirect("/add_user")
    else:
        return render_template("form.html")