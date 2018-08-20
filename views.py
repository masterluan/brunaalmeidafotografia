from flask import render_template


def configure(app):

    @app.route("/")
    def pagina_inicial():
        return render_template('index.html')

    @app.route("/port_criancas")
    def port_criancas():
        #conexao com o banco de dados para buscarga o problema
        return render_template(
            'port_criancas.html'#, 
          #  problema = problema ,
        
        )
   # @app.route("/port_casais")
   # def port_casais():
        #conexao com o banco de dados para buscarga o problema
    #    return render_template(
     #       'port_casais.html'#, 
          #  problema = problema ,
        
     #   )
    # @app.route("/port_mulheres")
    #def port_mulheres():
        #conexao com o banco de dados para buscarga o problema
    #    return render_template(
    #        'port_mulheres.html'#, 
          #  problema = problema ,
        
    #    )
    @app.route("/sobre")
    def sobre():
        #conexao com o banco de dados para buscarga o problema
        return render_template(
            'sobre.html'#, 
          #  problema = problema ,
        
       )
    @app.route("/contato")
    def contato():
        #conexao com o banco de dados para buscarga o problema
        return render_template(
            'contato.html'#, 
          #  problema = problema ,
        
        )