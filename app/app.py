from flask import Flask, redirect, request, Response
from flask_cors import CORS
from lib.routes.route import Route
import lib.misc.generators as gen

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

# generate a route to a link
@app.route("/generate", methods=["POST"])
def generate():
    link = request.get_json()["linkto"]
    r = Route()
    r.setLink(link)
    r.createRoute()
    r.closeDBconn()
    return Response(status="200 OK")

# redirect to route url 
@app.route("/r/<id>", methods=["GET"])
def redirect_external(id):
    r = Route()
    r.setId(id)
    link = r.getLink()
    r.closeDBconn()
    return redirect(link, code=302)
