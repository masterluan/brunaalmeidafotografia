import views
import db

from flask import Flask

def create_app():
    app = Flask(__name__) #templates folder sao html e statics javascript/css etc.. se nao informar nada ele pega o nome padrao
    
    db.configure(app)
    
    views.configure(app)
    
    #admin.configure(app)

    #configurar funçoes
    #contact.configure(app)
    
    #variaveis 
    app.config['SECRET_KEY']='HSUAHSUHAFUUHDHA'
    return app

