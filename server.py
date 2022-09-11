from flask import Flask, render_template, redirect, request

from users import User
app = Flask(__name__)
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



if __name__ == "__main__":
    app.run(debug=True)