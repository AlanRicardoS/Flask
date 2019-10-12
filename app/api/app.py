from flask import Flask

app = Flask(__name__) #instancia do Flask

@app.route("/") #define uma rota da pagina. No caso a principal 

def index():
    return "Hellow Word!"

if __name__ == "__main__":
    app.run()