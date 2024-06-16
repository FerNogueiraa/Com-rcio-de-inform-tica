from flask import request, render_template, jsonify #Permite rodar os HTMLs criados, assim exibindo as informações do Banco em uma págine WEB
from database.db import db
from models.classificacao import Classificacao


#Irá rodar o pag WEB a fim de exibir o CRUD do banco
def classificacaoHtmlController():
    if request.method == 'GET':
         return render_template('FrontEnd/cadastroClassificacao.html')
    return render_template('FrontEnd/cadastroClassificacao.html')


#Essa função contém o CRUD completo da tabela "classificacao"
def classificacaoController():

    # POST
    # ----------------------------------------------------------------------------------------------------------------------------------
    if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                user = Classificacao(data['codigo'], data['nome'])
                db.session.add(user)
                db.session.commit()  #manda as informações para o banco de dados
                return 'Classificação criada com sucesso', 200
            except Exception as e:
                return 'Não foi possível criar uma nova classificação{}'.format(str(e)), 405
    

    #GET
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'GET':
        try:
            codigo = request.args.get('codigo')
            nome = request.args.get('nome')
            query = Classificacao.query

            if codigo:
                query = query.filter_by(codigo=codigo)
            if nome:
                query = query.filter(Classificacao.nome.like(f"%{nome}%"))

            classificacao = query.all()
            results = [{'codigo': cat.codigo, 'nome': cat.nome} for cat in classificacao]
            return jsonify(results), 200
        except Exception as e:
            return 'Erro ao buscar pelas classificações: {}'.format(str(e)), 405
    

    # PUT
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'PUT':
          try:
              id_classificacao = int(request.args.to_dict().get('codigo'))
              data = request.get_json()
              print(id_classificacao)

              classificacao = Classificacao.query.get(id_classificacao)
              if classificacao is None: #Caso o número seja inválido, um erro é informado
                  return {'error': 'Classificação não encontrada'}, 404
              print(data)
              classificacao.nome = data.get('nome', classificacao.nome)
              print(classificacao.codigo, classificacao.nome)
              db.session.commit() #Finaliza o processo
              return {
                   "message": "Classificação atualizada com sucesso",
                   "status": 200
              }
          except Exception as e:
              return 'Não foi possível atualizar a classificação. ERRO:{}'.format(str(e)),405


    # DELETE
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'DELETE':
        try:
            data = int(request.args.to_dict().get('codigo'))
            classificacao = Classificacao.query.get(data)
            if classificacao is None: 
                return {'error': 'Classificação não encontrada'}, 404
            db.session.delete(classificacao)
            db.session.commit()
            return 'Classificação deletada com sucesso', 200
        except Exception as e:
            return 'Não foi possível deletar a classificação. ERRO: {}'.format(str(e)), 405 