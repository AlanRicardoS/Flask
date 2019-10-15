from flask import Flask

app = Flask(__name__) #instancia do Flask

from app.controllers import default 


