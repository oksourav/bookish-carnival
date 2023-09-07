from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, template_folder="template")

app.secret_key = "feel_the_ocean_as_it_breathes"


@app.route("/", methods=["GET"])
def home():
    try:
        if "username" in session:
            return redirect(url_for("dashboard"))
        else:
            return render_template("index.html")

    except:
        return render_template("unauthorised.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]

            # Dummy user validation
            if username == "admin" and password == "secretpassword":
                session["username"] = username
                return redirect(url_for("dashboard"))
            else:
                return render_template("index.html")
        else:
            return render_template("index.html")
    except:
        return render_template("unauthorised.html")


@app.route("/dashboard", methods=["GET"])
def dashboard():
    try:
        if "username" in session:
            username = session["username"]
            if username == "admin":
                return render_template("admin.html")
            else:
                return render_template("index.html")
        else:
            return render_template("index.html")
    except:
        return render_template("unauthorised.html")


@app.route("/view_file", methods=["GET"])
def viewFile():
    try:
        if "username" in session:
            username = session["username"]
            if username == "admin":
                return render_template("files.html")
            else:
                return render_template("index.html")
        else:
            return render_template("index.html")
    except:
        return render_template("unauthorised.html")


@app.route("/profile", methods=["GET"])
def profile():
    try:
        if "username" in session:
            username = session["username"]
            if username == "admin":
                return render_template("profile.html")
            else:
                return render_template("index.html")
        else:
            return render_template("index.html")
    except:
        return render_template("unauthorised.html")


@app.route("/admin_flag", methods=["GET"])
def getAdminFlag():
    try:
        if "username" in session:
            username = session["username"]
            if username == "admin":
                return render_template("adminflag.html")
            else:
                return render_template("index.html")
        else:
            return render_template("index.html")
    except:
        return render_template("unauthorised.html")


@app.route("/logout")
def logout():
    try:
        session.pop("username", None)
        return redirect(url_for("home"))
    except:
        return render_template("unauthorised.html")


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True)
