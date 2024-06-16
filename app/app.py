from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/google", methods=["GET"])
def redirect_external():
    return redirect("https://sentry.io/", code=302)

