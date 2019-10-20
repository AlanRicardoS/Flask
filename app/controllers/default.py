from flask import render_template
from app import app


@app.route("/") #define uma rota da pagina. No caso a principal 
@app.route("/index")
def index():
    return "index.html"
