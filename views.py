from flask import jsonify,render_template


def configure(app):
    #@app.route("/")
    #def Hello():
    #    return "hello world!"

    #@app.route("/api")
    #def api():
    #    return jsonify(data={'name':'Luan'})

    #@app.route("/langs")
    #def langs():
    #    linguages =['python','java']
    #    return render_template(
    #        'index.html', 
    #        tittle="melhores linguagens",
    #        linguages= linguages
    #    )
    @app.route("/detalhe_problema")
    def detalhe_problema():

        #conexao com o banco de dados para buscarga o problema
        problema ='Deu ruim na agua'
        sub_problema = 'Bueiro entupido'
        responsavel = 'Secretaria Municipal de Urbanismo - SMU'
        obs_cliente = 'O caminhão do lixo não reconhe o lixo há 2 semanas'
        img = 'img/esgoto_1.jpg'

        return render_template(
            'detalhe_problema.html', 
            tittle="Detalhe Problema", 
            problema = problema ,
            sub_problema = sub_problema,
            responsavel = responsavel,
            obs_cliente = obs_cliente,
            imagem = img
        )
    @app.route("/mapa")
    def getmap():
        return render_template(
            'mapa.html'
        )
