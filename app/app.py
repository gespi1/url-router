from flask import Flask, redirect, request
from lib.db.route import Route
import lib.misc.generators as gen

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/generate", methods=["POST"])
def generate():
    return gen.generateUniqueID()

@app.route("/r/<id>", methods=["GET"])
def redirect_external(id):
    r = Route(id)
    link = r.getLink()
    r.closeDBconn()
    return redirect(link, code=302)
