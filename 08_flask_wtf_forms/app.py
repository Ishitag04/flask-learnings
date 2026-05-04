from flask import Flask, request, redirect, url_for, render_template, flash
from form import RegistrationForm

app = Flask(__name__)
app.secret_key = "my-secret-key"

@app.route("/",methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Welcome {name}! You registered successfully")
        return render_template("success.html")
    return render_template("register.html",form=form)

@app.route("/success")
def success():
    return render_template("success.html")