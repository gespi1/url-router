from flask import Flask, redirect, request, Response
from lib.routes.route import Route
import lib.misc.generators as gen

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/generate", methods=["POST"])
def generate():
    link = request.get_json()["linkTo"]
    id = gen.generateUniqueID()
    r = Route(id)
    r.setLink(link)
    r.createRoute()
    return Response(status="200 OK")

@app.route("/r/<id>", methods=["GET"])
def redirect_external(id):
    r = Route(id)
    link = r.getLink()
    r.closeDBconn()
    return redirect(link, code=302)
