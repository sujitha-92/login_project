from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-this-secret-key-before-production"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        # Demo only: connect secure authentication here.
        flash(f"Demo form submitted for {email}. Authentication is not configured yet.")
        return redirect(url_for("login"))
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Demo only: account creation is not connected to a database.
        flash("Demo form submitted. Account creation is not configured yet.")
        return redirect(url_for("signup"))
    return render_template("signup.html")

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        # Demo only: a real app should send a secure, time-limited reset link.
        flash("If this email belongs to an account, reset instructions would be sent.")
        return redirect(url_for("forgot_password"))
    return render_template("forgot_password.html")

if __name__ == "__main__":
    app.run(debug=True)
