from flask import render_template
from app import app


@app.route("/", defaults={"user":None}) #define uma rota da pagina. No caso a principal 
@app.route("/index/<user>")
def index():
    return render_template("index.html")
