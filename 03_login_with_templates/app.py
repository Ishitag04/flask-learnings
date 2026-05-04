from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # if username=="123" and password=="pass":
    #     return render_template("welcome.html", name=username)

    valid_credentials = {
        'admin' : '123',
        'Ishita' : 'pass',
        'Rajat' : 'Raj'
    }

    if username in valid_credentials and password == valid_credentials[username]:
        return render_template("welcome.html", name=username)
    else:
        return "Invalid credentials"