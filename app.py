from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username and password:
            message = f"Welcome, {username}!"
        else:
            message = "Error: Please fill both Username and Password fields."
    return render_template("login.html", message=message)


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        msg = request.form.get("message")
        return render_template("result.html", name=name, email=email, message=msg)
    return render_template("feedback.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        return "You submitted data via POST method."
    else:
        return "You accessed this page using GET method."

if __name__ == "__main__":
    app.run(debug=True)
