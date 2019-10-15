from app import app

@app.route("/") #define uma rota da pagina. No caso a principal 

def index():
    return "Hellow Word!"
