from flask import request, render_template, jsonify #Permite rodar os HTMLs criados, assim exibindo as informações do Banco em uma págine WEB
from database.db import db
from models.produto import Produto


#Irá rodar o pag WEB a fim de exibir o CRUD do banco
def produtoHtmlController():
    if request.method == 'GET':
         return render_template('TesteCRUDS/CRUDProduto.html')


#Essa função contém o CRUD completo da tabela "produto"
def produtoController():

    # POST
    # ----------------------------------------------------------------------------------------------------------------------------------
    if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                user = Produto(data['codigo'], data['descricao'], data['codCategoria'], data['codClassificacao'], data['codMarca'], data['preco'], data['foto1'])
                db.session.add(user)
                db.session.commit()  #manda as informações para o banco de dados
                return 'produto criada com sucesso', 200
            except Exception as e:
                return 'Não foi possível criar uma nova produto{}'.format(str(e)), 405
    


    #GET
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'GET':
        try:
            codigo = request.args.get('codigo')
            descricao = request.args.get('descricao')
            codCategoria = request.args.get('codCategoria')
            codClassificacao = request.args.get('codClassificacao')
            codMarca = request.args.get('descricao')
            preco = request.args.get('preco')
            foto1 = request.args.get('foto1')
            query = Produto.query

            if codigo:
                query = query.filter_by(codigo=codigo)
            if descricao:
                query = query.filter(Produto.descricao.like(f"%{descricao}%"))
            if codCategoria:
                query = query.filter(Produto.codCategoria.like(f"%{codCategoria}%"))
            if codClassificacao:
                query = query.filter(Produto.codClassificacao.like(f"%{codClassificacao}%"))
            if codMarca:
                query = query.filter(Produto.codMarca.like(f"%{codMarca}%"))
            if preco:
                query = query.filter(Produto.preco.like(f"%{preco}%"))
            if foto1:
                query = query.filter(Produto.foto1.like(f"%{foto1}%"))
            produto = query.all()
            results = [{'codigo': cat.codigo, 'descricao': cat.descricao, 'codCategoria': cat.codCategoria, 'codClassificacao': cat.codClassificacao, 'codMarca': cat.codMarca, 'preco': cat.preco, 'foto1': cat.foto1} for cat in produto]
            return jsonify(results), 200
        except Exception as e:
            return 'Erro ao buscar categorias: {}'.format(str(e)), 405
    


    # PUT
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'PUT':
          try:
              id_produto = int(request.args.to_dict().get('codigo'))
              data = request.get_json()
              print(id_produto)

              produto = Produto.query.get(id_produto)
              if produto is None: #Caso o número seja inválido, um erro é informado
                  return {'error': 'produto não encontrada'}, 404
              print(data)
              #Se não, os campos de codigo e descrição são atualizados com novas informações digitadas pelo usuário
              produto.descricao = data.get('descricao', produto.descricao)
              produto.codCategoria = data.get('codCategoria', produto.codCategoria)
              produto.codClassificacao = data.get('codClassificacao', produto.codClassificacao)
              produto.codMarca = data.get('codMarca', produto.codMarca)
              produto.preco = data.get('preco', produto.preco)
              produto.foto1 = data.get('foto1', produto.foto1) 
              print(produto.codigo, produto.descricao, produto.codCategoria, produto.codClassificacao, produto.codMarca, produto.preco, produto.foto1)
              db.session.commit() #Finaliza o processo
              return {
                   "message": "Produto atualizada com sucesso",
                   "status": 200
              }
          except Exception as e:
              return 'Não foi possível atualizar a produto. ERRO:{}'.format(str(e)),405



    # DELETE
    # ----------------------------------------------------------------------------------------------------------------------------------
    elif request.method == 'DELETE':
        try:
            data = int(request.args.to_dict().get('codigo'))
            produto = Produto.query.get(data)
            if produto is None: 
                return {'error': 'Produto não encontrada'}, 404
            db.session.delete(produto)
            db.session.commit()
            return 'Produto deletada com sucesso', 200
        except Exception as e:
            return 'Não foi possível deletar o produto. ERRO: {}'.format(str(e)), 405 