from flask import request, render_template, jsonify
from database.db import db
from models.produto import Produto


def produtoHtmlController():
    if request.method == 'GET':
         return render_template('FrontEnd/cadastroProduto.html')
    return render_template('FrontEnd/cadastroProduto.html')


def produtoController():
    if request.method == 'POST':
            try:
                data = request.get_json()
                print(data)
                produto = Produto(data['codigo'], data['descricao'], data['codCategoria'], data['codClassificacao'], data['codMarca'], data['preco'], data['foto1'])
                db.session.add(produto)
                db.session.commit()
                return 'Produto criado com sucesso', 200
            except Exception as e:
                return 'Não foi possível criar um novo produto: {}'.format(str(e)), 405

    elif request.method == 'GET':
        try:
            codigo = request.args.get('codigo')
            descricao = request.args.get('descricao')
            codCategoria = request.args.get('codCategoria')
            codClassificacao = request.args.get('codClassificacao')
            codMarca = request.args.get('codMarca')
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
            produtos = query.all()
            results = [{'codigo': produto.codigo, 'descricao': produto.descricao, 'codCategoria': produto.codCategoria, 'codClassificacao': produto.codClassificacao, 'codMarca': produto.codMarca, 'preco': produto.preco, 'foto1': produto.foto1} for produto in produtos]
            return jsonify(results), 200
        except Exception as e:
            return 'Erro ao buscar produtos: {}'.format(str(e)), 405

    elif request.method == 'PUT':
          try:
              id_produto = int(request.args.to_dict().get('codigo'))
              data = request.get_json()
              print(id_produto)

              produto = Produto.query.get(id_produto)
              if produto is None:
                  return {'error': 'Produto não encontrado'}, 404
              
              produto.descricao = data.get('descricao', produto.descricao)
              produto.codCategoria = data.get('codCategoria', produto.codCategoria)
              produto.codClassificacao = data.get('codClassificacao', produto.codClassificacao)
              produto.codMarca = data.get('codMarca', produto.codMarca)
              produto.preco = data.get('preco', produto.preco)
              produto.foto1 = data.get('foto1', produto.foto1) 
              print(produto.codigo, produto.descricao, produto.codCategoria, produto.codClassificacao, produto.codMarca, produto.preco, produto.foto1)
              db.session.commit()
              return {
                   "message": "Produto atualizado com sucesso",
                   "status": 200
              }
          except Exception as e:
              return 'Não foi possível atualizar o produto: {}'.format(str(e)), 405

    elif request.method == 'DELETE':
        try:
            codigo = int(request.args.to_dict().get('codigo'))
            produto = Produto.query.get(codigo)
            if produto is None: 
                return {'error': 'Produto não encontrado'}, 404
            db.session.delete(produto)
            db.session.commit()
            return 'Produto deletado com sucesso', 200
        except Exception as e:
            return 'Não foi possível deletar o produto: {}'.format(str(e)), 405
