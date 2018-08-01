from flask import render_template


def configure(app):

    @app.route("/")
    def pagina_inicial():
        return render_template('index.html')
        
    @app.route("/portifolio")
    def portifolio():

        #conexao com o banco de dados para buscarga o problema
    
        return render_template(
            'portifolio.html', 
            problema = problema ,
        
        )
